# 🚨 LISTA ROJA: MARCAS PROPIETARIAS Y BLOQUEOS
**Guía Técnica para Filtrado de Presupuestos - Lithium Electronica**

En el mundo de las baterías de litio, existen marcas que utilizan **protocolos de comunicación cerrados** (CanBus o UART propietarios) entre la batería, el controlador y el motor. Si reemplazamos sus celdas o su BMS por uno genérico, el vehículo no arrancará o mostrará errores fatales.

---

## 🟥 LISTA ROJA (Evitar o Rechazar por defecto)
Estas baterías son prácticamente **irreparables** con componentes genéricos. Solo se pueden reparar si el fallo es mecánico (un cable suelto) o si se mantienen las celdas con voltaje durante el cambio (procedimiento de altísimo riesgo).

### 1. BOSCH (E-bikes)
*   **Problema:** Si el BMS detecta que se desconectaron las celdas, entra en un "Hard Lock" (bloqueo por software) permanente.
*   **Protocolo:** CanBus encriptado. No acepta BMS genéricos.
*   **Diagnóstico:** Si la batería no prende luces o el cargador original no la reconoce, está "muerta" para nosotros.

### 2. SHIMANO STEPS / SPECIALIZED / YAMAHA / GIANT
*   **Problema:** Sistemas integrados de alta gama. El motor "interroga" a la batería por su número de serie y salud. 
*   **Síntoma:** "Error de comunicación" en el display al intentar encender con otro pack.

---

## 🟨 LISTA AMARILLA (Tomar con precaución / Costo extra)
Estas baterías se pueden reparar, pero **requieren placas BMS específicas** para ese modelo, no las que tenemos en stock.

### 1. XIAOMI (M365, Pro, Mi Scooter)
*   **Bloqueo:** El sistema de luces y el display dependen de la comunicación con el BMS original. 
*   **Solución:** Se puede reparar cambiando las celdas **MANTENIENDO EL BMS ORIGINAL** (siempre que este no se haya bloqueado por descarga profunda). Si el BMS original murió, hay que comprar un "BMS Clon Xiaomi" específico. **No sirve el BMS de 10S genérico.**

### 2. SEGWAY-NINEBOT (Serie ES, MAX G30)
*   **Bloqueo:** Muy similar a Xiaomi. El controlador del monopatín muestra "Error 21" (fallo de comunicación) si no detecta el BMS original.

### 3. MONOPATINES PHILCO / FIAT / FOSTON
*   **Riesgo:** Algunos traen protecciones por software, otros son 100% genéricos. Siempre pedir foto del BMS antes de presupuestar.

---

## 📋 PROTOCOLO DE FILTRADO (WhatsApp)
Cuando un cliente consulta por estas marcas, el vendedor **NUNCA debe dar un precio fijo** de inmediato. Debe usar este mensaje:

> *"Estuvimos revisando tu modelo. Al ser una marca con electrónica propietaria (Bosch/Xiaomi/Shimano), estos equipos tienen protecciones de software que pueden bloquear la batería al ser intervenida. Necesitamos recibirla en el taller para hacer un **Diagnóstico de Viabilidad ($X.XXX)** antes de confirmar si el trasplante de celdas es posible. Si el BMS original está bloqueado, es posible que el equipo no acepte componentes genéricos."*

---

## 💡 REGLA DE ORO DEL TALLER
Si la batería tiene **más de 3 cables** de salida (ej. tiene cables finos de datos además del Positivo y Negativo gruesos), es una **Batería con Comunicación**. 
**¡ALERTA MÁXIMA!** Consultar con el Jefe antes de pasar cualquier presupuesto.
