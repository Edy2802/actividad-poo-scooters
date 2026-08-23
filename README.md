# Actividad - POO - Scooters


## Instanciación

### Scooter 1
- id = "S-001"
- nivelBateria = 79
- estaDisponible = true

### Usuario 1
- nombre = "Esmeralda"
- saldo = 150.00

## Pregunta de Análisis Lógico
### Si la Instancia de Usuario 1 intenta ejecutar el método rentar() enviando como parámetro un Scooter que tiene un 15% de batería, ¿cómo debería comportarse internamente la lógica del sistema?

Esto depende de muchos factores, principalmente, para que el usuario pueda ejecutar correctamente el método rentar(), requiere que el scooter señale "true" en el booleano de su atributo. 
Dejando esto de lado, debido a que el codigo no esta completo, aun faltaria algo importante: considerar si la instancia Scooter tiene un metodo de "minimoRequerido", es decir, 
que se haya establecido un minimo de bateria necesaria para que la instancia pueda ser utilizada. Por ello, hay dos caminos que puede tomar el sistema:

- Si el Scooter cuenta con el método "minimoRequerido" y este se establece en un 20%, por ejemplo, el sistema cambiaría automáticamente el bool de "estaDisponible" a "false", debido a que la instancia no cumple este método.
- Si la instancia no cuenta con el metodo ya mencionado, entonces su atributo "estaDisponible" permaneceria en "true". Pero este seria perjudicial para el usuario, ya que si el Scooter llegara a quedarse sin bateria, podria ocasionar la mala experiencia del Usuario.

Por ello, desde mi punto de vista, directamente la entidad "Scooter" deberia tener el metodo "minimoRequerido" para que asi todas las instancias que surgan a partir de este, cuenten con el mismo metodo.

## Uso de la IA en esta actividad

Para finalizar, me gustaría aclarar el uso que le di a la inteligencia artificial:
Principalmente utilice la IA para hallar otras perspectivas, y generar explicaciones. ¿A qué me refiero? Al momento de analizar la lógica, yo ya llevaba una idea de cómo debía funcionar el sistema ante esas circunstancias. Lo que hice con la IA fue reafirmar mi teoría, buscando algo más que se me hubiera escapado de la mente. Por otra parte, debo aclarar que al inicio del ejercicio, me resultó algo complicado entender hacia dónde apuntaba toda la actividad, o sea, qué debíamos realizar y conseguir dentro de la misma. Es por ello que utilicé la IA para que me explicara el ejercicio completo con otras palabras. Aparte de lo mencionado, no necesité usar la IA para nada más; la redacción de este README fue realizada completamente por mí y un asistente de ortografía, ya que a veces suelo descuidar un poco mi escritura.
