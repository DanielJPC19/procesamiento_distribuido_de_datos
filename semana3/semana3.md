Las tres funciones son map, reduce y shuffle. El map se encarga de asignar un par de clave valor para cada dato. El shuffle se encarga de agrupar conjuntos. El reduce se encarga de condensar la información final en el nodo Master.

**¿Por qué MapReduce?**

*Desafios*

1. Grandes Volúmenes de Datos
2. Complejidad Distribuida
3. Fallos Frecuentes

*La Solución MapReduce*

1. Abstración Total --> Solo define que hacer, ingnorando la complejidad de la red.
2. Tolerancia a Fallos
3. Escalabilidad Lineal --> Escalabilidad Horizontal, las funciones Map-Reduce tienen que ser `determinística`

---

**Función Map**

Map(x1, v1) -> list(x2, v2)

Contamos con varias características, como por ejemplo:

1. Paralelismo puro
2. Sin estado compartido

**Función Shuffle & Sort + Reduce**

El shuffle lo que realiza es agrupar los datos por clave y los redistribuye a través de la red.

---

Microservicios para MapReduce

---> Vamos a generar un servicio

La idea es tener una API Rest que sea capaz de realizar el Map, reduce y shuffle para cualquier conjunto de entrada.