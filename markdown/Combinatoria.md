
# Permutación y el factorial

Una **permutación** se trata de calcular las maneras posibles de ordenar elementos.

De cuantas maneras posibles puedo ordenar estos 5 emojis? : {👽 ,👾,💥,💠,🧶}

Si tengo que elegir un primer elemento para ordenar, tengo 5 opciones. Supongamos que elijo 🧶.


Entonces el 🧶 queda descartado. Para el siguiente elemento tengo 4 opciones {👽 ,👾,💥,💠}



Si elijo el 👾,  me quedaría 🧶, 👾, _ , _ , _. Es decir, 3 posibilidades para el siguiente elemento, luego para el próximo 2 y por ultimo 1.

**Para contar posibilidades, tengo que multiplicarlas todas**

$$
5 \times 4 \times 3 \times 2 \times 1 = 5!
$$

Y si no hace falta que elija todos los elementos?

 Supongamos que quiero ver cuantas formas de ordenar 3 emojis de los 5 que tenia.

El razonamiento seria parecido. En el primer caso tendría 5 posibilidades (como antes), en el segundo caso 4 posibilidades y en el tercer caso 3 posibilidades. Como solo necesito 3 terminaría ahí. La cuenta me quedaría.

$$
5\times4\times3
$$


# El numero combinatorio

En combinatoria todo se suele expresar con factoriales, entonces, Como podría expresar el resultado anterior como un factorial? Si para eso me faltan el 2 y el 1.

La respuesta es dividiendo.

$$
5 \times 4\times3  = \frac{5 \times 4 \times 3 \times 2 \times1}{2 \times 1} =  \frac{5!}{2!}
$$

Esto de querer ver  cuantos conjuntos de **n** elementos puedo formar con un conjunto de **k** elementos tiene una formula: El **numero combinatorio**.

$$
\boxed {\dbinom{n}{k} = \frac {n!} {k! \cdot (n - k)!}}
$$

Sólo tiene sentido la expresión si $0≤k≤n, n \in \mathbb{N}_0$

# Los anagramas

Un anagrama es una palabra o frase formada mediante la reordenación de las letras de otra palabra o frase. En otras palabras, se trata de un juego de palabras en el que se mezclan las letras de una palabra o frase para formar una nueva palabra o frase con las mismas letras pero en un orden diferente. Por ejemplo, la palabra "amor" es un anagrama de la palabra "roma". En esta materia se juega mucho a **calcular todos los posibles anagramas** de una palabra (a pesar de que estas palabras tengan o no sentido). 

Calcular la cantidad de anagramas posibles es equivalente a hacer una **permutación** cuando tiene letras que no se repiten, por ej:

GATO = 4!

Ahora, si quiero calcular los anagramas de la palabra “ananá” tengo el problema de que la **a** se repite 3 veces y la **n** 2. Lo que hago es dividir el numero de letras totales entre cada factorial de las letras que se repiten, con ananá quedaría $\frac{5!}{2! 3!}$.

El 5! de arriba porque ananá tiene 5 letras. El 2! porque la n se repite 2 veces y el 3 porque la a se repite 3.

Vamos a ver que pensar ciertos ejercicios como si fuesen anagramas es muy útil para resolver ejercicios de combinatoria.
