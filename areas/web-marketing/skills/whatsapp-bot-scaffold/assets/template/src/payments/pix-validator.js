/**
 * @module payments/pix-validator
 * Payment status verification
 */

import { config } from '../config.js';

/**
 * In-memory order registry for amount validation
 * @type {Map<string, number>}
 */
const orderAmounts = new Map();

/**
 * Register an order's expected amount
 * @param {string} orderId
 * @param {number} amount - Amount in BRL cents
 */
export function registerOrderAmount(orderId, amount) {
  orderAmounts.set(orderId, amount);
}

/**
 * Validate that a payment matches the expected order amount
 * @param {string} orderId - Order identifier
 * @param {number} paidAmount - Amount paid in BRL cents
 * @returns {Promise<boolean>} Whether the payment is valid
 */
export async function validatePayment(orderId, paidAmount) {
  if (config.mockPayments) {
    // In mock mode, always valid
    return true;
  }

  const expectedAmount = orderAmounts.get(orderId);
  if (!expectedAmount) {
    console.warn(`⚠️  No registered amount for order ${orderId}`);
    return true; // Allow if not registered (webhook may arrive before registration)
  }

  // Allow 1 cent tolerance for rounding
  const isValid = Math.abs(expectedAmount - paidAmount) <= 1;

  if (!isValid) {
    console.error(
      `❌ Amount mismatch: expected ${expectedAmount}, got ${paidAmount} for order ${orderId}`
    );
  }

  return isValid;
}

/**
 * Check payment status with Stark Bank
 * @param {string} orderId - Order identifier
 * @returns {Promise<'pending'|'confirmed'|'failed'>}
 */
export async function checkPaymentStatus(orderId) {
  if (config.mockPayments) {
    return 'confirmed';
  }

  try {
    const starkbank = await import('starkbank');
    const brcodes = await starkbank.default.dynamicBrcode.query({
      tags: [orderId],
      limit: 1,
    });

    for await (const brcode of brcodes) {
      if (brcode.status === 'paid') return 'confirmed';
      if (brcode.status === 'expired' || brcode.status === 'canceled') return 'failed';
    }

    return 'pending';
  } catch (error) {
    console.error(`❌ Error checking payment status:`, error);
    return 'pending';
  }
}
