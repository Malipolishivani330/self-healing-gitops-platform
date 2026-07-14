# 🚀 Production-Ready Cloud-Native Self-Healing GitOps Platform

> A production-inspired cloud-native microservices platform built using **FastAPI, Docker, Kubernetes, PostgreSQL, Prometheus, and Grafana**, demonstrating containerized application deployment, Kubernetes orchestration, self-healing capabilities, observability, and a GitOps-ready architecture.

---

## 📖 Project Overview

Modern cloud-native applications demand **high availability, scalability, resiliency, and observability**. Managing these applications manually becomes increasingly difficult as systems grow in complexity.

This project demonstrates how to build and deploy a **production-inspired microservices platform** by leveraging modern cloud-native technologies and Kubernetes best practices.

The platform is designed around independent microservices, each running in its own container and orchestrated by Kubernetes. It includes automated service discovery, centralized configuration management, monitoring, self-healing deployments, and production-style infrastructure components.

Unlike traditional monolithic applications, every service can be independently deployed, scaled, monitored, and recovered without affecting other services.

The project demonstrates practical implementation of:

- Containerized Microservices
- Kubernetes Orchestration
- Kubernetes Self-Healing
- Service Discovery
- Configuration Management
- Secrets Management
- Ingress Routing
- Monitoring & Observability
- Production Deployment Practices
- GitOps-Ready Architecture

This project is intended to simulate how modern applications are deployed in production Kubernetes environments while following cloud engineering best practices.

---

# 🏗️ Solution Architecture

```
                          Developer

                              │
                              ▼

                     Docker Image Build

                              │
                              ▼

                    Docker Compose (Local)

                              │
                              ▼

                     Kubernetes Cluster

         ┌─────────────────────────────────────┐
         │                                     │
         │      Kubernetes Control Plane       │
         │                                     │
         └─────────────────────────────────────┘

                │                     │

                ▼                     ▼

      User Service             Product Service

                │                     │

                └──────────┬──────────┘

                           ▼

                     PostgreSQL Database

                           │

                           ▼

                ConfigMap & Kubernetes Secrets

                           │

                           ▼

                    Kubernetes Services

                           │

                           ▼

                    NGINX Ingress Controller

                           │

                           ▼

                    Prometheus Monitoring

                           │

                           ▼

                     Grafana Dashboards

```

---

# ✨ Key Features

## ✅ Cloud-Native Microservices

- Independent User Service
- Independent Product Service
- RESTful API architecture
- FastAPI framework
- Modular project structure

---

## ✅ Containerization

- Dockerized microservices
- Lightweight Python images
- Multi-container deployment
- Docker Compose integration

---

## ✅ Kubernetes Orchestration

- Kubernetes Deployments
- ReplicaSets
- ClusterIP Services
- ConfigMaps
- Secrets
- Ingress Controller

---

## ✅ High Availability

Multiple application replicas ensure higher availability and fault tolerance.

Example:

- User Service → Multiple Pods
- Product Service → Multiple Pods

---

## ✅ Self-Healing

If a running pod becomes unavailable or is manually deleted:

- Kubernetes automatically detects the failure
- A replacement pod is scheduled
- Desired replica count is restored automatically

This demonstrates Kubernetes' built-in self-healing capability.

---

## ✅ Observability

Application monitoring is implemented using:

- Prometheus
- Grafana
- Kubernetes Metrics
- Pod Monitoring
- Cluster Monitoring

---

## ✅ Production-Oriented Design

The platform is designed following production-inspired architecture principles including:

- Stateless Microservices
- Service Isolation
- Independent Scaling
- Environment Configuration
- Infrastructure Separation
- Observability
- Declarative Kubernetes Resources

---

# ☁️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| Backend | FastAPI, Python |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| API Documentation | Swagger UI (OpenAPI) |
| Containerization | Docker |
| Multi-Container | Docker Compose |
| Container Orchestration | Kubernetes (Kind) |
| Networking | Kubernetes Services, NGINX Ingress |
| Configuration | ConfigMap |
| Secret Management | Kubernetes Secrets |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Version Control | Git |
| Repository | GitHub |

---

# 📁 Project Structure

