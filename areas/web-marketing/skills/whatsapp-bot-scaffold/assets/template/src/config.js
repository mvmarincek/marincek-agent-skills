/**
 * @module config
 * Environment configuration loader with validation
 */

/** @type {Record<string, string>} Required environment variables */
const REQUIRED_VARS = {
  TWILIO_ACCOUNT_SID: 'Twilio Account SID',
  TWILIO_AUTH_TOKEN: 'Twilio Auth Token',
  TWILIO_WHATSAPP_NUMBER: 'Twilio WhatsApp Number',
  WEBHOOK_VERIFY_TOKEN: 'Webhook Verify Token',
};

/** @type {Record<string, string>} Conditionally required (when MOCK_PAYMENTS=false) */
const PAYMENT_VARS = {
  STARKBANK_PROJECT_ID: 'Stark Bank Project ID',
  STARKBANK_PRIVATE_KEY: 'Stark Bank Private Key',
};

const mockPayments = process.env.MOCK_PAYMENTS === 'true';

// Validate required vars
const missing = [];
for (const [key, label] of Object.entries(REQUIRED_VARS)) {
  if (!process.env[key]) {
    missing.push(`  - ${key} (${label})`);
  }
}

if (!mockPayments) {
  for (const [key, label] of Object.entries(PAYMENT_VARS)) {
    if (!process.env[key]) {
      missing.push(`  - ${key} (${label})`);
    }
  }
}

if (missing.length > 0) {
  console.warn('⚠️  Missing environment variables:');
  missing.forEach((m) => console.warn(m));
  console.warn('   Bot may not function correctly. See .env.example');
}

export const config = {
  port: parseInt(process.env.PORT || '3000', 10),

  // Twilio
  twilioAccountSid: process.env.TWILIO_ACCOUNT_SID || '',
  twilioAuthToken: process.env.TWILIO_AUTH_TOKEN || '',
  twilioWhatsappNumber: process.env.TWILIO_WHATSAPP_NUMBER || '',

  // Webhook
  webhookVerifyToken: process.env.WEBHOOK_VERIFY_TOKEN || '',

  // Stark Bank (PIX)
  starkbankProjectId: process.env.STARKBANK_PROJECT_ID || '',
  starkbankPrivateKey: process.env.STARKBANK_PRIVATE_KEY || '',

  // Feature flags
  mockPayments,

  // Store info
  storeName: process.env.STORE_NAME || 'Lanchonete',
  storeCnpj: process.env.STORE_CNPJ || '',
};
