# Visión general de API e integraciones

## 1. Objetivo

La API expone información consolidada para sistemas externos sin obligarles a acceder directamente a la base de datos.

## 2. Recursos típicos

- `/health`
- `/projects`
- `/meters`
- `/meters/{meter_name}`
- `/meters/{meter_name}/realtime`
- `/meters/{meter_name}/history`
- `/alarms`
- `/meteo-stations`
- `/status/communications`

## 3. Principios

- respuestas consistentes
- timestamps normalizados
- paginación en históricos
- filtrado por proyecto y rango temporal
- control de acceso por rol

## 4. Integraciones previstas

- centros de control ROC
- sistemas corporativos de reporting
- herramientas internas de explotación
