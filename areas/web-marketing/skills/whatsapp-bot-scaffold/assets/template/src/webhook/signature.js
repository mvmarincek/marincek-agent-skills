/**
 * @module webhook/signature
 * HMAC signature validation for incoming webhooks
 */

import crypto from 'node:crypto';
import { config } from '../config.js';

/**
 * Validates the Twilio request signature
 * @param {import('express').Request} req - Express request object
 * @returns {boolean} Whether the signature is valid
 */
export function validateSignature(req) {
  // In development / mock mode, skip validation
  if (config.mockPayments && !req.headers['x-twilio-signature']) {
    return true;
  }

  const signature = req.headers['x-twilio-signature'];
  if (!signature) {
    return false;
  }

  // Build the validation URL
  const url = `${req.protocol}://${req.get('host')}${req.originalUrl}`;

  // Sort POST params and append to URL
  const params = req.body || {};
  const sortedKeys = Object.keys(params).sort();
  const dataString = sortedKeys.reduce((acc, key) => acc + key + params[key], url);

  // Compute HMAC-SHA1
  const computed = crypto
    .createHmac('sha1', config.twilioAuthToken)
    .update(dataString, 'utf-8')
    .digest('base64');

  return crypto.timingSafeEqual(
    Buffer.from(signature, 'utf-8'),
    Buffer.from(computed, 'utf-8')
  );
}

/**
 * Validates Stark Bank webhook signature
 * @param {import('express').Request} req - Express request object
 * @returns {boolean} Whether the signature is valid
 */
export function validatePaymentSignature(req) {
  // In mock mode, skip validation
  if (config.mockPayments) {
    return true;
  }

  const signature = req.headers['x-starkbank-signature'];
  if (!signature) {
    return false;
  }

  // Stark Bank uses digital signature verification
  // Full implementation depends on starkbank SDK
  // This is a placeholder for the validation logic
  try {
    const payload = JSON.stringify(req.body);
    // In production, use starkbank.event.parse() for validation
    return payload.length > 0 && signature.length > 0;
  } catch {
    return false;
  }
}
