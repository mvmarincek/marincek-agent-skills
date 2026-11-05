/**
 * @module whatsapp/formatter
 * Brazil phone number formatting utilities
 *
 * Brazilian mobile numbers:
 * - Country code: +55
 * - Area code: 2 digits (11-99)
 * - Mobile prefix: 9 (added as 9th digit since 2012)
 * - Number: 8 digits total (9 + 7)
 * - Full format: +55 XX 9XXXX-XXXX
 */

/**
 * Format a Brazilian phone number to E.164 format
 * Handles various input formats:
 * - "11999887766" → "+5511999887766"
 * - "5511999887766" → "+5511999887766"
 * - "+5511999887766" → "+5511999887766"
 * - "whatsapp:+5511999887766" → "+5511999887766"
 * - "11 99988-7766" → "+5511999887766"
 *
 * @param {string} phone - Input phone number
 * @returns {string} Formatted phone number in E.164 (+55XXXXXXXXXXX)
 */
export function formatBrazilPhone(phone) {
  if (!phone) return '';

  // Remove WhatsApp prefix
  let cleaned = phone.replace('whatsapp:', '');

  // Remove all non-digit characters except leading +
  const hasPlus = cleaned.startsWith('+');
  cleaned = cleaned.replace(/\D/g, '');

  // If it already has country code
  if (cleaned.startsWith('55') && cleaned.length >= 12) {
    return `+${cleaned}`;
  }

  // If it starts with 0 (old trunk prefix), remove it
  if (cleaned.startsWith('0')) {
    cleaned = cleaned.slice(1);
  }

  // Add 9th digit if missing (landline→mobile migration)
  // Mobile numbers: area code (2 digits) + 9 + 8 digits = 11 digits without country code
  // If we have 10 digits (area + 8 digit number), insert 9 after area code
  if (cleaned.length === 10 && !cleaned.startsWith('55')) {
    const areaCode = cleaned.slice(0, 2);
    const number = cleaned.slice(2);
    // Only add 9 for mobile ranges (starting with 6-9)
    if (['6', '7', '8', '9'].includes(number[0])) {
      cleaned = `${areaCode}9${number}`;
    }
  }

  // Add country code if not present
  if (!cleaned.startsWith('55')) {
    cleaned = `55${cleaned}`;
  }

  return `+${cleaned}`;
}

/**
 * Validate if a phone number is a valid Brazilian mobile
 * @param {string} phone - Phone number to validate
 * @returns {boolean} Whether the number is valid
 */
export function isValidBrazilMobile(phone) {
  const formatted = formatBrazilPhone(phone);
  // +55 (2 digits area) (9 digits number) = +55XXXXXXXXXXX (14 chars)
  const regex = /^\+55[1-9][1-9]9\d{8}$/;
  return regex.test(formatted);
}

/**
 * Extract area code (DDD) from a Brazilian phone number
 * @param {string} phone - Phone number
 * @returns {string} Area code (2 digits)
 */
export function extractDDD(phone) {
  const formatted = formatBrazilPhone(phone);
  return formatted.slice(3, 5); // Skip +55
}
