/**
 * @module conversation/confirmation
 * Order confirmation and payment flow
 */

import { v4 as uuidv4 } from 'uuid';
import { sendMessage } from '../whatsapp/client.js';
import { templates } from '../whatsapp/templates.js';
import { STATES } from './state-machine.js';
import { generatePixLink } from '../payments/pix-generator.js';

/**
 * Handle confirmation state — confirm order and send PIX link
 * @param {object} session - Current session
 * @param {string} message - Normalized message text
 */
export async function handleConfirmation(session, message) {
  if (session.state === STATES.CONFIRMING) {
    const confirmKeywords = ['sim', 'confirmo', 'confirmar', 'ok', 's', '1'];
    const cancelKeywords = ['nao', 'não', 'cancelar', 'voltar', 'n', '2'];

    if (confirmKeywords.includes(message)) {
      // Generate order ID and PIX link
      session.order.id = uuidv4();

      const pixResult = await generatePixLink({
        orderId: session.order.id,
        amount: session.order.total,
        description: `Pedido ${session.order.id.slice(0, 8)}`,
      });

      session.state = STATES.AWAITING_PAYMENT;

      await sendMessage(
        session.phoneNumber,
        templates.pixPayment(pixResult, session.order)
      );
    } else if (cancelKeywords.includes(message)) {
      // Go back to ordering
      session.state = STATES.ORDERING;
      await sendMessage(session.phoneNumber, templates.orderCancelled());
    } else {
      await sendMessage(session.phoneNumber, templates.confirmHelp());
    }
    return;
  }

  if (session.state === STATES.AWAITING_PAYMENT) {
    // While waiting for payment, just acknowledge
    await sendMessage(session.phoneNumber, templates.awaitingPayment());
  }
}
