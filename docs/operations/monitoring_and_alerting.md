# Monitorización y alertado

## 1. Objetivo

Detectar de forma temprana problemas de:

- conectividad
- rendimiento
- inserción en base de datos
- acumulación de backlog
- errores de configuración

## 2. Métricas recomendadas

- tiempo medio de polling por equipo
- número de equipos online/offline
- número de reconexiones por hora
- número de insert fallidos
- longitud del backlog de recuperación
- tiempo desde la última lectura válida

## 3. Alarmas recomendadas

### Críticas
- base de datos no accesible
- caída completa de adquisición
- pérdida de acceso a interfaz principal

### Medias
- equipo sin comunicación prolongada
- latencia anómala de polling
- aumento de backlog de recuperación

### Bajas
- timeout puntual
- intento de reconexión exitoso
- aviso de mantenimiento programado
