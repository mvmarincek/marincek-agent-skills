/**
 * @module whatsapp/templates
 * Message template definitions (Portuguese - Brazil)
 */

/**
 * Format currency in BRL
 * @param {number} cents - Amount in cents
 * @returns {string} Formatted string e.g. "R$ 19,90"
 */
function formatBRL(cents) {
  return `R$ ${(cents / 100).toFixed(2).replace('.', ',')}`;
}

export const templates = {
  /**
   * Welcome message for first contact
   */
  welcome(userName, storeName) {
    return (
      `Olá, ${userName}! 👋\n\n` +
      `Bem-vindo(a) ao *${storeName}*!\n` +
      `Aqui você pode fazer seu pedido direto pelo WhatsApp.\n\n` +
      `Antes de começar, preciso da sua autorização para continuar.`
    );
  },

  /**
   * LGPD consent request
   */
  lgpdConsent(storeName) {
    return (
      `📋 *Aviso de Privacidade (LGPD)*\n\n` +
      `Para processar seu pedido, o *${storeName}* precisa coletar:\n` +
      `• Seu número de telefone\n` +
      `• Itens do pedido\n` +
      `• Dados de pagamento (PIX)\n\n` +
      `Seus dados são usados apenas para processar pedidos e não são compartilhados com terceiros.\n\n` +
      `Você pode solicitar a exclusão dos seus dados a qualquer momento.\n\n` +
      `*Você concorda?* Responda:\n` +
      `1️⃣ Sim, concordo\n` +
      `2️⃣ Não concordo`
    );
  },

  /**
   * Consent accepted confirmation
   */
  consentAccepted() {
    return (
      `✅ Obrigado! Seus dados estão protegidos.\n\n` +
      `Vou mostrar nosso cardápio agora! 🍔`
    );
  },

  /**
   * Consent denied message
   */
  consentDenied() {
    return (
      `Entendido! Sem problemas. 🙏\n\n` +
      `Sem o consentimento, não podemos processar pedidos.\n` +
      `Se mudar de ideia, é só mandar uma mensagem!`
    );
  },

  /**
   * Display menu
   */
  menu(menuData) {
    let text = `📋 *CARDÁPIO*\n\n`;
    let index = 1;

    for (const category of menuData.categories) {
      text += `━━━ *${category.name}* ━━━\n`;
      for (const item of category.items) {
        text += `${index}. ${item.name} — ${formatBRL(item.price)}\n`;
        if (item.description) {
          text += `   _${item.description}_\n`;
        }
        index++;
      }
      text += '\n';
    }

    return text;
  },

  /**
   * Menu usage instructions
   */
  menuInstructions() {
    return (
      `Para pedir, envie o *número* ou *nome* do item.\n` +
      `Exemplo: "1" ou "x-burger"\n\n` +
      `Quando terminar, envie *pronto* para fechar o pedido.`
    );
  },

  /**
   * Item added to order
   */
  itemAdded(item, order) {
    return (
      `✅ *${item.name}* adicionado!\n\n` +
      `🛒 Carrinho: ${order.items.length} item(ns)\n` +
      `💰 Total: ${formatBRL(order.total)}\n\n` +
      `Deseja mais alguma coisa?\n` +
      `• Envie outro número para adicionar\n` +
      `• "cardapio" para ver o menu\n` +
      `• "pronto" para finalizar`
    );
  },

  /**
   * Item not found
   */
  itemNotFound() {
    return (
      `❌ Não encontrei esse item no cardápio.\n` +
      `Envie "cardapio" para ver as opções disponíveis.`
    );
  },

  /**
   * Item removed from order
   */
  itemRemoved(item, order) {
    return (
      `🗑️ *${item.name}* removido do pedido.\n` +
      `💰 Total: ${formatBRL(order.total)}`
    );
  },

  /**
   * Item not found in order (for removal)
   */
  itemNotFoundInOrder() {
    return `❌ Esse item não está no seu pedido.`;
  },

  /**
   * Empty order warning
   */
  emptyOrder() {
    return (
      `🛒 Seu carrinho está vazio!\n` +
      `Envie "cardapio" para ver o menu.`
    );
  },

  /**
   * Order summary for confirmation
   */
  orderSummary(order) {
    let text = `📝 *RESUMO DO PEDIDO*\n\n`;

    for (const item of order.items) {
      const qty = item.quantity > 1 ? ` x${item.quantity}` : '';
      text += `• ${item.name}${qty} — ${formatBRL(item.price * item.quantity)}\n`;
    }

    text += `\n━━━━━━━━━━━━━━━\n`;
    text += `*TOTAL: ${formatBRL(order.total)}*\n\n`;
    text += `Confirma o pedido?\n`;
    text += `1️⃣ Sim, confirmar\n`;
    text += `2️⃣ Não, voltar ao menu`;

    return text;
  },

  /**
   * PIX payment instructions
   */
  pixPayment(pixResult, order) {
    return (
      `💳 *PAGAMENTO PIX*\n\n` +
      `Valor: *${formatBRL(order.total)}*\n\n` +
      `Copie o código PIX abaixo:\n\n` +
      `\`\`\`\n${pixResult.pixCode}\`\`\`\n\n` +
      `⏱️ Válido por 30 minutos.\n` +
      `Aguardando confirmação do pagamento...`
    );
  },

  /**
   * Payment confirmed
   */
  paymentConfirmed(order) {
    return (
      `✅ *PAGAMENTO CONFIRMADO!*\n\n` +
      `Seu pedido está sendo preparado! 🍳\n\n` +
      `📋 Pedido: #${order.id.slice(0, 8)}\n` +
      `💰 Valor: ${formatBRL(order.total)}\n\n` +
      `Obrigado pela preferência! 🙏`
    );
  },

  /**
   * Order cancelled (back to menu)
   */
  orderCancelled() {
    return (
      `↩️ Pedido cancelado. Voltamos ao menu.\n` +
      `Envie "cardapio" para ver as opções.`
    );
  },

  /**
   * Help during confirmation
   */
  confirmHelp() {
    return (
      `Responda:\n` +
      `1️⃣ *Sim* para confirmar o pedido\n` +
      `2️⃣ *Não* para voltar e alterar`
    );
  },

  /**
   * Waiting for payment
   */
  awaitingPayment() {
    return (
      `⏳ Ainda aguardando o pagamento PIX.\n` +
      `Assim que o pagamento for confirmado, você receberá uma notificação aqui!`
    );
  },

  /**
   * Help during ordering
   */
  orderHelp() {
    return (
      `🤔 Não entendi. Você pode:\n` +
      `• Enviar um *número* para adicionar item\n` +
      `• "cardapio" para ver o menu\n` +
      `• "remover [nome]" para tirar um item\n` +
      `• "pronto" para finalizar`
    );
  },
};
