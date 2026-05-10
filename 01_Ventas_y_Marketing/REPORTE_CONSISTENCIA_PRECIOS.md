# 🔍 REPORTE DE CONSISTENCIA DE PRECIOS - 04/05/2026

Este archivo sirve para unificar los criterios comerciales y evitar confusiones en los presupuestos. 

---

### ⚠️ DISCREPANCIAS DETECTADAS (PARA REVISIÓN)
Actualmente hay una diferencia entre los precios de la Web y los precios que estuve calculando hoy. **Mañana debemos decidir cuál de estos valores queda "clavado" como oficial.**

| Modelo | Precio en Web (Landing) | Precio en Lista Interna (Actual) | Estado |
| :--- | :--- | :--- | :--- |
| **24V 20Ah** | $385.000 | $385.000 | ✅ Sincronizado |
| **36V 10Ah** | $495.000 | $485.000 | ❌ Desfasado |
| **48V 15Ah** | $695.000 | $645.000 | ❌ Desfasado |
| **60V 20Ah** | $1.095.000 | $1.095.000 | ✅ Sincronizado |

---

### 📏 REGLA DE ORO PARA EL ASISTENTE (ANTIGRAVITY)
1. **NUNCA** modificar un precio en `index.html` o `lista_precios_resumida.txt` sin confirmación explícita de Marcos.
2. **SIEMPRE** verificar este archivo antes de pasar un presupuesto por WhatsApp para asegurar que el cliente reciba el mismo valor que vio en la web.
3. **COHERENCIA:** Un modelo más chico (ej: 60V 15Ah) **siempre** debe ser más barato que el modelo superior (60V 20Ah).

---
*Nota: Este reporte se generó para limpiar la confusión del día 04/05. Mañana se espera la validación de Marcos para unificar la columna "Oficial".*
