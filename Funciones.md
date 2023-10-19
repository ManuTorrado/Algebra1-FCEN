# Funciones 
Sean $A$ y $B$ conjuntos, y sea $\mathcal R$ una **relacion** de $A$ en $B$.  Se dice que $\mathcal R$ es una función si para cada $x$ $\in A$  existe un $y \in B$ , y este elemento $y$ es único. Es decir:

$$
\forall x \in A, \exists! \space y \in B \space/\space x \space \mathcal R \space y
$$

Sean $A$ y $B$ conjuntos. Una relación $\mathcal R$ de $A$ en $B$ es un subconjunto cualquiera $\mathcal R$ del producto cartesiano $A \times B$. Es decir $\mathcal R$ es una relación de $A$  en $B$ si $\mathcal R\in\mathcal P(A\times B)$.


# Relaciones
- $\mathcal R$ es una relación de $A$ en $B$ $\iff$ $\mathcal R \subseteq A \times B$
- Como $A \times B \not = B \times A$, el orden de los elementos de los pares importa. No son iguales las relaciones de $A$ en $B$ y las relaciones de $B$ en $A$
- En vez de expresar: $(a, 1) \in \mathcal R_1$, se denota como: $a \space \mathcal R_1 \space 1$ (se lee " $a$ *está relacionado* con 1 ").
- El vacío, denotado $\emptyset$, siempre esta contenido en $A \times B$, por lo que puede estar en $\mathcal R$.

# Tipos de relaciones

### Relación reflexiva

Se dice que $R$ es reflexiva si $(x, x) ∈ R, ∀ x ∈ A$ (dicho de otra
manera, $x R x, ∀ x ∈ A$).

### Relación simétrica

Se dice que $R$  es $simétrica$ si cada vez que un par $(x, y) ∈ R$ , entonces el par “simétrico” $(y, x) ∈ R$ también (dicho de otra manera,
$∀ x, y ∈ A, x R y ⇒ y R x$ )

### Relación antisimétrica

Se dice que $R$ es $antisimétrica$ si cada vez que un par $(x, y) ∈ R$ con $x \cancel{ = } y$ , entonces el par $(y, x) ∈ R$ (dicho de otra manera,

 $∀ x, y ∈
A, x R y \text{ e } y R x ⇒ x = y$ ).

### Relación transitiva

Se dice que $R$ es transitiva si para toda terna de elementos $x, y, z ∈ A$ tales que $(x, y) ∈ R \text{ e } (y, z) ∈ R$ , se tiene que $(x, z) ∈ R$ también (dicho de otra manera, $∀ x, y, z ∈ A, x R y \text{ e } y R z ⇒ x R z$ ).


## Relaciones de orden
Este ya lo vimos anteriormente, pero repasemos

**Relacion de orden**

- Reflexividad: $x \mathcal{R}  x$
- Transitividad:  $x \mathcal{R} y$ ^  $y \mathcal{R} z$ $\rightarrow$ $x \mathcal{R} z$   
- Antisimetria: $x \mathcal{R} y$ ^  $y \mathcal{R} x$ $\rightarrow$ $x = y$   


## Relaciones de equivalencia
Para ser una relación de equivalencia tiene que ser una relación:

- Reflexiva
- Simétrica
- Transitiva


## Clases de equivalencia
