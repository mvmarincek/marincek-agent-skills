import 'dotenv/config';
import express from 'express';
import { config } from './config.js';
import { handleWebhook, verifyWebhook } from './webhook/handler.js';
import { handlePaymentCallback } from './webhook/payment-callback.js';

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

/** Health check endpoint */
app.get('/health', (_req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

/** WhatsApp webhook verification (GET) */
app.get('/webhook', verifyWebhook);

/** WhatsApp incoming messages (POST) */
app.post('/webhook', handleWebhook);

/** PIX payment callback (POST) */
app.post('/webhook/payment', handlePaymentCallback);

app.listen(config.port, () => {
  console.log(`🤖 WhatsApp Bot running on port ${config.port}`);
  console.log(`📋 Store: ${config.storeName}`);
  if (config.mockPayments) {
    console.log('⚠️  MOCK_PAYMENTS=true — PIX payments are simulated');
  }
});

export default app;
