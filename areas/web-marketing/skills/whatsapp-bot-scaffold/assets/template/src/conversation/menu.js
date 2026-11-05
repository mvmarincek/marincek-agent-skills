/**
 * @module conversation/menu
 * Menu display and item selection parsing
 */

import { sendMessage } from '../whatsapp/client.js';
import { templates } from '../whatsapp/templates.js';
import { STATES } from './state-machine.js';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const menuPath = join(__dirname, '..', 'data', 'menu.json');

/** @type {object} Loaded menu data */
let menuData;
try {
  menuData = JSON.parse(readFileSync(menuPath, 'utf-8'));
} catch {
  console.error('❌ Failed to load menu.json');
  menuData = { categories: [] };
}

/**
 * Get all menu items as a flat list with indices
 * @returns {Array<{index: number, item: object, category: string}>}
 */
export function getMenuItems() {
  const items = [];
  let index = 1;
  for (const category of menuData.categories) {
    for (const item of category.items) {
      items.push({ index, item, category: category.name });
      index++;
    }
  }
  return items;
}

/**
 * Find a menu item by number or name
 * @param {string} input - User input (number or partial name)
 * @returns {object|null}
 */
export function findMenuItem(input) {
  const items = getMenuItems();

  // Try by number
  const num = parseInt(input, 10);
  if (!isNaN(num)) {
    const found = items.find((i) => i.index === num);
    return found || null;
  }

  // Try by name (partial match)
  const normalized = input.toLowerCase();
  return items.find((i) => i.item.name.toLowerCase().includes(normalized)) || null;
}

/**
 * Handle menu state — display menu and parse selections
 * @param {object} session - Current session
 * @param {string} message - Normalized message text
 */
export async function handleMenu(session, message) {
  const menuKeywords = ['cardapio', 'cardápio', 'menu', 'ver menu', 'opcoes', 'opções'];

  if (menuKeywords.includes(message) || session.state === STATES.MENU) {
    // If it's a menu keyword, show menu
    if (menuKeywords.includes(message)) {
      await sendMessage(session.phoneNumber, templates.menu(menuData));
      await sendMessage(session.phoneNumber, templates.menuInstructions());
      return;
    }

    // Try to parse item selection
    const selected = findMenuItem(message);
    if (selected) {
      session.order.items.push({
        name: selected.item.name,
        price: selected.item.price,
        quantity: 1,
      });
      session.order.total += selected.item.price;
      session.state = STATES.ORDERING;

      await sendMessage(
        session.phoneNumber,
        templates.itemAdded(selected.item, session.order)
      );
    } else {
      await sendMessage(session.phoneNumber, templates.itemNotFound());
    }
  }
}
