# Microservices CI/CD Automation using GitHub Actions

> End-to-end DevOps project demonstrating containerization, automated testing, CI/CD, Docker image management, and Kubernetes deployment for a Python-based microservices application.

## 📌 Project Overview

This project implements a containerized microservices application and automates its software delivery process using modern DevOps tools.

The application consists of three independent services:

- **Frontend Service** – Provides the web interface.
- **Backend Service** – Handles backend application functionality.
- **Users Service** – Handles user-related functionality.

The services are containerized using Docker, orchestrated locally using Docker Compose, and deployed to Kubernetes using Kubernetes Deployments and Services.

GitHub Actions is used to automate testing, Docker image building, and publishing images to Docker Hub.

---

## 🏗️ Architecture

```text
                         Developer
                            |
                            | git push
                            v
                  +----------------------+
                  |   GitHub Repository  |
                  +----------+-----------+
                             |
                             v
                  +----------------------+
                  |    GitHub Actions    |
                  +----------+-----------+
                             |
                    +--------+--------+
                    |                 |
                    v                 v
               Run Tests       Build Docker Images
                                      |
                                      v
                              Push to Docker Hub
                                      |
                                      v
                         +----------------------+
                         |      Kubernetes      |
                         +----------+-----------+
                                    |
              +---------------------+---------------------+
              |                     |                     |
              v                     v                     v
       +-------------+       +-------------+       +-------------+
       |   Frontend  |       |   Backend   |       |    Users    |
       |   Service   |       |   Service   |       |   Service   |
       +-------------+       +-------------+       +-------------+
              |                     |                     |
           2 Pods                2 Pods                2 Pods
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python / Flask | Microservices application |
| Git | Version control |
| GitHub | Source code repository |
| GitHub Actions | CI/CD automation |
| Docker | Application containerization |
| Docker Compose | Local multi-container development |
| Docker Hub | Container image registry |
| Kubernetes | Container orchestration |
| YAML | Configuration and Kubernetes manifests |
| WSL2 / Docker Desktop | Local development environment |

---

## 📂 Project Structure

```text
microservices-cicd-github-actions/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── test_app.py
│
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
├── users-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── test_app.py
│
├── kubernetes/
│   ├── namespace.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── users-deployment.yaml
│   ├── users-service.yaml
│   ├── frontend-deployment.yaml
│   └── frontend-service.yaml
│
├── .github/
│   └── workflows/
│       └── cicd.yml
│
├── docker-compose.yaml
└── README.md
```

---

# 🚀 Application Components

## 1. Frontend Service

The frontend provides the user-facing web application.

**Port:**

```text
5002
```

Docker image:

```text
pavangujari/frontend:v1
```

---

## 2. Backend Service

The backend provides application APIs and backend functionality.

**Port:**

```text
5000
```

Docker image:

```text
pavangujari/backend:v1
```

---

## 3. Users Service

The Users Service handles user-related functionality.

**Port:**

```text
5001
```

Docker image:

```text
pavangujari/users-service:v1
```

---

# 🐳 Docker Implementation

Each microservice has its own Dockerfile.

The services can be started together using Docker Compose.

## Start the application

```bash
docker compose up -d --build
```

## Check running containers

```bash
docker compose ps
```

## Stop the application

```bash
docker compose down
```

### Local Ports

| Service | Port |
|---|---:|
| Backend | 5000 |
| Users Service | 5001 |
| Frontend | 5002 |

---

# ☸️ Kubernetes Deployment

The application is deployed to a Kubernetes cluster using:

- Namespace
- Deployments
- Services
- Multiple replicas

Each microservice runs with **2 replicas**.

```text
Kubernetes
│
├── Backend
│   ├── Pod 1
│   └── Pod 2
│
├── Users Service
│   ├── Pod 1
│   └── Pod 2
│
└── Frontend
    ├── Pod 1
    └── Pod 2
