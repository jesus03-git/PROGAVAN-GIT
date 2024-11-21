# **Práctica 5**

**Pregunta 1: ¿Qué es una función lambda?**<br>
->La función lambda es una función anónima, una función que no tiene un nombre asociado. Se utiliza principalmente para operaciones pequeñas y de una sola línea.<br><br>
**Pregunta 2: ¿Qué son los decoradores?**<br>
->Los decoradores son una forma de modificar o extender el comportamiento de funciones o métodos sin tener que cambiar su código directamente.<br><br>
**Pregunta 3: ¿Por qué se utiliza un setter para el atributo prestado?**<br>
->El setter permite controlar cómo se asigna el valor a ese atributo, y su implementación en el código de la clase Book permite modificar el estado del libro entre "prestado" y "disponible".<br><br>
**Pregunta 4: ¿Qué hace el decorador @property en la clase book?**<br>
->En la clase Book, el decorador @property se utiliza para definir propiedades para los atributos titulo, autor, isbn y prestado.<br><br>
**Pregunta 5: ¿Por qué enla clase User, el atributo nombre tiene un setter y un getter, pero el atributo user_id solo tiene un getter?**<br>
->Porque el nombre es un valor que podría cambiar en el transcurso del uso de la clase, mientras que el user_id es un identificador único que no debería modificarse una vez asignado.<br><br>
**Pregunta 6: ¿Por qué el método añadir verifica si el objeto es una instancia de la clase Book antes de agregarlo a la lista books?**<br>
->El método añadir verifica si el objeto pasado como parámetro es una instancia de la clase Book antes de agregarlo a la lista books.<br><br>
**Pregunta 7: ¿Para qué se utiliza UUID?**<br>
->se utiliza para crear identificadores que sean prácticamente únicos y no dependan de ninguna otra fuente de información.
