/**
 * @module webhook/payment-callback
 * PIX payment confirmation webhook handler
 */

import { validatePaymentSignature } from './signature.js';
import { validatePayment } from '../payments/pix-validator.js';
import { sendMessage } from '../whatsapp/client.js';
import { templates } from '../whatsapp/templates.js';
import { getSessionByOrderId, updateSessionState } from '../conversation/state-machine.js';

/**
 * POST /webhook/payment — Handle PIX payment confirmations
 * @param {import('express').Request} req
 * @param {import('express').Response} res
 */
export async function handlePaymentCallback(req, res) {
  try {
    if (!validatePaymentSignature(req)) {
      console.warn('⚠️  Invalid payment webhook signature');
      return res.status(401).json({ error: 'Invalid signature' });
    }

    const { event } = req.body;

    if (!event || event.type !== 'payment.confirmed') {
      return res.status(200).json({ status: 'ignored' });
    }

    const { orderId, amount } = event.data;
    console.log(`💰 Payment confirmed: Order ${orderId} — R$ ${(amount / 100).toFixed(2)}`);

    // Find the conversation session for this order
    const session = getSessionByOrderId(orderId);
    if (!session) {
      console.warn(`⚠️  No session found for order ${orderId}`);
      return res.status(200).json({ status: 'no_session' });
    }

    // Validate payment amount matches order
    const isValid = await validatePayment(orderId, amount);
    if (!isValid) {
      console.error(`❌ Payment amount mismatch for order ${orderId}`);
      return res.status(200).json({ status: 'amount_mismatch' });
    }

    // Update session state
    updateSessionState(session.phoneNumber, 'PAYMENT_CONFIRMED');

    // Notify customer
    await sendMessage(
      session.phoneNumber,
      templates.paymentConfirmed(session.order)
    );

    res.status(200).json({ status: 'processed' });
  } catch (error) {
    console.error('❌ Payment callback error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
}