```

## Create the namespace

```bash
kubectl apply -f kubernetes/namespace.yaml
```

## Deploy Backend

```bash
kubectl apply -f kubernetes/backend-deployment.yaml
kubectl apply -f kubernetes/backend-service.yaml
```

## Deploy Users Service

```bash
kubectl apply -f kubernetes/users-deployment.yaml
kubectl apply -f kubernetes/users-service.yaml
```

## Deploy Frontend

```bash
kubectl apply -f kubernetes/frontend-deployment.yaml
kubectl apply -f kubernetes/frontend-service.yaml
```

---

# 🔍 Kubernetes Verification

Check all Pods:

```bash
kubectl get pods -n microservices
```

Check Deployments:

```bash
kubectl get deployments -n microservices
```

Check Services:

```bash
kubectl get services -n microservices
```

Check all Kubernetes resources:

```bash
kubectl get all -n microservices
```

Expected architecture:

```text
Backend          → 2 Pods → Running
Users Service    → 2 Pods → Running
Frontend         → 2 Pods → Running
```

---

# 🌐 Accessing the Frontend

The frontend is exposed through a Kubernetes NodePort.

Example:

```text
frontend-service
5002:31623
```

For local testing, port forwarding can be used:

```bash
kubectl port-forward svc/frontend-service 5002:5002 -n microservices
```

Then open:

```text
http://localhost:5002
```

---

# 🔄 CI/CD Pipeline

GitHub Actions automates the Continuous Integration process.

Whenever code is pushed to the `main` branch:

```text
Developer
    |
    | git push
    v
GitHub
    |
    v
GitHub Actions
    |
    +---- Checkout Source Code
    |
    +---- Setup Python
    |
    +---- Install Dependencies
    |
    +---- Run Tests
    |
    +---- Login to Docker Hub
    |
    +---- Build Docker Images
    |
    +---- Push Images to Docker Hub
    |
    v
Docker Hub
```

The workflow is located at:

```text
.github/workflows/cicd.yml
```

---

# 🧪 Automated Testing

The CI pipeline runs automated tests before building and publishing Docker images.

Example:

```bash
pytest backend/test_app.py
```

```bash
pytest users-service/test_app.py
```

The Docker build stage depends on the test stage.

Therefore:

```text
Tests Pass
    ↓
Build Images
    ↓
Push Images
```

If tests fail:

```text
Tests Fail
    ↓
Pipeline Stops
    ↓
Images Are Not Published
```

---

# 📦 Docker Hub Images

The application images are published to Docker Hub.

```text
pavangujari/backend:v1
pavangujari/users-service:v1
pavangujari/frontend:v1
```

The CI pipeline also publishes the latest builds using the `latest` tag.

---

# 🔐 GitHub Actions Secrets

Docker Hub authentication is handled using GitHub repository secrets.

Required secrets:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

Credentials are not stored directly inside the workflow file.

Example:

```yaml
username: ${{ secrets.DOCKERHUB_USERNAME }}
password: ${{ secrets.DOCKERHUB_TOKEN }}
```

---

# 📈 DevOps Concepts Demonstrated

This project demonstrates practical experience with:

- Microservices architecture
- Containerization
- Docker image creation
- Docker Compose
- Container registry management
- Git version control
- GitHub repository management
- GitHub Actions
- Continuous Integration
- Automated testing
- Docker image build automation
- Docker Hub image publishing
- Kubernetes Deployments
- Kubernetes Services
- Kubernetes Namespaces
- Kubernetes replica management
- Service discovery
- Rolling deployment concepts
- Infrastructure configuration using YAML

---

# 🎯 Project Goals

The primary goals of this project are to:

1. Containerize independent microservices.
2. Run multiple services using Docker Compose.
3. Publish container images to Docker Hub.
4. Deploy microservices to Kubernetes.
5. Run multiple replicas for each service.
6. Automate testing using GitHub Actions.
7. Automate Docker image building and publishing.
8. Establish a foundation for continuous deployment.

---

# 🔮 Future Enhancements

The project can be extended with:

- Kubernetes-based automated deployment from GitHub Actions
- Kubernetes Ingress
- HTTPS/TLS
- Prometheus monitoring
- Grafana dashboards
- Kubernetes Horizontal Pod Autoscaler
- SonarQube code-quality analysis
- Trivy container vulnerability scanning
- AWS EKS deployment
- Environment-specific deployments
- Rolling updates and rollback automation

---

# 👨‍💻 Author

**Pavan Gujari**

DevOps / Cloud Engineering Project

---