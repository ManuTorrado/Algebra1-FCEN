# Principio de buena ordenación

El **principio del buen orden** afirma que en cualquier conjunto de números naturales existe un mínimo, es decir, un número no mayor que algún otro del resto, siempre y cuando dicha colección no esté vacía. Esto diferencia al conjunto de los números naturales de otros conjuntos ordenados de números, como por ejemplo los números enteros o los números reales. El principio de buena ordenación es equivalente al principio de inducción: uno puede demostrarse a partir del otro.

# Principio de Inducción

*Citado del libro Introduction to abstract algebra de Jonathan Smith.*

**Paso base**: enuncia que la propiedad $P(0)$ se cumple.

**Paso inductivo**: Enuncia que si la propiedad $P(n)$ es verdadera, entonces $P(n+1)$ también lo es.

**Principio de inducción**: Enuncia que si el paso base y el paso inductivo se cumplen, entonces $P(n)$ se cumple para todo $n \in \mathbb{N}$.

**Demostrando el principio de inducción**

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

