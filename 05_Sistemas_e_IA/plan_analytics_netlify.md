# Plan de Implementación Futuro: Sistema de Analytics Propio con Netlify

*Nota: Este plan fue pausado temporalmente. Cuando haya cuota disponible, retomaremos esta implementación.*

**Directorio Objetivo:** `C:\Users\Marcos\Documents\Landingpage lithium` (Página oficial activa).

## Arquitectura Propuesta

### 1. Backend (Servidor Netlify)
- **Instalación:** Inicializar `package.json` para instalar dependencias `@netlify/functions` y `@netlify/blobs`.
- **Configuración:** Crear `netlify.toml` para definir la ubicación de las funciones.
- **Función Receptora (`netlify/functions/track-analytics.mts`):** Una función Serverless que recibe los "eventos" de los clientes (tiempo de navegación, clics) y los guarda en la base de datos gratuita de Netlify Blobs.
- **Función de Lectura (`netlify/functions/get-analytics.mts`):** Un endpoint seguro que expone la información recopilada de los Blobs para consumo interno.

### 2. Frontend (Landing Page `index.html`)
- **Script de Tracking:** Inyectar un código JavaScript nativo y ligero justo antes de la etiqueta `</body>`.
- **Eventos a medir:** 
  - Tiempo total que el usuario pasó en la página.
  - Clics en enlaces de WhatsApp o botones de conversión.
  - Scroll depth (cuánto de la página leyeron).
- **Envío de datos:** Al momento de cerrar la pestaña, usar `navigator.sendBeacon()` para enviar la métrica al backend sin entorpecer la carga ni afectar al SEO de Google.

### 3. Herramienta de Lectura Interna
- **Script Local (`C:\Users\Marcos\Documents\LithiumBateriasPro\05_Sistemas_e_IA\leer_analytics.py`):** Un archivo Python diseñado para ser ejecutado por la IA. Se conectará al endpoint seguro de Netlify, descargará los datos del Blob, los procesará y generará un reporte diario o semanal en texto plano, directamente en el chat.

---

*Para reactivar este plan, simplemente mencionarle al Asistente IA "Retomemos el plan de Analytics de Netlify" y la IA leerá este documento para comenzar a ejecutar el código.*
