# Docker Common Commands

## List Containers

```bash
docker ps
docker ps -a
```

## Access a Container

```bash
docker exec -it <container_name> sh
```

If Bash is available:

```bash
docker exec -it <container_name> bash
```

## View Logs

```bash
docker logs <container_name>
docker logs -f <container_name>
```

## Stop

```bash
docker stop <container_name>
```

## Start

```bash
docker start <container_name>
```

## Restart

```bash
docker restart <container_name>
```

## Remove

```bash
docker rm <container_name>
docker rm -f <container_name>
```

## Remove Image

```bash
docker rmi <image_name>
```

## Inspect

```bash
docker inspect <container_name>
```

## Copy Files

```bash
docker cp file.txt container:/path
docker cp container:/path/file.txt .
```

## Execute a Command

```bash
docker exec <container_name> ls /app
```

## Check Resource Usage

```bash
docker stats
```

## Networks

```bash
docker network ls
docker network inspect bridge
```

## Volumes

```bash
docker volume ls
docker volume inspect <volume_name>
```