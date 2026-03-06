# Troubleshooting

## 1. No aparecen nuevos datos en pantalla

Comprobar:
- servicio de adquisición activo
- conectividad IP
- puerto TCP accesible
- logs de timeout
- estado de base de datos

## 2. Un contador aparece en gris

Comprobar:
- IP y puerto en CSV
- dirección de enlace
- disponibilidad real del contador
- firewall intermedio
- último evento de comunicación

## 3. El histórico presenta huecos

Comprobar:
- si existió pérdida de comunicación
- si el proceso de backfill está activo
- si el contador soporta recuperación del periodo faltante
- si hay errores de inserción en base de datos

## 4. Una estación meteorológica no muestra datos

Comprobar:
- IP y puerto configurados
- timeout Modbus
- mapeo de registros
- calidad de datos recibidos

## 5. La aplicación arranca pero no carga equipos

Comprobar:
- rutas en `system.yaml`
- existencia de CSV
- cabeceras correctas
- codificación UTF-8
- campos obligatorios no vacíos
