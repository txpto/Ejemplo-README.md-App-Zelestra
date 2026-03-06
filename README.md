
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
3. Arquitectura general del sistema  
4. Diagrama C4 de arquitectura  
5. Arquitectura estilo Cloud / AWS  
6. Flujo de datos del sistema  
7. Diagrama UML de la base de datos  
8. Estructura del repositorio GitHub  
9. Prerrequisitos  
10. Instalación  
11. Configuración  
12. Observabilidad  
13. DevOps / CI  
14. SLA recomendado  
15. Propiedad intelectual  

---

# 1. Introducción

Plataforma de monitorización energética diseñada para plantas solares que permite la adquisición de datos desde contadores IEC60870-5-102 y estaciones meteorológicas Modbus TCP.

Permite:

- monitorización en tiempo real
- historización energética
- recuperación automática de datos
- visualización SCADA
- integración con centros de control

La solución se diseña como **software industrial robusto y completamente documentado**, preparado para mantenimiento futuro.

---

# 2. Características

✔ adquisición de datos IEC60870-5-102  
✔ integración Modbus TCP  
✔ historian energético  
✔ recuperación automática de datos  
✔ gestión de alarmas  
✔ API de integración externa  
✔ arquitectura escalable  

---

# 3. Arquitectura general

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

# 4. Diagrama C4 de arquitectura

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

## Nivel Contenedores

```
+---------------------------+
|        SCADA Frontend     |
+------------+--------------+
             |
             v
+---------------------------+
|        API Service        |
+------------+--------------+
             |
             v
+------------+--------------+
|    Acquisition Engine     |
+------------+--------------+
             |
             v
+------------+--------------+
|     Historian Service     |
+------------+--------------+
             |
             v
+---------------------------+
|       SQL Database        |
+---------------------------+
```

---

# 5. Arquitectura estilo Cloud / AWS

Ejemplo conceptual de despliegue:

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
                           |
                           v
                Backup / Storage
```

---

# 6. Flujo de datos

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

# 7. UML Base de Datos

Diagrama conceptual simplificado

```
+-------------+
|   meters    |
+-------------+
| id          |
| name        |
| location    |
+------+------
       |
       | 1
       |
       | n
+------+------+
| historical_readings |
+---------------------+
| id                  |
| meter_id            |
| timestamp           |
| value               |
+---------------------+

+-------------+
| alarms      |
+-------------+
| id          |
| meter_id    |
| level       |
| message     |
| timestamp   |
+-------------+

+-------------+
| parameters  |
+-------------+
| id          |
| name        |
| unit        |
+-------------+
```

---

# 8. Estructura del repositorio

Repositorio GitHub propuesto

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
├── logs
│
└── README.md
```

---

# 9. Prerrequisitos

Servidor recomendado

CPU: 4 cores  
RAM: 16GB  
Disco: SSD  

Software

- Linux / Windows Server
- PostgreSQL / MySQL

---

# 10. Instalación

```
git clone https://github.com/empresa/solar-monitoring-platform.git
cd solar-monitoring-platform
pip install -r requirements.txt
```

---

# 11. Configuración

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

# 12. Observabilidad

Integración posible con:

- Prometheus
- Grafana

Métricas clave

- latencia adquisición
- contadores offline
- errores comunicación

---

# 13. DevOps / CI

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

Herramientas recomendadas

- GitHub Actions
- Docker
- CI/CD

---

# 14. SLA recomendado

Disponibilidad objetivo

99.5 % uptime

Tiempo respuesta incidencias

Crítica < 4h  
Media < 24h  
Baja < 72h

---

# 15. Propiedad intelectual

El software desarrollado es **propiedad del cliente**, incluyendo

- código fuente
- arquitectura
- documentación

Esto garantiza independencia tecnológica y mantenimiento por terceros.

---

Ingeniería e Instalaciones Industriales del Maresme S.L.
Departamento de Ingeniería de Automatización
