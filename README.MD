# Haz clic en enlaces de una web de forma automática

Este pequeño script permite mediante Python3, Selenium y Gecko Driver hacer clic en los enlaces que aparecen en la URL que se le indica al script (en la variable url). Bien es cierto que este script se creó para una función muy determinada, que fue la de interactuar de forma automática y autónoma casi por completo con los enlaces que aparecían en el temario que había en un curso que realice de forma telemática, y que utilizaba como plataforma Moodle. Con este script pude hacer que el conteo de horas de mi usuario siguiese aumentando, sin necesidad de tener que estar delante del ordenador moviendo el temario para que el conteo de horas aumentase y así cumplir con la cuota de horas mínima por módulo.

El script cuenta con un tiempo mímo y tiempo máximo (todos en segundos), para que el tiempo que transcurre entre clics no sea siempre el mismo, y poder darle un aspecto de navegación más natural a la hora de ver las estadísticas de navegación en la plataforma. A medida que el script se vaya ejecutando, en la terminal nos irá avisando del tiempo de espera que queda para el siguiente clic en el siguiente enlace.

Cuando se ejecute, se abrirá una ventana de Firefox, en la que se irá mostrando el movimiento por la web indicada. Como decía, esto se hizo para un proposito en particular, por eso en el script aparece un concepto que es "Salta al contenido principal" que no se toma como enlace, para así evitar salir del temario cuando se hace clic en este enlace en particular.

También decir que el script está pensado para ser ejecutado con Firefox, con Chrome sería un poco diferente.

Esto es algo muy básico, se pueden pulir muchas cosas para hacer más efectivo el código, pero para marcar 800 horas de navegación en las estadísticas, a mi me ha servido. Quien quiera tomar el código y modificarlo a su gusto, que no se corte.

## Actualizaciones

- Se ha añadido soporte para que el usuario inserte la URL a visitar, para indicar el tiempo máximo y el tiempo mínimo de espera entre salto al siguiente enlace, desde una ventana.
- Se ha establecido que la URL debe tener el formato indicado.
- También se han añadido controles para que el tiempo máximo y mínimos sean números enteros. Además el tiempo máximo debe ser mayor que el tiempo mínimo.
- Se establece una comprobación para que no se haga clic en un enlace que lleve fuera del dominio indicado por el usuario.

## Dependencias

Las dependencias necesarias para este script son:

- tkinter: Biblioteca para crear interfaces gráficas de usuario.
- re: Módulo de expresiones regulares para validar la URL.
- time: Módulo para trabajar con el tiempo.
- random: Módulo para generar números aleatorios.
- selenium: Biblioteca para automatizar navegadores web.
- webdriver: Clase para crear una instancia del navegador.
- By: Clase para seleccionar elementos por su tipo, id, nombre, etc.
- WebDriverWait: Clase para esperar hasta que se cumpla una condición.
- expected_conditions: Clase para definir condiciones esperadas.
- ElementNotInteractableException: Excepción para indicar que un elemento no es interactuable.
- StaleElementReferenceException: Excepción para indicar que un elemento ya no está presente en el DOM.
- ElementClickInterceptedException: Excepción para indicar que otro elemento está interceptando el clic.
- NoSuchWindowException: Excepción para indicar que la ventana del navegador ha sido cerrada.
- Keys: Clase para simular pulsaciones de teclas.

Es necesario tener todas estas dependencias instaladas para ejecutar el script correctamente. Puedes instalar las dependencias faltantes utilizando pip:
```
pip install selenium
```

Además, debes asegurarte de tener instalado un navegador compatible (por ejemplo, Firefox) y su controlador WebDriver correspondiente. En este caso, se está utilizando Firefox, por lo que necesitarías tener GeckoDriver instalado y configurado en tu sistema. Puedes descargar GeckoDriver desde el sitio web oficial de Selenium: https://github.com/mozilla/geckodriver

## Iniciar el script

Como este script se ha desarrollado utilizando Python3, tras tener instaladas en nuestro equipo todas las dependencias necesarias, iniciarlo es tan sencillo como escribir en la terminal:
```
python3 index.py
```
Este comando se lanza desde la misma carpeta en la que tengamos guardado el script.