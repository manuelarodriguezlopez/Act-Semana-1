  A. Numpy arreglos

    Como primer paso veremos que son los arreglos y como se pueden aplicar, de esta forma entenderemos para que son y explicaremos de que forma estos se pueden utilizar en difernetes contextos.

    Los arreglos basicamente son una estructura por la que obtendremos formas diversas en las que podremos almacenar datos del mismo tipo, vale la pena mencionar que estas colecciones de datos son sumamente eficientes tanto en su creacion como en su almacenamiento.

    existen dos tipos, vectores y matrices.
    Cada uno de ellos tiene ciertas cualidades y  caracteristicas; por ejemplo los vectores son tecnicamente matrices, sinembargo tienen 1D, asi que se podria decir que son pseudo matrices que pueden ser creadas de manera vertical u horizontal según se desee, las matrices como tal tienen 2D, ahi radica su principal diferencia.
    
    Para empezar vamos a hablar de lo mas básico de la libreria numpy, lo cual es el modo en el que se va a importar la propia libreria, es sumamente sencillo, haremos uso de una simple linea de codigo
    
    * import numpy as np
    Esta simple lina de codigo importa una gran herramienta, nos ahorrará algunos si no muchos dolores de cabeza. en caso que quieras conocer la versión de numpy, debemos usar otra simple linea de codigo.
    * np.__version__

    EJEMPLO 1°
![Importe](./imagenes/Importe%20de%20Numpy.png)
    en este caso podemos ver que la version que fue importada es la 2.0.2

  los arreglos pueden ser creados a partir de la conversion de una lista o una lista que contenga listas, por ejemplo
  * my_list = [1, 2, 3]
  * my_list
![Listas](/imagenes/Ejemplo%20de%20listas.png)

  mediante el metodo array es posible convertir una lista a un arreglo, con este metodo, podemos tambien asignar el arreglo a un tipo de dato, por otro lado el comando "a.dtipe" nos permite conocer el tipo de datos que tiene el arreglo, ademas podemos mostrar que efectivamente el dato del arreglo "a" fue guardado

  * a = np.array(my_list)
  * type(a)
  * a.dtype 
  * print(a)

![Tipo](/imagenes/Tipo%20de%20dato%20e%20impresion.png)

* reshape
  En NumPy, este metodo se utiliza para modificar la estructura dimensional de un arreglo sin cambiar el contenido de sus datos. Matemáticamente, un arreglo puede considerarse como un tensor con cierta cantidad de dimensiones y elementos. La operación de reshape consiste en reconfigurar la distribución de esos elementos en un nuevo espacio de dimensiones, manteniendo constante el número total de elementos.

![Reshape](/imagenes/Ejemplo%20n2.png)

  * concatenar
    En NumPy, la concatenación se entiende como el proceso de unir dos o más arreglos en uno solo, conservando su estructura pero ampliando su tamaño en alguna de sus dimensiones. Existen principalmente dos formas de realizar esta unión: a lo largo de las filas o a lo largo de las columnas.

    Cuando se concatena en el eje de las filas, lo que ocurre es que los arreglos se apilan uno debajo del otro, generando así un mayor número de filas pero manteniendo el mismo número de columnas. En cambio, cuando la concatenación se hace sobre el eje de las columnas, los arreglos se disponen uno al lado del otro, aumentando el número de columnas pero conservando el número de filas.

    Un aspecto importante es que, para que la concatenación sea posible, los arreglos deben coincidir en todas las dimensiones excepto en aquella en la que se está uniendo. De esta forma, NumPy asegura la coherencia en la estructura del nuevo arreglo creado.

![Concatenar](/imagenes/EJemlpo%20de%20concatenar.png)

  * operaciones basicas
    En NumPy, las operaciones básicas se refieren a aquellas que pueden aplicarse directamente sobre los arreglos, de forma similar a como se trabaja con números o con expresiones matemáticas. La gran diferencia es que estas operaciones se realizan de manera elemento por elemento, lo que significa que cada posición del arreglo es afectada de forma independiente, pero en paralelo.

    Por ejemplo, cuando se suman dos arreglos del mismo tamaño, lo que ocurre es que cada elemento del primero se combina con el elemento en la misma posición del segundo. Lo mismo sucede con la resta, la multiplicación y la división. Esta capacidad convierte a NumPy en una herramienta muy eficiente, ya que evita el uso de ciclos tradicionales y permite cálculos vectorizados, propios de un tratamiento más matemático y cercano al álgebra lineal.

    Además de estas operaciones aritméticas básicas, NumPy también incorpora funciones matemáticas elementales como la potencia, la raíz cuadrada, el logaritmo o las funciones trigonométricas, las cuales pueden aplicarse directamente sobre los arreglos y devuelven resultados con la misma forma dimensional.
    
![OperacionesBasicas](/imagenes/Codigo.png)
![OperacionesBasicas](/imagenes/ejecucion.png)


_______________________________________________________________________________________________________

PANDAS Y SUS OPERAACIONES AVANZADAS
¿QUE ES PANDAS?

 Pandas es una librería de Python muy poderosa para el análisis y manipulación de datos.
 Permite trabajar con DataFrames (tablas de datos con filas y columnas) de forma sencilla, similar a Excel o SQL, pero con la potencia de Python.

 Con Pandas puedes:

 -Limpiar datos (quitar nulos, duplicados, etc.).

 -Transformar y organizar información.

 -Hacer análisis estadístico.

 -Exportar e importar a distintos formatos (CSV, Excel, SQL, JSON).

  *Filtros (Filtering)

Qué es: Seleccionar filas o columnas que cumplen una condición.

Uso: Permite trabajar solo con los datos relevantes.

![alt text](/imagenes/image-1.png)

  *GroupBy

Qué es: Agrupar datos según una o varias columnas y aplicar funciones de agregación.

Uso: Sirve para análisis estadístico, como totales, promedios, conteos.

![alt text](/imagenes/image-2.png)

   *Merge / Join

Qué es: Combinar dos DataFrames según columnas en común (similar a JOIN en SQL).

Uso: Integrar información de distintas tablas en una sola.

![alt text](/imagenes/image-3.pngx)




