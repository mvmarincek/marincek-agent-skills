/**
 * @module conversation/state-machine
 * Conversation state management for WhatsApp interactions
 */

import { handleGreeting } from './greeting.js';
import { handleMenu } from './menu.js';
import { handleOrder } from './order.js';
import { handleConfirmation } from './confirmation.js';

/**
 * Conversation states
 * @enum {string}
 */
export const STATES = {
  NEW: 'NEW',
  AWAITING_CONSENT: 'AWAITING_CONSENT',
  MENU: 'MENU',
  ORDERING: 'ORDERING',
  CONFIRMING: 'CONFIRMING',
  AWAITING_PAYMENT: 'AWAITING_PAYMENT',
  PAYMENT_CONFIRMED: 'PAYMENT_CONFIRMED',
  COMPLETED: 'COMPLETED',
};

/**
 * In-memory session store
 * In production, replace with Redis or database
 * @type {Map<string, object>}
 */
const sessions = new Map();

/**
 * Get or create a session for a phone number
 * @param {string} phoneNumber
 * @param {string} [userName]
 * @returns {object} Session object
 */
export function getSession(phoneNumber, userName = '') {
  if (!sessions.has(phoneNumber)) {
    sessions.set(phoneNumber, {
      phoneNumber,
      userName,
      state: STATES.NEW,
      order: { items: [], total: 0, id: null },
      consentGiven: false,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
  }
  const session = sessions.get(phoneNumber);
  session.updatedAt = new Date();
  return session;
}

/**
 * Get session by order ID
 * @param {string} orderId
 * @returns {object|null}
 */
export function getSessionByOrderId(orderId) {
  for (const session of sessions.values()) {
    if (session.order?.id === orderId) {
      return session;
    }
  }
  return null;
}

/**
 * Update session state
 * @param {string} phoneNumber
 * @param {string} newState
 */
export function updateSessionState(phoneNumber, newState) {
  const session = sessions.get(phoneNumber);
  if (session) {
    session.state = newState;
    session.updatedAt = new Date();
  }
}

/**
 * Process an incoming message through the state machine
 * @param {object} params
 * @param {string} params.phoneNumber - Sender's phone number
 * @param {string} params.message - Message text
 * @param {string} params.userName - Sender's profile name
 */
export async function processMessage({ phoneNumber, message, userName }) {
  const session = getSession(phoneNumber, userName);
  const normalizedMessage = message.toLowerCase().trim();

  // Global commands (work in any state)
  if (normalizedMessage === 'cancelar' || normalizedMessage === 'sair') {
    session.state = STATES.NEW;
    session.order = { items: [], total: 0, id: null };
    // Reset handled in greeting
  }

  switch (session.state) {
    case STATES.NEW:
    case STATES.AWAITING_CONSENT:
      await handleGreeting(session, normalizedMessage);
      break;

    case STATES.MENU:
      await handleMenu(session, normalizedMessage);
      break;

    case STATES.ORDERING:
      await handleOrder(session, normalizedMessage);
      break;

    case STATES.CONFIRMING:
    case STATES.AWAITING_PAYMENT:
      await handleConfirmation(session, normalizedMessage);
      break;

    case STATES.PAYMENT_CONFIRMED:
    case STATES.COMPLETED:
      // Start new conversation
      session.state = STATES.NEW;
      session.order = { items: [], total: 0, id: null };
      await handleGreeting(session, normalizedMessage);
      break;

    default:
      session.state = STATES.NEW;
      await handleGreeting(session, normalizedMessage);
  }
}
