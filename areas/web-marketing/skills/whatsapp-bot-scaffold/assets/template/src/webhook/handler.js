/**
 * @module webhook/handler
 * WhatsApp webhook verification and incoming message routing
 */

import { validateSignature } from './signature.js';
import { config } from '../config.js';
import { processMessage } from '../conversation/state-machine.js';

/**
 * GET /webhook — Twilio/Meta webhook verification
 * @param {import('express').Request} req
 * @param {import('express').Response} res
 */
export function verifyWebhook(req, res) {
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];

  // Meta-style verification
  if (mode === 'subscribe' && token === config.webhookVerifyToken) {
    console.log('✅ Webhook verified');
    return res.status(200).send(challenge);
  }

  // Twilio-style: just respond 200
  if (req.query.verify_token === config.webhookVerifyToken) {
    return res.status(200).json({ status: 'verified' });
  }

  return res.status(403).json({ error: 'Verification failed' });
}

/**
 * POST /webhook — Handle incoming WhatsApp messages
 * @param {import('express').Request} req
 * @param {import('express').Response} res
 */
export async function handleWebhook(req, res) {
  try {
    // Validate request signature
    if (!validateSignature(req)) {
      console.warn('⚠️  Invalid webhook signature');
      return res.status(401).json({ error: 'Invalid signature' });
    }

    const { From, Body, ProfileName } = req.body;

    if (!From || !Body) {
      return res.status(400).json({ error: 'Missing From or Body' });
    }

    const phoneNumber = From.replace('whatsapp:', '');
    const message = Body.trim();
    const userName = ProfileName || '';

    console.log(`📩 ${phoneNumber}: ${message}`);

    // Route to conversation state machine
    await processMessage({ phoneNumber, message, userName });

    // Twilio expects 200 quickly
    res.status(200).json({ status: 'received' });
  } catch (error) {
    console.error('❌ Webhook handler error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
}
