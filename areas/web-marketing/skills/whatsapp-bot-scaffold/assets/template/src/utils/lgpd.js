/**
 * @module utils/lgpd
 * LGPD (Lei Geral de Proteção de Dados) compliance helpers
 *
 * Brazil's data protection law requires:
 * - Explicit consent before data collection
 * - Right to access collected data
 * - Right to deletion (right to be forgotten)
 * - Data minimization (collect only what's necessary)
 */

/**
 * In-memory consent registry
 * In production, use a persistent database
 * @type {Map<string, {consent: boolean, timestamp: Date, version: string}>}
 */
const consentRegistry = new Map();

/** Current LGPD notice version */
const LGPD_VERSION = '1.0';

/**
 * Record a user's consent decision
 * @param {string} phoneNumber - User's phone number (hashed in production)
 * @param {boolean} consented - Whether the user gave consent
 */
export function recordConsent(phoneNumber, consented) {
  consentRegistry.set(phoneNumber, {
    consent: consented,
    timestamp: new Date(),
    version: LGPD_VERSION,
  });

  console.log(
    `📋 [LGPD] Consent ${consented ? 'given' : 'denied'} by ${phoneNumber.slice(-4)}`
  );
}

/**
 * Check if a user has given consent
 * @param {string} phoneNumber
 * @returns {boolean}
 */
export function hasConsent(phoneNumber) {
  const record = consentRegistry.get(phoneNumber);
  return record?.consent === true;
}

/**
 * Get consent record for a user (for data access requests)
 * @param {string} phoneNumber
 * @returns {object|null}
 */
export function getConsentRecord(phoneNumber) {
  return consentRegistry.get(phoneNumber) || null;
}

/**
 * Revoke consent and delete user data
 * @param {string} phoneNumber
 * @returns {boolean} Whether revocation was successful
 */
export function revokeConsent(phoneNumber) {
  if (consentRegistry.has(phoneNumber)) {
    consentRegistry.delete(phoneNumber);
    console.log(`📋 [LGPD] Consent revoked and data deleted for ${phoneNumber.slice(-4)}`);
    return true;
  }
  return false;
}

/**
 * Get all data stored for a user (data portability / access request)
 * @param {string} phoneNumber
 * @returns {object} All stored user data
 */
export function getUserData(phoneNumber) {
  return {
    phoneNumber: phoneNumber.slice(0, 4) + '***' + phoneNumber.slice(-2),
    consent: consentRegistry.get(phoneNumber) || null,
    lgpdVersion: LGPD_VERSION,
    exportedAt: new Date().toISOString(),
  };
}

/**
 * LGPD privacy notice text (for API/endpoint use)
 * @returns {string}
 */
export function getPrivacyNoticeText() {
  return (
    'Este serviço coleta seu número de telefone e dados de pedido ' +
    'exclusivamente para processar suas solicitações. ' +
    'Seus dados não são compartilhados com terceiros. ' +
    'Você pode solicitar acesso ou exclusão dos seus dados ' +
    'a qualquer momento enviando "meus dados" ou "excluir dados".'
  );
}
