
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

1. [Introducción](#introducción)
2. [Características](#características)
3. [Arquitectura general del sistema](#arquitectura-general-del-sistema)
4. [Diagrama C4 de arquitectura](#diagrama-c4-de-arquitectura)
5. [Arquitectura estilo Cloud / AWS](#arquitectura-estilo-cloud--aws)
6. [Flujo de datos del sistema](#flujo-de-datos-del-sistema)
7. [UML de la base de datos](#uml-de-la-base-de-datos)
8. [Estructura del repositorio GitHub](#estructura-del-repositorio-github)
9. [Prerrequisitos](#prerrequisitos)
10. [Instalación](#instalación)
11. [Configuración](#configuración)
12. [Observabilidad](#observabilidad)
13. [DevOps / CI](#devops--ci)
14. [SLA recomendado](#sla-recomendado)
15. [Propiedad intelectual](#propiedad-intelectual)

---

# Introducción

Plataforma de monitorización energética diseñada para plantas solares que permite la adquisición de datos desde contadores IEC60870-5-102 y estaciones meteorológicas Modbus TCP.

Permite:

- monitorización en tiempo real
- historización energética
- recuperación automática de datos
- visualización SCADA
- integración con centros de control

La solución se diseña como **software industrial robusto y completamente documentado**.

---

# Características

✔ adquisición de datos IEC60870-5-102  
✔ integración Modbus TCP  
✔ historian energético  
✔ recuperación automática de datos  
✔ gestión de alarmas  
✔ API de integración externa  
✔ arquitectura escalable  

---

# Arquitectura general del sistema

```
        +-----------------------+
        |        SCADA UI       |
        +-----------+-----------+
                    |
                    v
        +-----------------------+
        |      API Gateway      |
        +-----------+-----------+
                    |
                    v
+---------+---------+----------+---------+
| Acquisition | Historian | Alarm Engine |
+---------+---------+----------+---------+
                    |
                    v
           +----------------+
           | SQL Database   |
           +----------------+
                    |
                    v
           Contadores / Meteo
```

---

# Diagrama C4 de arquitectura

## Nivel Contexto

```
             +---------------------+
             |  Operador SCADA     |
             +----------+----------+
                        |
                        v
            +-----------------------+
            | Plataforma Monitorización |
            +-----------+-----------+
                        |
          +-------------+-------------+
          |                           |
          v                           v
  Centro Control Energía      Sistemas Corporativos
```

---

# Arquitectura estilo Cloud / AWS

```
                +---------------------+
                |  Internet / VPN     |
                +----------+----------+
                           |
                           v
                +---------------------+
                |   Load Balancer     |
                +----------+----------+
                           |
                           v
                +---------------------+
                |   SCADA Web Server  |
                +----------+----------+
                           |
                           v
                +---------------------+
                |   API Application   |
                +----------+----------+
                           |
                           v
           +---------------+---------------+
           |                               |
           v                               v
   Acquisition Engine                 Historian Engine
           |                               |
           +---------------+---------------+
                           |
                           v
                    SQL Database
```

---

# Flujo de datos del sistema

```
Contador IEC102
      │
      ▼
Motor adquisición
      │
      ▼
Normalización datos
      │
      ▼
Historian
      │
      ▼
Base de datos
      │
      ▼
SCADA / API
```

---

# UML de la base de datos

```
+-------------+
|   meters    |
+-------------+
| id PK       |
| name        |
| location    |
+------+------
       |
       | 1
       |
       | n
+------+------------------+
| historical_readings     |
+-------------------------+
| id PK                   |
| meter_id FK             |
| timestamp               |
| value                   |
+-------------------------+

+-------------+
| alarms      |
+-------------+
| id PK       |
| meter_id FK |
| level       |
| message     |
| timestamp   |
+-------------+
```

---

# Estructura del repositorio GitHub

```
solar-monitoring-platform

├── docs
│   ├── architecture
│   │   ├── c4-diagrams.md
│   │   ├── system-architecture.md
│   │   └── database-uml.md
│   │
│   ├── manuals
│   │   ├── user-manual.md
│   │   └── technical-manual.md
│
├── src
│   ├── acquisition
│   ├── historian
│   ├── alarms
│   ├── api
│   └── integrations
│
├── database
│   ├── schema.sql
│   └── migrations
│
├── config
│   └── system.yaml
│
├── scripts
│   ├── deploy.sh
│   └── backup.sh
│
└── README.md
```

---

# Prerrequisitos

Servidor recomendado

CPU: 4 cores  
RAM: 16GB  
Disco: SSD  

Software

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

Archivo principal

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

# Observabilidad

Integración posible con:

- Prometheus
- Grafana

Métricas clave

- latencia adquisición
- contadores offline
- errores comunicación

---

# DevOps / CI

Pipeline

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

# SLA recomendado

Disponibilidad objetivo

99.5 % uptime

Tiempo respuesta incidencias

Crítica < 4h  
Media < 24h  
Baja < 72h  

---

# Propiedad intelectual

El software desarrollado es **propiedad del cliente**, incluyendo:

- código fuente
- arquitectura
- documentación

Esto garantiza independencia tecnológica y mantenimiento por terceros.

---

Ingeniería e Instalaciones Industriales del Maresme S.L.
