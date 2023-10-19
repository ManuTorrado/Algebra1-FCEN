# Número combinatório

$\binom{n}{k}$ es la cantidad de subconjuntos de $k$ elementos que tiene un conjunto con $n$ elementos.

Sólo tiene sentido la expresión si $0≤k≤n$, $n \in \mathbb{N}_0$.


💡 Contar la cantidad de subconjuntos de $k$ elementos en un conjunto de $n$ elementos es lo mismo que contar las formas distintas que tengo de elegir $k$ elementos en un conjunto de elementos (sin orden).

**Propiedades**

Sean $0≤k≤n$ con $n \in \mathbb{N}_0$

- $\dbinom{n}{0} = 1 \implies \dbinom{0}{0} = 1$
- $\dbinom{n}{1} = n = \dbinom{n}{-1}$
- $\dbinom{n}{k} = \dbinom{n}{n-k}$
- La cantidad total de subconjuntos que tiene un conjunto con $n$ elementos es #$p(A) = 2^n$. Todos los subconjuntos puedo clasificarlos disjuntamente por su cardinal, conjuntos con 1 elemento, con 2 elementos, con 3 elementos, con $n$ elementos, y así. Entonces el cardinal de partes de $A$ es igual a la suma de los números combinatorios.

$$
|p(A)| = 2^n = \binom{n}{0} + \binom{n}{1} + ... + \binom{n}{n} = \sum_{k=0}^n \binom{n}{k}
$$ 

## Proposición

Sea $n \in \mathbb{N}_0$ y $0 ≤ k ≤ n$

Entonces

$\boxed {\dbinom{n}{k} = \frac {n!} {k! \cdot (n - k)!}}$

## Anagramas

Un anagrama es una palabra o frase formada mediante la reordenación de las letras de otra palabra o frase. En otras palabras, se trata de un juego de palabras en el que se mezclan las letras de una palabra o frase para formar una nueva palabra o frase con las mismas letras pero en un orden diferente. Por ejemplo, la palabra "amor" es un anagrama de la palabra "roma". En esta materia se juega mucho a **calcular todos los posibles anagramas** de una palabra (a pesar de que estas palabras tengan o no sentido). 

Calcular la cantidad de anagramas posibles es equivalente a hacer una **permutación** cuando tiene letras que no se repiten, por ej:

GATO = 4!

Ahora, si quiero calcular los anagramas de la palabra “ananá” tengo el problema de que la **a** se repite 3 veces y la **n** 2. Lo que hago es dividir el numero de letras totales entre cada factorial de las letras que se repiten, con ananá quedaría $\frac{5!}{2! 3!}$.

El 5! de arriba porque ananá tiene 5 letras. El 2! porque la n se repite 2 veces y el 3 porque la a se repite 3.
