# Modelo de datos

## 1. Entidades principales

### meters
Inventario de contadores configurados.

Campos típicos:
- id
- meter_name
- link_address
- measurement_point
- ip_address
- tcp_port
- physical_location
- psfv_project
- enabled

### meteo_stations
Inventario de estaciones meteorológicas.

### parameters
Catálogo de variables manejadas por la aplicación.

### historical_readings
Tabla de histórico principal.

Campos típicos:
- id
- asset_type
- asset_name
- signal_name
- timestamp_utc
- value
- quality
- source_protocol

### alarms
Registro de alarmas y eventos operativos.

### communication_status
Estado más reciente de cada equipo.

## 2. Criterios de diseño

- timestamps normalizados
- nombres de señal estables y versionables
- separación entre catálogo e histórico
- posibilidad de particionado futuro por fecha o proyecto
- capacidad de explotación por reporting y API

## 3. Calidad de dato

Se recomienda clasificar la calidad con etiquetas como:

- GOOD
- BAD
- UNCERTAIN
- RECOVERED

La marca RECOVERED es especialmente útil para identificar datos introducidos durante procesos de relleno de huecos históricos.
