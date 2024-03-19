## Haz clic en enlaces de una web de forma automática

Este pequeño script permite mediante Python3, Selenium y Gecko Driver hacer clic en los enlaces que aparecen en la URL que se le indica al script (en la variable url). 
Bien es cierto que este script se creó para una función muy determinada, que fue la de interactuar de forma automática y autónoma casi por completo con los enlaces que aparecían en el temario que había en 
un curso que realice de forma telemática, y que utilizaba como plataforma Moodle. Con este script pude hacer que el conteo de horas de mi usuario siguiese aumentando, sin necesidad de tener que estar delante 
del ordenador moviendo el temario para que el conteo de horas aumentase y así cumplir con la cuota de horas mínima por módulo.

El script cuenta con un tiempo mímo y tiempo máximo (todos en segundos), para que el tiempo que transcurre entre clics no sea siempre el mismo, y poder darle un aspecto de navegación más natural a la hora de ver las estadísticas de 
navegación en la plataforma. A medida que el script se vaya ejecutando, en la terminal nos irá avisando del tiempo de espera que queda para el siguiente clic en el siguiente enlace.

Cuando se ejecute, se abrirá una ventana de Firefox, en la que se irá mostrando el movimiento por la web indicada. Como decía, esto se hizo para un proposito en particular, por eso en el script aparece un concepto que es 
"Salta al contenido principal" que no se toma como enlace, para así evitar salir del temario cuando se hace clic en este enlace en particular.

También decir que el script está pensado para ser ejecutado con Firefox, con Chrome sería un poco diferente.

Esto es algo muy básico, se pueden pulir muchas cosas para hacer más efectivo el código, pero para marcar 800 horas de navegación en las estadísticas, a mi me ha servido. Quien quiera tomar el código y modificarlo a su gusto, que no se corte.