```text
self-healing-gitops-platform/

├── .github/
│   └── workflows/
│
├── k8s/
│   ├── config/
│   ├── postgres/
│   ├── user-service/
│   ├── product-service/
│   ├── ingress/
│   └── monitoring/
│
├── services/
│   ├── user-service/
│   │   ├── app/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── .env
│   │
│   └── product-service/
│       ├── app/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── .env
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

# ⚙️ Architecture Workflow

The complete request flow of the application is illustrated below.

```
Client Request

      │

      ▼

NGINX Ingress Controller

      │

      ▼

Kubernetes Service

      │

      ▼

Deployment

      │

      ▼

Application Pod

      │

      ▼

PostgreSQL Database

      │

      ▼

Response Returned

```

At the infrastructure level:

```
Developer

     │

     ▼

Git Repository

     │

     ▼

Docker Build

     │

     ▼

Docker Images

     │

     ▼

Kubernetes Deployment

     │

     ▼

Pods

     │

     ▼

Services

     │

     ▼

Ingress

     │

     ▼

Prometheus

     │

     ▼

Grafana Dashboards

```

---

## 🎯 Project Objectives

This project was built to gain hands-on experience with modern cloud-native technologies and production deployment workflows.

The primary objectives include:

- Designing containerized microservices
- Deploying applications using Kubernetes
- Implementing service discovery and networking
- Managing application configuration using ConfigMaps and Secrets
- Demonstrating Kubernetes self-healing capabilities
- Monitoring workloads with Prometheus and Grafana
- Building a GitOps-ready architecture for future CI/CD automation
- Following production-inspired engineering practices suitable for cloud environments
- ---

# 🐳 Docker Implementation

Containerization is the foundation of this platform. Each microservice is independently packaged into lightweight Docker images, ensuring consistency across development and deployment environments.

## Why Docker?

Docker provides:

- Consistent runtime environment
- Dependency isolation
- Faster deployments
- Easy scalability
- Production-ready packaging
- Platform independence

---

## Dockerized Services

The following services are containerized:

| Service | Purpose |
|----------|---------|
| User Service | User Management APIs |
| Product Service | Product Management APIs |
| PostgreSQL | Persistent Database |

---

## Docker Build Workflow

```
Application Source Code

        │

        ▼

Dockerfile

        │

        ▼

Docker Build

        │

        ▼

Docker Image

        │

        ▼

Docker Container

        │

        ▼

Application Running
```

---

## Docker Images

The project builds independent Docker images for:

- User Service
- Product Service

Each image contains:

- FastAPI Application
- Python Runtime
- Required Dependencies
- Environment Configuration

---

## Multi-Container Deployment

Docker Compose was used to orchestrate multiple containers during local development.

Services include:

- User Service
- Product Service
- PostgreSQL

Benefits:

- Service networking
- Simplified development
- Faster testing
- Centralized container management

---

# ☸️ Kubernetes Deployment

After validating the application using Docker Compose, the platform was migrated to Kubernetes for orchestration.

Each application component was deployed as an independent Kubernetes workload.

---

## Kubernetes Resources Used

### Deployments

Deployments manage:

- Pod lifecycle
- Replica management
- Rolling updates
- Automatic recovery

Implemented Deployments:

- PostgreSQL
- User Service
- Product Service

---

### ReplicaSets

ReplicaSets ensure the desired number of application replicas remain available.

Example:

```
Desired Replicas = 2

Running Pods = 2

↓

Delete One Pod

↓

Running Pods = 1

↓

ReplicaSet Creates New Pod

↓

Running Pods = 2
```

---

### Services

ClusterIP Services provide internal communication between workloads.

Implemented Services:

- postgres-service
- user-service
- product-service

Responsibilities:

- Service discovery
- Internal networking
- Load balancing across replicas

---

### ConfigMap

Application configuration is externalized using ConfigMaps.

Examples include:

- Application Name
- Environment
- Version
- Database Host

Benefits:

- Environment separation
- Easy configuration updates
- Improved maintainability

---

### Secrets

Sensitive configuration is securely managed using Kubernetes Secrets.

Examples:

- Database Username
- Database Password

Benefits:

- Secure credential management
- Separation of configuration from code
- Production best practice

---

### NGINX Ingress

NGINX Ingress Controller provides a single entry point for external traffic.

Responsibilities:

- HTTP routing
- Path-based routing
- Reverse proxy
- Centralized access management

Architecture:

```
Client

   │

   ▼

