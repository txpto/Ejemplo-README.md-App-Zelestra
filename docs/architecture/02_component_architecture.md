# Arquitectura de componentes

## 1. Componentes principales

### 1.1 Acquisition Engine
Responsable de:

- leer inventario de equipos desde CSV
- establecer sesiones de comunicación
- ejecutar ciclos de polling
- mapear respuestas a un modelo interno de variables
- publicar datos normalizados a la capa de procesado

### 1.2 Historian Service
Responsable de:

- filtrar variables historizables
- aplicar periodos de muestreo configurados
- insertar datos en base de datos
- registrar calidad y timestamp de adquisición
- lanzar procesos de backfill cuando procede

### 1.3 Alarm Engine
Responsable de:

- detectar pérdida de comunicación
- detectar cambios de estado relevantes
- emitir eventos y alarmas
- clasificar severidades
- mantener trazabilidad temporal

### 1.4 API Service
Responsable de:

- exponer datos consolidados a terceros
- proporcionar acceso a inventario, estados y datos históricos
- actuar como punto de integración con sistemas ROC o corporativos

### 1.5 SCADA / HMI
Responsable de:

- mostrar estado general de planta
- mostrar detalle por contador
- presentar históricos
- visualizar progreso de recuperación de datos
- mostrar alarmas recientes y estado operativo

## 2. Dependencias lógicas

El sistema debe mantener desacoplamiento suficiente para permitir:

- sustituir la interfaz sin reescribir adquisición
- escalar adquisición sin modificar persistencia
- ampliar integraciones sin tocar historización

## 3. Fallos controlados

Los componentes deben contemplar:

- reintento de comunicaciones
- degradación controlada del servicio
- persistencia de eventos de fallo
- recuperación ordenada tras reconexión
