import urllib.request
import urllib.error
import json
import ssl
from collections import defaultdict

# Configuración
API_URL = "https://lithiumbaterias.com.ar/api/get-analytics" # Cambiado a URL de producción
API_KEY = "lithium-secreto-123"

def fetch_analytics():
    print(">> Conectando con la base de datos de Analytics de Lithium...")
    
    req = urllib.request.Request(API_URL)
    req.add_header('Authorization', f'Bearer {API_KEY}')
    req.add_header('Content-Type', 'application/json')
    
    try:
        # ctx = ssl.create_default_context()
        # ctx.check_hostname = False
        # ctx.verify_mode = ssl.CERT_NONE
        
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        return data.get('data', [])
    except urllib.error.URLError as e:
        print(f"❌ Error al conectar con el servidor: {e.reason}")
        if hasattr(e, 'code') and e.code == 401:
            print("❌ Error: Token de autorización inválido.")
        return None
    except json.JSONDecodeError:
        print("❌ Error: Respuesta del servidor no es un JSON válido.")
        return None

def process_and_display(analytics_list):
    if not analytics_list:
        print("\n[!] No hay datos analíticos para mostrar aún.")
        return

    total_sessions = len(analytics_list)
    total_time = sum(item.get('timeSpentSeconds', 0) for item in analytics_list)
    avg_time = total_time / total_sessions if total_sessions > 0 else 0
    
    total_whatsapp_clicks = sum(item.get('whatsappClicks', 0) for item in analytics_list)
    avg_scroll = sum(item.get('maxScrollPercentage', 0) for item in analytics_list) / total_sessions if total_sessions > 0 else 0

    print("\n" + "="*50)
    print(" REPORTE DE ANALYTICS - LITHIUM ELECTRÓNICA")
    print("="*50)
    print(f" Visitas Registradas (Sesiones): {total_sessions}")
    print(f" Tiempo Promedio en la Página: {avg_time:.1f} segundos")
    print(f" Porcentaje Promedio de Scroll: {avg_scroll:.1f}%")
    print(f" Clics Totales en WhatsApp: {total_whatsapp_clicks}")
    
    # Calcular tasa de conversión (sesiones con al menos un clic)
    sessions_with_clicks = sum(1 for item in analytics_list if item.get('whatsappClicks', 0) > 0)
    conversion_rate = (sessions_with_clicks / total_sessions * 100) if total_sessions > 0 else 0
    print(f" Tasa de Conversión (Visita -> WhatsApp): {conversion_rate:.1f}%")
    print("="*50 + "\n")

    print("[v] Últimas 5 visitas:")
    # Ordenar por fecha, más reciente primero
    sorted_analytics = sorted(analytics_list, key=lambda x: x.get('recordedAt', ''), reverse=True)
    for i, item in enumerate(sorted_analytics[:5]):
        print(f"  {i+1}. Fecha: {item.get('recordedAt', 'N/A')[:19]}")
        print(f"     Tiempo: {item.get('timeSpentSeconds', 0)}s | Scroll: {item.get('maxScrollPercentage', 0)}% | Clics WA: {item.get('whatsappClicks', 0)}")
        print(f"     Plataforma: {item.get('userAgent', 'N/A')[:40]}...")
        print("-" * 30)

if __name__ == "__main__":
    data = fetch_analytics()
    if data is not None:
        process_and_display(data)
