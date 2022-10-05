# Tarea 00:school_satchel:


## Consideraciones generales :octocat:

-Hay un menu de inicio en donde se puede elegir entre crear partida, cargar partida, ver ranking y salir. 
Si no se elige ninguna de estas opciones se reconocera esto y aparecera el menu denuevo, pero si se ingresa
cualquier opcion en este nuevo menu el programa se cerrara.

-La opcion cargar partida no esta disponible y simplemente se saldra del juego. Tampoco se guarda la partida,
lo unico que se almacena es el puntaje.

-La opcion ver ranking esta implementada, pero se debera tener un minimo de 10 puntajes para poder utilizarla,
osino dara un error.

-En la consola si se pierde el juego se cerrara, pero en PyCharm si se pierde se muestran todas las posiciones 
de los legos con una L como dice en el enunciado.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* 2. Flujo de juego: Implementado, pero no funciona al 100 % en la consola
* 3. Menus:
    * 3.1 Menu de inicio: Implementado a esepcion de cargar partida
    * 3.2 Menu de juego: Implementado, pero solo se puede salir del juego en el menu de inicio
* 5. Partida:
    * 5.1 Crear: Implementado
    * 5.2 Guardar: No implementado
    * 5.3 Cargar: No implementado
* 6. Puntajes: Implementado, pero se requiere de al menos 10 puntajes para visualizar el ranking.
* 8. Bonus: No implementado


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:


1. ```parametros```-> ```PROB_LEGO``` ```POND_PUNT``` (debe instalarse)
2. ```tablero```-> ```print_tablero_sin_utf8()``` (debe instalarse)
3. ```random```-> ```randint()``` (debe instalarse)

...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```celda```-> ```Clase: Celda()```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Habran mas de 10 puntajes antes de pedir el ranking, porque el juego es muy adictivo y no pararan de jugar :)
2. Solo se querran salir en el menu de inicio, ya que nadie podria parar de jugar esta maravilla si ya empezo.
3. Se recomienda jugar en PyCharm
...

### Referencia de codigo externo

* Se utilizo una playlist de videos de youtube para sacar referencias de como poder hacer el juego. Esto se especifica
en el codigo principal.
    *https://www.youtube.com/watch?v=5d1CfnYT-KM&list=PLyqJaJwNMikB-nNOcVdSik-KbB5EWgjI9





Para realizar mi tarea saqué código de:
1. (link de código): este hace X cosa y está implementado en el archivo (nombre.py) en las líneas (número de líneas) y hace (explicación breve de que hace)



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
