# Visión general del sistema

## 1. Propósito

La aplicación tiene como objetivo centralizar la adquisición, historización, visualización e integración de datos procedentes de:

- contadores IEC60870-5-102
- estaciones meteorológicas Modbus TCP
- servicios internos de alarmas y reporting

La plataforma ha sido diseñada para operar en entornos industriales de plantas solares fotovoltaicas, con foco en continuidad operativa, trazabilidad de datos y mantenibilidad a largo plazo.

## 2. Capacidades principales

- adquisición periódica de valores instantáneos
- historización de variables seleccionadas
- recuperación automática de huecos de datos
- visualización de estados y variables en interfaz SCADA
- gestión básica de alarmas
- integración con sistemas externos

## 3. Principios de diseño

- separación clara entre lógica de negocio y configuración
- crecimiento mediante parametrización, no mediante recodificación
- documentación suficiente para transferencia tecnológica
- bajo acoplamiento entre adquisición, historización y visualización
- trazabilidad de eventos de comunicación y calidad de dato

## 4. Bloques funcionales

### 4.1 Equipos de campo
Constituidos por contadores eléctricos y estaciones meteorológicas.

### 4.2 Capa de adquisición
Encargada de establecer comunicaciones, ejecutar polling, normalizar datos y detectar incidencias.

### 4.3 Capa de procesado
Incluye validación, historización, cálculo de estados y recuperación de huecos históricos.

### 4.4 Persistencia
Base de datos relacional para configuración operativa, lecturas históricas, eventos y alarmas.

### 4.5 Exposición e interfaz
API, servicios de integración y pantallas de operación.

## 5. Escalabilidad funcional

La plataforma admite ampliación a:

- nuevos contadores
- nuevas plantas
- nuevas estaciones meteorológicas
- nuevas señales
- nuevos periodos de historización

sin modificar código fuente para ampliaciones estándar, siempre que el tipo de equipo y protocolo ya estén soportados.
