/**
 * @module conversation/order
 * Order building — add/remove items, calculate total
 */

import { sendMessage } from '../whatsapp/client.js';
import { templates } from '../whatsapp/templates.js';
import { STATES } from './state-machine.js';
import { findMenuItem } from './menu.js';

/**
 * Handle ordering state — add items, show summary, finalize
 * @param {object} session - Current session
 * @param {string} message - Normalized message text
 */
export async function handleOrder(session, message) {
  const finalizeKeywords = ['pronto', 'fechar', 'finalizar', 'pedir', 'ok', 'confirmar'];
  const menuKeywords = ['cardapio', 'cardápio', 'menu', 'mais'];
  const removeKeywords = ['remover', 'tirar', 'remove'];

  // User wants to see menu again
  if (menuKeywords.includes(message)) {
    const { handleMenu } = await import('./menu.js');
    session.state = STATES.MENU;
    await handleMenu(session, 'cardapio');
    return;
  }

  // User wants to remove an item
  if (removeKeywords.some((kw) => message.startsWith(kw))) {
    const itemName = message.replace(/^(remover|tirar|remove)\s*/i, '');
    const idx = session.order.items.findIndex((i) =>
      i.name.toLowerCase().includes(itemName)
    );
    if (idx >= 0) {
      const removed = session.order.items.splice(idx, 1)[0];
      session.order.total -= removed.price * removed.quantity;
      await sendMessage(session.phoneNumber, templates.itemRemoved(removed, session.order));
    } else {
      await sendMessage(session.phoneNumber, templates.itemNotFoundInOrder());
    }
    return;
  }

  // User wants to finalize order
  if (finalizeKeywords.includes(message)) {
    if (session.order.items.length === 0) {
      await sendMessage(session.phoneNumber, templates.emptyOrder());
      return;
    }
    session.state = STATES.CONFIRMING;
    await sendMessage(session.phoneNumber, templates.orderSummary(session.order));
    return;
  }

  // Try to add another item
  const selected = findMenuItem(message);
  if (selected) {
    // Check if item already in order
    const existing = session.order.items.find((i) => i.name === selected.item.name);
    if (existing) {
      existing.quantity += 1;
    } else {
      session.order.items.push({
        name: selected.item.name,
        price: selected.item.price,
        quantity: 1,
      });
    }
    session.order.total += selected.item.price;

    await sendMessage(
      session.phoneNumber,
      templates.itemAdded(selected.item, session.order)
    );
  } else {
    await sendMessage(session.phoneNumber, templates.orderHelp());
  }
}
