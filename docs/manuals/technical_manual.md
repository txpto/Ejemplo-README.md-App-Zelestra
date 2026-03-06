# Manual técnico

## 1. Objetivo

Este documento sirve como referencia para personal técnico encargado de instalar, configurar, mantener o ampliar la solución.

## 2. Módulos técnicos

- motor de adquisición IEC102
- motor de adquisición Modbus TCP
- servicio de historización
- motor de alarmas
- capa API
- frontend SCADA

## 3. Archivos clave

- `config/system.yaml`
- `config/catalogs/meters.csv`
- `config/catalogs/meter_historization.csv`
- `config/catalogs/meteo_stations.csv`
- `database/schema.sql`

## 4. Arranque lógico del sistema

1. carga de configuración global
2. carga de catálogos CSV
3. validación básica de integridad
4. inicialización de conectores
5. activación de polling
6. activación de historian y alarm engine
7. exposición de interfaz y servicios externos

## 5. Consideraciones de mantenimiento

- revisar coherencia entre inventario y topología real
- revisar latencias y timeouts de red
- validar crecimiento de base de datos
- planificar backups
- revisar logs de reconexión y backfill

## 6. Ampliaciones ordinarias

Las ampliaciones típicas deben resolverse por configuración:

- alta de contadores
- alta de estaciones meteo
- modificación de periodos de historización
- activación de nuevas plantas

## 7. Ampliaciones no ordinarias

Requieren intervención de desarrollo:

- incorporación de un protocolo no soportado
- nuevas reglas complejas de negocio
- cambios profundos de modelo de datos
- integración con un nuevo estándar externo
