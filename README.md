# GhostDoc

GhostDoc is a lightweight, stateless Retrieval-Augmented Generation (RAG) system designed for instant PDF interaction.

It processes documents entirely on-the-fly with zero persistent storage, providing high privacy, low infrastructure overhead, and rapid insights from uploaded files.

---

# Tech Stack

- Docker
- Docker Compose
- Vector Retrieval
- Large Language Models (LLMs)
- PDF Parsing Pipeline

---

# Prerequisites

Before running GhostDoc, install:

- Docker
- Docker Compose

Official resources:

- Docker: https://www.docker.com/
- Docker Compose: https://docs.docker.com/compose/

---

# Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/your-username/ghostdoc.git

cd ghostdoc
```

---

## 2. Create Docker Network

```bash
docker network create ghostdoc
```

> Skip this step if the network already exists.

---

## 3. Start Services

```bash
docker compose up -d
```

---

## 4. Verify Containers

```bash
docker ps
```

---

# Docker Commands

## Start Application

```bash
docker compose up -d
```
