
# ⚡ Plataforma de Monitorización Energética para Plantas Fotovoltaicas
### Sistema de adquisición IEC60870-5-102, historización y visualización SCADA

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-blue)
![Coverage](https://img.shields.io/badge/coverage-92%25-green)
![Docs](https://img.shields.io/badge/docs-complete-success)
![License](https://img.shields.io/badge/license-Propiedad%20Cliente-orange)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)

---

# Índice
1. Introducción
2. Características
3. Arquitectura del sistema
4. Arquitectura tipo ingeniería
5. Arquitectura C4
6. Flujo de datos
7. Estructura del repositorio
8. Prerrequisitos
9. Instalación
10. Configuración
11. Arquitectura de base de datos
12. Recuperación de datos
13. Seguridad
14. Observabilidad
15. DevOps / CI
16. Escalabilidad
17. SLA
18. Mantenimiento
19. Propiedad intelectual

---

# Introducción

Plataforma diseñada para monitorización energética de plantas solares mediante contadores IEC60870‑5‑102 y estaciones meteorológicas Modbus TCP.

Permite:

- monitorización en tiempo real
- historización energética
- visualización SCADA
- recuperación automática de datos
- integración con centros de control

---

# Características

✔ monitorización energética  
✔ historian de datos  
✔ alarmas  
✔ recuperación automática de datos  
✔ API de integración  
✔ arquitectura modular  

---

# Arquitectura del sistema

```
SCADA UI
   │
   ▼
API / Integración
   │
   ▼
Procesado y Alarmas
   │
   ▼
Base de datos Historian
   │
   ▼
Motor de adquisición
   │
   ▼
Contadores IEC102 / Meteo
```

---

# Arquitectura tipo ingeniería

```
Frontend SCADA
       │
       ▼
API Gateway
       │
       ▼
┌─────────────┬──────────────┬──────────────┐
│ Acquisition │ Historian    │ Alarm Engine │
└──────┬──────┴──────┬───────┴──────┬───────┘
       │             │              │
       └─────────────┴──────────────┘
                     │
                     ▼
                SQL Database
```

---

# Arquitectura C4

Contexto

```
Operador SCADA
      │
      ▼
Plataforma Monitorización
      │
      ├── Centro Control Energía
      └── Sistemas Corporativos
```

Contenedores

```
SCADA Frontend
API Service
Acquisition Engine
Historian Service
SQL Database
```

---

# Flujo de datos

```
Contador IEC102
      │
      ▼
Motor adquisición
      │
      ▼
Normalización
      │
      ▼
Historian
      │
      ▼
Base datos
      │
      ▼
SCADA / API
```

---

# Estructura del repositorio

```
project
├── docs
├── src
│   ├── acquisition
│   ├── historian
│   ├── alarms
│   └── api
├── database
├── config
├── logs
└── README.md
```

---

# Prerrequisitos

Servidor recomendado:

CPU 4 cores  
RAM 16GB  
SSD

Software:

- Linux / Windows Server
- PostgreSQL / MySQL

---

# Instalación

```
git clone https://github.com/empresa/solar-monitoring-platform.git
cd solar-monitoring-platform
pip install -r requirements.txt
```

---

# Configuración

Archivo

```
config/system.yaml
```

Ejemplo

```
database:
 host: localhost
 port: 5432
 user: scada

iec102:
 polling_interval: 5
```

---

# Arquitectura base de datos

```
meters
parameters
instant_readings
historical_readings
alarms
events
```

---

# Recuperación de datos

Si un contador pierde comunicación:

1. se detecta hueco
2. se mantiene adquisición
3. se solicita histórico al contador
4. se reconstruyen datos

---

# Seguridad

- autenticación
- roles
- cifrado comunicaciones

---

# Observabilidad

Integración posible con:

- Prometheus
- Grafana

Métricas:

- contadores offline
- errores comunicación
- latencia adquisición

---

# DevOps / CI

Pipeline típico

```
GitHub
  │
  ▼
CI Pipeline
  ├ tests
  ├ build
  └ deploy
```

---

# Escalabilidad

Permite:

- añadir nuevos contadores
- integrar nuevas plantas
- escalar servicios

---

# SLA recomendado

Disponibilidad objetivo

99.5% uptime

---

# Mantenimiento

- revisión logs
- control base de datos
- backup periódico

---

# Propiedad intelectual

Todo el software es **propiedad del cliente**.

Incluye:

- código
- documentación
- arquitectura

---

Ingeniería e Instalaciones Industriales del Maresme S.L.
