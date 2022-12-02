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

## MVC (Model-View.Controller)

## Levantar el servidor de desarrollo
con todo esto
```bash
pipenv shell
pipenv install
set FLASK_APP=app
set FLASK_ENV=development
flask run
```
o con la siguiente linea
'pipenv run flask --app app ..debug run'

Y si tiene el archivo .env con las variables FLASK_DEBUG=1 y FLASK_APP=app, solo debe ejecutar lo siguiente

'flask run'

## blueprints

## MVC
(Model-View-Controller)

![MVC](https://cdn.educba.com/academy/wp-content/uploads/2019/04/what-is-mvc-design-pattern.jpg.webp)

Es una arquitectura para separar las responsabilidades en la manipulacion de las solicitudes y respuestas. Quien recibe las solicitudes es el controlador  o en flask, las rutas .
los controladores se encargan de revisar las solicitudes cumpla con las caracteristicas ppara entregar respuestas acorde (que tenga todos los datos) Si el controlador lo permite, se podria opcionalmente llamar al modelo  para obtener o modificar los datos de la BBDO. Y finalmente enviar una respuesta que contenga la presentacion de la aplicacion. En nuestro caso la capa de ppresentacion comunmente conocida como Vistas(views)se llaman Templates.

Por lo tanto en flask el MVC podria ser adaptado como MTR (Modelo, Template,), pero es lo mismo en terminos de separar la responsabilidad.