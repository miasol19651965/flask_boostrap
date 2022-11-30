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
Luego de clonar el repositorio y para instalar las dependencias debe ejecutar 'pipenv install'

## Migraciones
Para ejecutar las migraciones el comando siguiente:
´´´
flask db upgrade
´´´
Para ejecutar hacia atras
```
flask db downgrade

Cuando hacemos algun cambio en un modelo y necesitamos considerar esos cambios tambien en la base de datos hay que generar una nueva migracion.

```
flask db migrate -m"mensaje de la migracion"
```

En caso de modificar un Modelo agregando o modificando un atributo debemos generar una nueva migracion, con el comando:
```
flask db migrate -m"mensaje de la migracion"
```
**Nota**:Los comandos anteriores se deben ejecutar dentro de 'pipenv shell'.

## Blueprint

Los blueprint permiten componer aplicaciones desde componentes pequeños. Cada componentees como una mini aplicacion. Permiten crear aplicaciones grandes, pero manteniendo el codigo y la estrcturas simples.

## Modulos

Para que los blueprint esten bien organizados, es mejor trabajarlos como modulos, es decir, que esten dentro de una carpeta. Los modulos se pueden anidar nosotros hicimos el modulo 'app' con su respectivos_init_.py y dentro tenemos otros modulos como el modulo 'messages' que es ademas un blueprint

En caso de modificar un modelo agregando o modificando un atributo, debemos generar una nueva migracion con el comando.
'''
flask db migrate -m"mensaje de la migracion"
'''
**nota**: Los comandos anteriores se deben ejecutar dentro de la 'pipenv shell'

## Levantando la aplicacion

Para ejecutar el servidor de desarrollo el comando es el siguiente.
flask --app app --debug run

## Tarea
Crear un nuevo recurso sencillo, sin base de datos, como blueprint bajo url '/memes' y debe renderiar un html lleno de memes.

