# NSTOOLS 

NSTOOLS permite administrar la NSPBX mediante CLI de manera facil, incluye muchas herramientas para tareas administrativas y de depuracion.


# Variables de Entorno:
- SSHPORT: Puerto ssh, si no se especifica usara el 22

# Docker RUN
```
docker run --name=nstools --net=host -e SSHPORT=2222 \
        --restart=always \
		-v /etc/localtime:/etc/localtime:ro \
		-v /:/host \
		-v /var/run/docker.sock:/var/run/docker.sock
		-d nsoporte/nstools:tag 

```

# Docker Compose

```
version: '3'

services:
 nstools:
  container_name: 'nstools'
  image: 'nsoporte/nstools'
  restart: 'always'
  network_mode: 'host'
  environment:
   - 'SSHPORT=2222'
  volumes:
   - '/etc/localtime:/etc/localtime:ro'
   - '/:/host'
   - '/var/run/docker.sock:/var/run/docker.sock' 
   - '/opt/nstools:/opt/nstools'


```