/**
 * @module conversation/greeting
 * First contact greeting and LGPD consent flow
 */

import { sendMessage } from '../whatsapp/client.js';
import { templates } from '../whatsapp/templates.js';
import { recordConsent } from '../utils/lgpd.js';
import { STATES } from './state-machine.js';
import { config } from '../config.js';

/**
 * Handle greeting state — first contact + LGPD consent
 * @param {object} session - Current session
 * @param {string} message - Normalized message text
 */
export async function handleGreeting(session, message) {
  if (session.state === STATES.NEW) {
    // First message — send welcome + LGPD notice
    await sendMessage(
      session.phoneNumber,
      templates.welcome(session.userName || 'amigo', config.storeName)
    );
    await sendMessage(session.phoneNumber, templates.lgpdConsent(config.storeName));
    session.state = STATES.AWAITING_CONSENT;
    return;
  }

  if (session.state === STATES.AWAITING_CONSENT) {
    const positiveResponses = ['sim', 'aceito', 'ok', 'concordo', 's', '1', 'yes'];

    if (positiveResponses.includes(message)) {
      // LGPD consent given
      session.consentGiven = true;
      recordConsent(session.phoneNumber, true);

      await sendMessage(session.phoneNumber, templates.consentAccepted());
      session.state = STATES.MENU;
      // Show menu immediately
      const { handleMenu } = await import('./menu.js');
      await handleMenu(session, 'cardapio');
    } else {
      // Consent denied — inform and close
      session.consentGiven = false;
      recordConsent(session.phoneNumber, false);

      await sendMessage(session.phoneNumber, templates.consentDenied());
      session.state = STATES.COMPLETED;
    }
  }
}
