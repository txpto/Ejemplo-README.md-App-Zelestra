# Modelo de configuración

## 1. Filosofía

La aplicación utiliza una configuración externa basada en:

- YAML para parámetros globales
- CSV para inventario de activos
- CSV para reglas de historización

Esto permite ampliar la solución sin modificar código fuente.

## 2. Ficheros esperados

- `config/system.yaml`
- `config/catalogs/meters.csv`
- `config/catalogs/meter_historization.csv`
- `config/catalogs/meteo_stations.csv`

## 3. Reglas

- todo equipo debe tener identificador único
- una señal no debe definirse dos veces para la misma entidad y periodo
- los cambios en CSV deben validarse antes de pasar a producción
- los CSV deben mantenerse bajo control de versiones

## 4. Flujo de cambio recomendado

1. editar plantilla
2. validar sintaxis y consistencia
3. aplicar en preproducción
4. comprobar conectividad y tags
5. desplegar en producción
