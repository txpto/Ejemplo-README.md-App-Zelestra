# ⚡ Plataforma de Monitorización Energética para Plantas Fotovoltaicas
### Sistema de adquisición IEC60870-5-102, historización y visualización SCADA

<p align="left">
  <img src="https://img.shields.io/badge/build-passing-brightgreen" alt="build">
  <img src="https://img.shields.io/badge/version-1.0-blue" alt="version">
  <img src="https://img.shields.io/badge/coverage-92%25-green" alt="coverage">
  <img src="https://img.shields.io/badge/docs-complete-success" alt="docs">
  <img src="https://img.shields.io/badge/license-Propiedad%20Cliente-orange" alt="license">
  <img src="https://img.shields.io/badge/CI-GitHub%20Actions-blue" alt="ci">
</p>

---

## ✨ Resumen ejecutivo

Solución software industrial diseñada para la **monitorización energética de plantas solares**, con adquisición de datos desde contadores **IEC60870-5-102** y estaciones meteorológicas **Modbus TCP**, historización, alarmas, visualización SCADA e integración con sistemas externos.

### ✅ Qué aporta esta plataforma
- Monitorización en tiempo real
- Historización energética
- Recuperación automática de datos perdidos
- Gestión básica de alarmas
- Visualización SCADA
- Integración con centros de control
- Arquitectura modular y mantenible
- Propiedad intelectual del cliente

---

## 📚 Índice

