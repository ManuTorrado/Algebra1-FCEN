from conjuntos import interseccion 

def cuantasVecesAparece(a: any, l:list[any]) -> int:
    res:int = 0
    for x in l:
        if(x == a):
            res +=1
    return res

def borrarRepetidos(a:list) -> list:
    res:list =  set(a)       
    return res
    
def esDivisiblePor(a:int, b:int) -> bool:
    res:bool = a%b == 0
    return res


# revisa que dos numeros se dividan el uno al otro
def dobleDivision(a:int, b:int) -> bool:
    res: bool = esDivisiblePor(a,b) and esDivisiblePor(b,a)
    return res


def esPrimo(a:int) ->bool:
    res:bool = True
    aux:int = 2
    
    while(aux < a):
        if(esDivisiblePor(a, aux)):
            res = False
            break 
        aux +=1
        
    return res


# lista de numeros primos hasta n
def primosHasta(n:int) -> list[int]:
    res:list[int] = []
    aux:int = 2
    
    while(aux < n):
        if(esPrimo(aux)):
            res.append(aux)
    return res
    

# lista de los divisores primos de un numero por TFA
def TFA (a:int) -> list[int]:
    res:list[int] = []
    
    if(esPrimo(a)):
        return [a,1]
    
    aux:int = 2
    while(aux < a):
        if(esPrimo(aux)):
            if(esDivisiblePor(a, aux)):
                res.append(aux)
        aux +=1
        
    
    return res

def cantidadDeDivisoresPositivos(a:int) ->int:
    res:int = 1
    setA:list[int] = borrarRepetidos(TFA(a))
    for x in setA:
        res = res*(cuantasVecesAparece(x, TFA(a)) + 1)
        
    if(res == 1):
        res = 2
    
    return res

def divisoresDe(n:int) -> list[int]:
    res:list[int] = []
    aux:int = 1
    while(aux <= n):
        if(esDivisiblePor(n,aux)):
            res.append(aux)
            res.append(-aux)
        aux += 1
    
    return res


def divisoresPositivos(n:int) -> list[int]:
    res:list[int] = []
    aux:int = 1
    while(aux <= n):
        if(esDivisiblePor(n,aux)):
            res.append(aux)
        aux += 1
    
    return res


def mcd(a:int, b:int) -> int:
    if(a%b == 0):
        return b
    elif(b%a == 0):
        return a
    if(a%b == 1 or a%b ==1):
        return 1      
    mcd(a, a%b)


def sonCoprimos(a:int, b:int) -> bool:
    res:bool = interseccion(divisoresDe(a),divisoresDe(b)) == [1]
    return res

def sonMultiplos(a:int, b:int) -> bool:
    res:bool = False
    
    return res


def esCongruente(a:int, b:int, m:int) -> bool:
    res:bool =  m%(a-b) == 0  
    return res


