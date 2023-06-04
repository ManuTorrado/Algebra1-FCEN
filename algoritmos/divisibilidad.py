

def cuantasVecesAparece(a: any, l:list[any]) -> int:
    res:int = 0
    for x in l:
        if(x == a):
            res +=1
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
        
    
    return res

def cantidadDeDivisores(a:int) ->int:
    res:int = 0
    
    return res

def mcd(a:int, b:int) -> int:
    res:int = 0
    aux:int = 1
    
    if(a%b == 0):
        res = a
    
    return res
