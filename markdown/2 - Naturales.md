# Ordenando Numeros
Dado un conjunto **finito** de numeros naturales o enteros. Al ser finito podemos afirmar que existe un **elemento minimo**, es decir, que sera mas chico que el resto de elementos del conjunto (Tengamos en cuenta que en este tipo de conjuntos los elementos no se pueden repetir) Esto se llama **Principio de buena ordenacion** y la definiremos mas adelante. Expresemos esto formalmente:

Dado un conjunto $A \not = \emptyset$ / $A \subset \mathbb{N}$
$\text{    }\rightarrow \text{    }$  $\exists n \in A / n \leq y \text{    }$ $\text{    }\forall y \in A$

> Y que tiene de importante esto?

Nos permite ordenar los numeros de un conjunto, creando una **relacion de orden**. Un ejemplo de relacion de orden son los simbolos $\leq$ y $\geq$. Que sentido tendrian estos simbolos si los numeros no estan ordenados?

Resulta que las relaciones de orden ocurren en muchos lados, y para ser existir tienen que cumplir 3 condiciones: Reflexividad, Transitividad y Antisimetria. Si no se entiende del todo no pasa nada, se va a profundizar en esto mas adelante.
Aca va un ejemplo de como es la relacion de orden con $\leq$ y $\geq$.

**Relacion de orden**
- Reflexividad: $x\leq x$
- Transitividad:  ($x\leq y$ ^  $y\leq z$) $\rightarrow$ $x \leq z$   
- Antisimetria: ($x\leq y$ ^  $y\leq x$) $\rightarrow$ $x = y$   

# Principio de buena ordenación

El **principio del buen orden** afirma que en cualquier conjunto de números naturales existe un mínimo, es decir, un número no mayor que algún otro del resto, siempre y cuando dicha colección no esté vacía. Esto diferencia al conjunto de los números naturales de otros conjuntos ordenados de números, como por ejemplo los números enteros o los números reales. El principio de buena ordenación es equivalente al principio de inducción: uno puede demostrarse a partir del otro.

# Principio de Inducción
Conoces la siguiente formula? Parece una monstruosidad pero no te asustes:
$$1 + 2 + 3 + ... + n = ∑_{i=1}^{n} i = n(n+1)/2$$

Se llama Suma de Gauss. Sirve para darnos la suma de los n numeros que le demos. Es decir, si n = 100, me devolvera la suma de 1 + 2 + 3 + 4 ... + 100.
Sabemos que la suma de Gauss funciona, pero como lo sabemos? Como podemos estar seguros de que esta suma sirve siempre y para todos los naturales?
La razon por la que podemos confiar en la suma de Gauss es gracias a que se puede realizar una **demostracion por induccion**. Al final de este capitulo haremos la demostracion de la suma de Gauss por induccion.


## Pasos para una demostracion por induccion

**Paso base**: enuncia que la propiedad $P(0)$ se cumple.

**Paso inductivo**: Enuncia que si la propiedad $P(n)$ es verdadera, entonces $P(n+1)$ también lo es.

**Principio de inducción**: Enuncia que si el paso base y el paso inductivo se cumplen, entonces $P(n)$ se cumple para todo $n \in \mathbb{N}$.


> Y como se que el principio de induccion no falla?

# Demostrando el principio de inducción
*Citado del libro Introduction to abstract algebra de Jonathan Smith.*

Vamos a asumir que el paso base y el paso inductivo se cumplen pero que el principio de inducción no lo hace, es decir que:

 $P(0)$ es verdadero y $P(n)$ verdadero $\rightarrow$ $P(n+1)$ verdadero, pero existe un $P(n)$ falso. Si pensamos en todos los $n$ tal que $P(n)$ es falso como un conjunto

entonces el conjunto $S = \Set{n \ |\ P(n) \text{ es falso} \}$ es no vacío (asumiendo que el principio de inducción falla).

Por el **principio de buena ordenación**, el conjunto $S$ tiene un elemento mínimo $\lambda$.

