# **Práctica 7-8**

**Pregunta 1: ¿Por qué se utiliza `__dict__` al guardar objetos en el fichero JSON?**<br>
->Porque `__dict__` permite acceder a todos los atributos internos del objeto en forma de diccionario, lo cual es necesario para serializar la información de cada publicación con `json.dump`.<br><br>

**Pregunta 2: ¿Cómo se implementa el polimorfismo en esta práctica y qué ventajas aporta?**<br>
->Se implementa sobrescribiendo el método `descripcion()` en `Libro` y `Revista`. Esto permite llamar a `descripcion()` sin preocuparse por el tipo exacto del objeto, haciendo el código más limpio y extensible.<br><br>

**Pregunta 3: ¿Qué problema se evita al incluir el atributo `tipo` al guardar cada objeto en el JSON?**<br>
->Permite reconstruir correctamente el tipo de objeto (`Libro` o `Revista`) al cargar el fichero, ya que JSON no guarda la información de clases por defecto.<br><br>

**Pregunta 4: ¿Por qué se realiza la validación de datos directamente en los constructores de las clases?**<br>
->Para asegurar que cada instancia se cree con datos válidos desde el principio. Esto previene errores posteriores y mantiene la integridad de los objetos.<br><br>

**Pregunta 5: ¿Qué ventaja tiene encapsular los atributos con `_` y acceder a ellos mediante `@property`?**<br>
->Permite proteger los atributos del acceso directo y facilita añadir lógica extra si se desea validar o transformar el valor en el futuro, sin cambiar cómo se accede externamente.<br><br>

**Pregunta 6: ¿Qué riesgos se controlan mediante las excepciones personalizadas en el sistema?**<br>
->Se controlan errores como archivos no encontrados, problemas al leer o escribir ficheros, y se ofrece al usuario un mensaje claro y específico según el tipo de error que ocurra.<br><br>

**Pregunta 7: ¿Por qué se importa `Libro` y `Revista` dentro de la función `cargar_publicaciones` en lugar de hacerlo arriba del archivo?**<br>
->Para evitar dependencias circulares entre módulos, ya que `utils.py` también es importado por `main.py`. La importación local mantiene la independencia y modularidad del código.<br><br>
