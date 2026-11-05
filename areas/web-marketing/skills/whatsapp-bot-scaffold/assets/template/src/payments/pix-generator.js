/**
 * @module payments/pix-generator
 * PIX payment link generation via Stark Bank (or mock)
 */

import { config } from '../config.js';
import { v4 as uuidv4 } from 'uuid';

/**
 * Generate a PIX payment link
 * @param {object} params
 * @param {string} params.orderId - Order identifier
 * @param {number} params.amount - Amount in BRL cents (e.g., 1990 = R$ 19.90)
 * @param {string} params.description - Payment description
 * @returns {Promise<{pixCode: string, pixLink: string, expiresAt: Date}>}
 */
export async function generatePixLink({ orderId, amount, description }) {
  if (config.mockPayments) {
    return generateMockPix({ orderId, amount, description });
  }

  return generateStarkBankPix({ orderId, amount, description });
}

/**
 * Mock PIX generation — returns fake link and auto-confirms after 3s
 * @param {object} params
 * @returns {Promise<{pixCode: string, pixLink: string, expiresAt: Date}>}
 */
async function generateMockPix({ orderId, amount, description }) {
  const mockCode = `00020126580014br.gov.bcb.pix0136${uuidv4()}5204000053039865404${(amount / 100).toFixed(2)}5802BR59${config.storeName.slice(0, 25)}6009SAO PAULO62140510${orderId.slice(0, 10)}6304`;

  const result = {
    pixCode: mockCode,
    pixLink: `https://pix.mock.local/pay/${orderId}`,
    expiresAt: new Date(Date.now() + 30 * 60 * 1000), // 30 min
  };

  // Auto-confirm payment after 3 seconds (mock mode)
  setTimeout(async () => {
    console.log(`🔄 [MOCK] Auto-confirming payment for order ${orderId}`);
    try {
      const response = await fetch(`http://localhost:${config.port}/webhook/payment`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          event: {
            type: 'payment.confirmed',
            data: { orderId, amount },
          },
        }),
      });
      if (response.ok) {
        console.log(`✅ [MOCK] Payment auto-confirmed for order ${orderId}`);
      }
    } catch (error) {
      console.error(`❌ [MOCK] Auto-confirm failed:`, error.message);
    }
  }, 3000);

  return result;
}

/**
 * Stark Bank PIX generation (production)
 * @param {object} params
 * @returns {Promise<{pixCode: string, pixLink: string, expiresAt: Date}>}
 */
async function generateStarkBankPix({ orderId, amount, description }) {
  // Dynamic import to avoid loading starkbank when in mock mode
  const starkbank = await import('starkbank');

  const payment = await starkbank.default.dynamicBrcode.create([
    {
      name: config.storeName,
      city: 'Sao Paulo',
      externalId: orderId,
      type: 'instant',
      amount: amount,
      expiration: 1800, // 30 minutes
      tags: ['order', orderId],
    },
  ]);

  const brcode = payment[0];

  return {
    pixCode: brcode.id,
    pixLink: brcode.url || `pix:${brcode.id}`,
    expiresAt: new Date(Date.now() + 30 * 60 * 1000),
  };
}
