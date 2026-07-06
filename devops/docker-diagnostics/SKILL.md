---
name: docker-diagnostics
description: Diagnose Docker and Docker Compose container status, inspect logs, resource consumption, and build issues.
description_fr: Diagnostiquer l'état des conteneurs Docker et Docker Compose, inspecter les journaux, la consommation de ressources et les erreurs de build.
category: devops
triggers: docker, container exited, docker compose, image build, container logs
risk: low
---

# Docker Diagnostics

## 1. Use when

Use this skill when investigating container failures, exited containers, build errors, Docker Compose status, or examining container resource utilization.

## 2. Command templates & Diagnostic steps

### Container status & list
To check running and exited containers:
```bash
docker ps -a
docker compose ps -a
```

### Container Logs
To inspect container stdout/stderr output:
```bash
docker logs --tail 100 <container_id_or_name>
docker compose logs --tail 100 <service_name>
```

### Resource Usage
To check CPU, memory, and network usage per container:
```bash
docker stats --no-stream
docker system df
```

### Inspection & Details
To get configuration details, IP addresses, or state of a container:
```bash
docker inspect <container_id_or_name>
# Find container IP address
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id_or_name>
```

## 3. Stop / block conditions

Do not write new images or deploy new compose files during diagnostic runs. This skill is strictly read-only for troubleshooting and reporting container states.
