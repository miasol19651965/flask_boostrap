# Documentacion
Este una aplicacion web  utizando Framewor y bootstrap.Su proposito es ejemplarizar un CRLD
Los datos se guardan en la base de datos postgres utilizando el recurso

Las dependencias se gestiona con pipenv.

# Dependencias
Para correr proyecto ud necesita tener instalado python 3 y sus herramientas pip
Para revisar si las tiene instalados debe ejecutar los siguientes comandos
'''

python -v
pip -v
'''

El resultado debe indicar un numero superios a 3
Luego de clonar el repositorio y para instalar las dependencias debe ejecutar 'pipen install'

## Migraciones
Para ejecutar las migraciones el comando siguiente:
'''
flask db upgrade
'''

En caso de modificar un modelo agregando o modificando un atributo, debemos generar una nueva migracion con el comando.
'''
flask db migrate -m"mensaje de la migracion"
'''
**nota**: Los comandos anteriores se deben ejecutar dentro de la 'pipenv shell'

## Levantando la aplicacion

Para ejecutar el servidor de desarrollo el comando es el siguiente.