- [✨ Resumen ejecutivo](#-resumen-ejecutivo)
- [🧭 Visión general](#-visión-general)
- [🚀 Características principales](#-características-principales)
- [🏗️ Arquitectura general del sistema](#️-arquitectura-general-del-sistema)
- [🧩 Diagrama C4 visual](#-diagrama-c4-visual)
- [☁️ Arquitectura estilo Cloud / AWS](#️-arquitectura-estilo-cloud--aws)
- [🗄️ Modelo de datos y UML](#️-modelo-de-datos-y-uml)
- [🌊 Flujo de datos](#-flujo-de-datos)
- [🗂️ Estructura del repositorio GitHub](#️-estructura-del-repositorio-github)
- [⚙️ Prerrequisitos](#️-prerrequisitos)
- [🛠️ Instalación](#️-instalación)
- [🔧 Configuración](#-configuración)
- [📈 Observabilidad](#-observabilidad)
- [🔄 DevOps / CI](#-devops--ci)
- [📋 SLA recomendado](#-sla-recomendado)
- [🔐 Propiedad intelectual](#-propiedad-intelectual)

---

## 🧭 Visión general

La plataforma se concibe como una solución de ingeniería software de propósito industrial, pensada para operar con continuidad y ser mantenida a largo plazo.

### Principios de diseño
- **Claridad arquitectónica**
- **Modularidad**
- **Escalabilidad**
- **Observabilidad**
- **Transferencia de conocimiento**
- **Independencia tecnológica del cliente**

> Esta documentación está pensada para que un tercero pueda comprender la arquitectura, desplegar el sistema y mantenerlo con garantías razonables.

---

## 🚀 Características principales

| Área | Capacidades |
|---|---|
| Adquisición | IEC60870-5-102, Modbus TCP, polling configurable |
| Historización | Registro de variables eléctricas y meteorológicas |
| Integración | API, exportación de datos, integración con ROC/centros de control |
| Explotación | SCADA, pantallas de detalle, vista general, alarmas |
| Continuidad | Recuperación automática de huecos de datos |
| Operación | Logs, métricas, observabilidad y soporte al mantenimiento |

---

## 🏗️ Arquitectura general del sistema

Separación en bloques funcionales para simplificar despliegue, operación y evolución.

```text
Campo → Adquisición → Procesado → Base de Datos → API/Integración → SCADA/UI
```

### Capas principales
1. **Equipos de campo**  
   Contadores IEC102 y estaciones meteorológicas.

2. **Capa de adquisición**  
   Motores de comunicación y normalización de datos.

3. **Capa de lógica**  
   Historian, alarmas, recuperación de huecos y servicios internos.

4. **Persistencia**  
   Base de datos relacional e histórico operativo.

5. **Exposición e interfaz**  
   API, integración externa, dashboards y pantallas SCADA.

---

## 🧩 Diagrama C4 visual

<p align="center">
  <img src="./diagrams/c4_architecture.svg" alt="Diagrama C4 de arquitectura" width="980">
</p>

### Lectura del diagrama
- **Operador SCADA** interactúa con la plataforma.
- **Plataforma de monitorización** centraliza adquisición, lógica y presentación.
- **Centro de control energético** y **sistemas corporativos** consumen información del sistema.

---

## ☁️ Arquitectura estilo Cloud / AWS

<p align="center">
  <img src="./diagrams/system_architecture_cloud.svg" alt="Arquitectura estilo cloud" width="980">
</p>

### Qué representa
- Punto de acceso seguro mediante **VPN / Internet corporativa**
- Capa de entrada mediante **Load Balancer**
- **Servidor web SCADA**
- **Servicio API**
- Motores especializados:
  - **Acquisition Engine**
  - **Historian Engine**
- **Base de datos SQL**
- **Backups / almacenamiento**

---

## 🗄️ Modelo de datos y UML

<p align="center">
  <img src="./diagrams/uml_database_schema.svg" alt="UML base de datos" width="980">
</p>

### Entidades clave
- **meters**: catálogo de contadores
- **historical_readings**: histórico de lecturas por contador
- **alarms**: eventos y estados de alarma
- **parameters**: metadatos de variables y unidades

---

## 🌊 Flujo de datos

```text
Contador IEC102 / Estación Meteo
        ↓
Motor de adquisición
        ↓
Normalización y validación
        ↓
Historian / Alarm Engine
        ↓
Base de datos
        ↓
API / SCADA / Reporting / ROC
```

---

## 🗂️ Estructura del repositorio GitHub

```text
solar-monitoring-platform/
├── README.md
├── docs/
├── diagrams/
├── src/
├── database/
├── config/
├── scripts/
└── tests/
```

---

## ⚙️ Prerrequisitos

### Hardware recomendado
- CPU: **4 cores** mínimo
- RAM: **16 GB** recomendados
- Disco: **SSD**
- Red: conectividad estable hacia equipos de campo y sistemas de integración

### Software base
- Linux o Windows Server
- PostgreSQL o MySQL
- Runtime de la aplicación
- Acceso a puertos y rutas de comunicación requeridos

---

## 🛠️ Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/txpto/Ejemplo-README.md-App-Zelestra.git
cd Ejemplo-README.md-App-Zelestra
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Revisar configuración

```bash
nano config/system.yaml
```

### 4. Lanzar servicios

```bash
./scripts/deploy.sh
```

---

## 🔧 Configuración

Archivo principal:

```text
config/system.yaml
```

Ejemplo:

```yaml
database:
  host: localhost
  port: 5432
  user: scada

iec102:
  polling_interval: 5

historian:
  retention_days: 3650
```

---

## 📈 Observabilidad

### Integraciones recomendadas
- **Prometheus**
- **Grafana**
- Logs centralizados
- Alertado por eventos críticos

### Métricas clave
- Latencia de adquisición
- Equipos offline
- Errores de comunicación
- Backlog de recuperación de datos
- Crecimiento de base de datos

---

## 🔄 DevOps / CI

Pipeline recomendado para un proyecto profesional:

```text
GitHub → CI Pipeline → Tests → Build → Artefactos → Despliegue controlado
```

### Herramientas compatibles
- GitHub Actions
- Docker
- Linters y validación estática
- Tests unitarios e integración

---

## 📋 SLA recomendado

### Disponibilidad objetivo
**99.5 % uptime**

### Tiempos de respuesta orientativos
- **Crítica**: < 4 horas
- **Media**: < 24 horas
- **Baja**: < 72 horas

---

## 🔐 Propiedad intelectual

Todo el software desarrollado es **propiedad del cliente**, incluyendo:

- Código fuente
- Arquitectura
- Documentación
- Diagramas
- Scripts de despliegue y operación

### Qué garantiza esto
- Independencia tecnológica
- Posibilidad de mantenimiento por terceros
- Evolución futura sin bloqueo tecnológico
- Seguridad para la continuidad operativa

---

## 🏁 Cierre

Esta documentación de ejemplo está pensada para mostrar cómo sería un repositorio serio y bien estructurado de una solución software industrial a medida.

**Ingeniería e Instalaciones Industriales del Maresme S.L.**  
Departamento de Ingeniería de Automatización
