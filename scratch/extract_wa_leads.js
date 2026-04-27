/**
 * WhatsApp Lead Extractor - LithiumBateriasPro
 * Instrucciones:
 * 1. Abrir WhatsApp Web (web.whatsapp.com)
 * 2. Presionar F12 para abrir la Consola.
 * 3. Pegar este código y presionar Enter.
 * 4. Se descargará un archivo 'whatsapp_leads.json'.
 */

(function() {
    console.log("Iniciando extracción de leads...");
    
    // Selectores (pueden cambiar con actualizaciones de WA)
    const CHAT_SELECTOR = 'div[role="listitem"]';
    const NAME_SELECTOR = 'span[title]';
    const MSG_SELECTOR = 'span.selectable-text.copyable-text'; // Último mensaje en la lista
    const UNREAD_SELECTOR = 'span[aria-label*="unread"]'; // Aproximado

    const chats = document.querySelectorAll(CHAT_SELECTOR);
    const results = [];

    chats.forEach(chat => {
        try {
            const nameEl = chat.querySelector('span[title]');
            const name = nameEl ? nameEl.getAttribute('title') : "Desconocido";
            
            // Intentar obtener el último mensaje de la previsualización
            // WhatsApp usa diferentes estructuras, buscamos texto legible
            const msgEl = chat.querySelector('span[dir="ltr"]'); 
            const lastMsg = msgEl ? msgEl.innerText : "";
            
            const unreadEl = chat.querySelector('span[aria-label]');
            const unread = unreadEl ? unreadEl.innerText : "0";

            // Si no hay mensaje, tal vez no es un chat válido o es un grupo
            if (name && lastMsg) {
                results.push({
                    contact: name,
                    lastMessage: lastMsg,
                    unreadCount: unread,
                    timestamp: new Date().toISOString()
                });
            }
        } catch (e) {
            console.error("Error en chat:", e);
        }
    });

    if (results.length === 0) {
        alert("No se encontraron chats. Asegúrate de estar en la pestaña de chats y que la lista esté cargada.");
        return;
    }

    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(results, null, 2));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", "whatsapp_leads.json");
    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();

    console.log(`Extracción finalizada: ${results.length} leads encontrados.`);
})();
