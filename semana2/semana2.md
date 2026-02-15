La paralelización tiende a demorarse más con datos más pequeños de datos, ya que se deben de realizar procesos antes de manejar los conjuntos de datos (tales como dividir y unir el conjunto de datos).

**Arquitecturas Distribuidas**

Sistema compuesto por un conjunto de nodos independientes que cooperan para realizar una tarea común

1. Se comunican por red
2. Coordinan su ejecución
3. Actúan como un solo sistema lógico

*Características - Atributos de Calidad:*

1. Concurrencia
2. Escalabilidad Horizontal
3. Tolerancia a Fallos
4. Ausencia de Reloj Global --> Cada nodo tiene su propio reloj, lo que complica la sincronización de eventos.

*Los problemas de memoria*

1. Memoria compartida (UMA): Todos los componentes computacionales tienen el mismo tiempo de acceso al conjunto de datos en memoria, lo que puede hacer mucho más rápido el intercambio de datos, sin embargo la escalabilidad es limitada, con un cuello de botella (punto único de fallo) y una contención de buses.

2. Memoria no compartida (NORMA) --> Esta trae el limitante de acceso directo a la información, sin embargo mejora la tolerancia a fallos, una comodidad de hardware, y una escalabilidad horizontal ilimitada (presupuesto). Como desventajas contamos con una complejidad en el desarrollo, una latencia de rede y requiere particionamiento de los datos y la unión de estos.

*Data Locality (Localidad de los Datos)*

//--> Principio fundamental: movel el cómputo hacia los datos, no los datos hacia el cómputo

1. Conexión directa (latencia baja): Un nodo de procesamiento
2. Conexión intra-rack (latencia media): Como un data center enfocado solo a datos pero los nodos de procesamiento esten en la misma red local
3. Conexión remota (latencia alta): Se realiza la conexión por medio de red