El paso base me dice que $P(0)$ se cumple, entonces no pertenece a $S$. Por este motivo $\lambda > 0$ y $\lambda -1$ es un numero natural.

Recordemos que como $\lambda$ es el elemento mas chico de $S$, entonces $\lambda -1$ no pertenece a $S$.

Como $\lambda-1 \not \in S$, entonces $P(\lambda-1)$ se cumple.

El **paso inductivo** entonces, nos dice que $P(\lambda)$ es verdadero, pero esto es una **contradicción**. Solo puede ser verdadero si el principio de inducción se cumple.

De esta manera, el principio de inducción no puede fallar.



## Inducción II/Fuerte/Completa
En esta materia les gusta llamar Induccion II/Fuerte/Completa/Global (entre otros nombres) A la induccion aplicada en sucesiones. Pero la realidad es que la induccion es solo una y estos nombres solo los encontramos aqui.

$\text{Sea } p(n), n \in \mathbb{N} \text{ una afirmacion sobre los numeros naturales. Si } p \text{ satisface :}$

- (Casos base):  $p(1)$ y $p(2)$ Son verdaderas
- (Paso inductivo): $\forall h \in \mathbb{N}, p(h)$  y $p(h+1)$ Verdaderas,   $\Rightarrow p(h+2)$ Verdaderas

Entonces $p(n)$ es verdadero $\forall n \in \mathbb{N}$



## Demostración de la Suma de Gauss por Inducción

Queremos demostrar que la suma de los primeros \(n\) números naturales es igual a $\(\frac{n(n+1)}{2}\)$ utilizando el principio de inducción matemática.

**Paso 1: Caso Base (n = 1):**

Cuando $\(n = 1\)$, tenemos:

$$\[
1 = \frac{1(1+1)}{2}
\]$$

Esto demuestra que la fórmula es válida para \(n = 1\).

**Paso 2: Hipótesis de Inducción:**

Suponemos que la fórmula es válida para un valor arbitrario \(k\), es decir, suponemos que:

$$\[
1 + 2 + 3 + \ldots + k = \frac{k(k+1)}{2}
\]$$

**Paso 3: Paso Inductivo:**

Queremos demostrar que la fórmula también es válida para \(k+1\). Entonces, sumamos \((k+1)\) al lado izquierdo de la ecuación:

$$\[
1 + 2 + 3 + \ldots + k + (k+1)
\]$$

Por nuestra hipótesis de inducción, sabemos que:

$$\[
1 + 2 + 3 + \ldots + k = \frac{k(k+1)}{2}
\]$$

Por lo tanto, podemos escribir:

$$\[
1 + 2 + 3 + \ldots + k + (k+1) = \frac{k(k+1)}{2} + (k+1)
\]$$

Factorizamos \((k+1)\) en el lado derecho:

$$\[
1 + 2 + 3 + \ldots + k + (k+1) = \frac{k(k+1)}{2} + \frac{2(k+1)}{2}
\]$$

Combinamos los términos del lado derecho:

$$\[
1 + 2 + 3 + \ldots + k + (k+1) = \frac{k(k+1) + 2(k+1)}{2}
\]$$

Factor común \((k+1)\) en el numerador:

$$\[
1 + 2 + 3 + \ldots + k + (k+1) = \frac{(k+1)(k+2)}{2}
\]$$

Esto demuestra que la fórmula es válida para \(k+1\).

**Conclusión:**

Hemos demostrado la fórmula de la suma de Gauss por inducción para todos los números naturales $\(n\)$. Por lo tanto, la suma de los primeros $\(n\)$ números naturales es igual a $\(\frac{n(n+1)}{2}\)$ para cualquier $\(n\)$.



## El Conjunto Inductivo

Sea $H \subset \mathbb{R}$  un conjunto, se dice que $H$ es un conjunto inductivo si se cumplen las condiciones siguientes

- $1 \in H$
- $\forall x,  x \in H \Rightarrow x+1 \in H$