Ingress Controller

   │

   ▼

User Service

Product Service

PostgreSQL
```

---

# 📊 Monitoring & Observability

A production platform requires continuous monitoring to ensure application reliability.

The project integrates Prometheus and Grafana to provide observability into Kubernetes workloads.

---

## Prometheus

Prometheus continuously collects metrics from the Kubernetes cluster.

Collected Metrics:

- Pod Health
- Service Availability
- Cluster Metrics
- Kubernetes Components
- Resource Usage

Benefits:

- Centralized metrics
- Time-series storage
- Real-time monitoring
- Production observability

---

## Grafana

Grafana visualizes Prometheus metrics through dashboards.

Implemented Dashboards:

- Kubernetes Cluster Dashboard
- Pod Metrics
- Cluster Health
- Application Monitoring

Benefits:

- Real-time dashboards
- Interactive visualization
- Infrastructure monitoring
- Performance analysis

---

## Monitoring Architecture

```
Kubernetes Cluster

        │

        ▼

Prometheus

        │

        ▼

Metrics Collection

        │

        ▼

Grafana

        │

        ▼

Dashboards
```

---

## Observability Features

The monitoring stack enables visibility into:

- Running Pods
- Kubernetes Deployments
- Cluster Health
- Replica Status
- Service Status
- Application Availability

---

# ❤️ Kubernetes Self-Healing Demonstration

One of the core objectives of this project was demonstrating Kubernetes' self-healing capabilities.

The application was deployed using Kubernetes Deployments with multiple replicas.

---

## Demonstration

A running User Service pod was manually deleted.

Example:

```bash
kubectl delete pod user-service-xxxxxxxx
```

---

## Kubernetes Response

Immediately after the pod deletion:

- Deployment detected the missing replica
- ReplicaSet created a replacement pod
- Kubernetes scheduled the new pod
- Service availability remained intact

---

## Verification

Pods were monitored using:

```bash
kubectl get pods -w
```

Observed lifecycle:

```
Running

↓

Terminating

↓

Pending

↓

ContainerCreating

↓

Running
```

This demonstrates Kubernetes' ability to automatically recover failed workloads without manual intervention.

---

## Self-Healing Benefits

The implementation validates several production-grade Kubernetes capabilities:

- Automatic Pod Recovery
- Replica Management
- High Availability
- Fault Tolerance
- Service Continuity
- Zero Manual Recovery

---

## Operational Workflow

```
Application Running

        │

Delete Pod

        │

        ▼

Deployment Detects Failure

        │

        ▼

ReplicaSet Creates New Pod

        │

        ▼

Scheduler Assigns Node

        │

        ▼

Container Starts

        │

        ▼

Application Running Again
```

---

## Production Readiness Highlights

This platform incorporates several production-inspired engineering practices:

- Independent Microservices
- Stateless Application Design
- Containerized Deployment
- Kubernetes Orchestration
- Declarative Infrastructure
- Configuration Externalization
- Secret Management
- Internal Service Discovery
- Health Monitoring
- Real-Time Observability
- Self-Healing Workloads
- Multi-Replica Deployments
- Centralized Ingress Routing

These capabilities collectively provide a strong foundation for cloud-native application deployment and are designed to be extended with CI/CD automation, GitOps workflows, and cloud infrastructure provisioning.
# 🏗️ Project Architecture

The Self-Healing GitOps Platform follows a cloud-native microservices architecture built with Kubernetes, GitOps, monitoring, and automated self-healing.

## Architecture Diagram

<img width="1536" height="1024" alt="00-architecture-diagram" src="https://github.com/user-attachments/assets/2b60624e-fa99-47fa-9447-4c48d8fec25a" />


### Architecture Highlights

- 🌐 NGINX Ingress routes external traffic to microservices.
- 👤 User Service manages user-related APIs.
- 📦 Product Service manages product-related APIs.
- 🐘 PostgreSQL provides persistent database storage.
- ☸️ Kubernetes orchestrates and manages containers.
- 📊 Prometheus collects application and cluster metrics.
- 📈 Grafana visualizes metrics with real-time dashboards.
- 🚨 Alertmanager handles alert routing and notifications.
- 🔄 GitHub + GitOps continuously synchronize Kubernetes manifests.
- ♻️ Kubernetes automatically recreates failed pods for self-healing.
