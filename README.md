# NSTOOLS 

NSTOOLS permite administrar la NSPBX mediante CLI de manera facil, incluye muchas herramientas para tareas administrativas y de depuracion.


# Instalar/Actualizar

Se asume que python3 esta instalado en /usr/bin/python3, se recomienda probar antes el path:

```
/usr/bin/python3 --version
```
Si no genera error se puede continuar con la instalacion 


```
yum install gcc python3-devel
pip3 install psutil
wget https://github.com/NSOPORTEDESARROLLO/nstools/raw/main/nstools.py -O /usr/sbin/nstools && chmod +x /usr/sbin/nstools

```

# Funcionalidades

- Reciclado de grabaciones
- Borrado de grabaciones 
- Limpieza de logs
- Reporte de sistema
