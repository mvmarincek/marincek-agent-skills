/**
 * @module whatsapp/client
 * WhatsApp API client via Twilio
 */

import { config } from '../config.js';
import { formatBrazilPhone } from './formatter.js';

/** @type {object|null} Twilio client instance */
let twilioClient = null;

/**
 * Get or initialize Twilio client (async)
 * @returns {Promise<object|null>} Twilio client
 */
async function getClient() {
  if (!twilioClient) {
    try {
      const twilio = (await import('twilio')).default;
      twilioClient = twilio(config.twilioAccountSid, config.twilioAuthToken);
    } catch (error) {
      console.error('❌ Failed to initialize Twilio client:', error.message);
      return null;
    }
  }
  return twilioClient;
}

/**
 * Send a WhatsApp message
 * @param {string} to - Recipient phone number (raw or formatted)
 * @param {string} body - Message text
 * @returns {Promise<{success: boolean, messageId?: string, error?: string}>}
 */
export async function sendMessage(to, body) {
  const formattedTo = formatBrazilPhone(to);

  // Log in development
  if (config.mockPayments) {
    console.log(`📤 [MSG] To: ${formattedTo}`);
    console.log(`   ${body.slice(0, 100)}${body.length > 100 ? '...' : ''}`);
  }

  if (!config.twilioAccountSid || !config.twilioAuthToken) {
    console.warn('⚠️  Twilio not configured — message not sent');
    return { success: false, error: 'Twilio not configured' };
  }

  try {
    const client = await getClient();
    if (!client) {
      return { success: false, error: 'Twilio client unavailable' };
    }

    const message = await client.messages.create({
      from: config.twilioWhatsappNumber,
      to: `whatsapp:${formattedTo}`,
      body,
    });

    return { success: true, messageId: message.sid };
  } catch (error) {
    console.error(`❌ Failed to send message to ${formattedTo}:`, error.message);
    return { success: false, error: error.message };
  }
}
