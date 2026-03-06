# Carpeta `src`

Esta carpeta contiene un esqueleto técnico realista de la aplicación, alineado con la filosofía del proyecto:

- crecimiento mediante configuración
- separación por dominios funcionales
- mantenibilidad
- claridad arquitectónica
- posibilidad de transferencia a terceros

## Estructura

- `acquisition/` → lectura IEC102 y Modbus TCP
- `historian/` → historización y backfill
- `alarms/` → alarmas y eventos
- `api/` → API de integración
- `integrations/` → adaptadores externos
- `common/` → utilidades comunes
- `main.py` → arranque de ejemplo
