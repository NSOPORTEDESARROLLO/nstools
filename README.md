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