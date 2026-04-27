import json
import os

def analizar_leads(file_path):
    if not os.path.exists(file_path):
        print(f"Error: No se encuentra el archivo {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        leads = json.load(f)

    # Definir pesos de palabras clave
    keywords_hot = ["precio", "cuanto sale", "presupuesto", "cotizacion", "comprar", "stock", "tenes"]
    keywords_product = ["bateria", "litio", "celda", "pack", "monopatin", "bici", "bicicleta", "ups", "silla"]
    
    scored_leads = []

    for lead in leads:
        msg = lead.get('lastMessage', '').lower()
        score = 0
        
        # Scoring logic
        for kw in keywords_hot:
            if kw in msg:
                score += 3
        
        for kw in keywords_product:
            if kw in msg:
                score += 2
        
        # Bonus for unread messages (priority)
        try:
            unread = int(lead.get('unreadCount', '0'))
            score += min(unread, 5) 
        except:
            pass

        lead['score'] = score
        scored_leads.append(lead)

    # Sort by score descending
    scored_leads.sort(key=lambda x: x['score'], reverse=True)

    print("\n🔥 TOP LEADS (MAYOR PROBABILIDAD DE VENTA) 🔥")
    print("-" * 50)
    for i, lead in enumerate(scored_leads[:10]):
        print(f"{i+1}. {lead['contact']} - Score: {lead['score']}")
        print(f"   Ult. Msg: {lead['lastMessage']}")
        print("-" * 50)

if __name__ == "__main__":
    path = 'c:/Users/Marcos/Documents/LithiumBateriasPro/scratch/whatsapp_leads.json'
    analizar_leads(path)
