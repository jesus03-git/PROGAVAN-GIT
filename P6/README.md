# **Práctica 6**

**Pregunta 1: ¿Cómo podría usar "crear_menu" para manejar el menú del primer código?**<br>
->Se podría reemplazar la lógica manual del menú en el primer código con "crear_menu".<br><br>
**Pregunta 2: ¿Qué función usaría para leer las horas, minutos y segundos en el menú?**<br>
->Usaría la función leer_int para asegurarme de que las horas, minutos y segundos sean números enteros válidos introducidos por el usuario.<br><br>
**Pregunta 3: ¿Cómo podría asociar un identificador único a cada hora creada en el primer código?**<br>
->Al crear una nueva instancia de "Time", se puede generar un identificador único con "generar_id_unico" y guardarlo en un diccionario donde las claves sean los identificadores y los valores las instancias de "Time".<br><br>
**Pregunta 4: ¿Cómo puedo integrar la función "leer_cadena" para pedir el formato de hora al usuario?**<br>
->Usaría "leer_cadena" para pedir el formato de hora al usuario y asegurarme de que la entrada no esté vacía, luego validar el formato usando el método "is_valid_format" de la clase "Time".<br><br>
**Pregunta 5: ¿Cómo podría guardar un historial de horas creadas junto con sus identificadores únicos?**<br>
->Se podría usar un diccionario donde las claves sean los identificadores únicos generados con "generar_id_unico" y los valores sean las instancias de "Time", esto permite buscar y listar fácilmente las horas creadas.<br><br>
**Pregunta 6: ¿Cómo usaría "crear_menu" para mostrar un menú dinámico basado en las opciones disponibles?**<br>
->Se podría pasar una lista de opciones generadas dinámicamente a crear_menu.<br><br>
**Pregunta 7: ¿Cómo podría buscar una hora específica en el historial usando su identificador único?**<br>
->Podría pedir al usuario que introduzca el identificador único usando "leer_cadena" y luego buscar en el diccionario de horas registradas. Si el identificador existe, mostrar la hora asociada; si no, informar al usuario que no se encontró.<br><br>
