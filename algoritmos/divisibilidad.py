

def cuantasVecesAparece(a: any, l:list[any]) -> int:
    res:int = 0
    for x in list:
        if(x == a):
            res +=1
    return res
    

def esDivisiblePor(a:int, b:int) -> bool:
    res:bool = a%b == 0
    return res

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

def primosHasta(a:int) -> list[int]:
    res:list[int] = []
    aux:int = 2
    
    while(aux < a):
        if(esPrimo(aux)):
            res.append(aux)
    return res
    

def TCR (a:int) -> list[int]:
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
    
    return res