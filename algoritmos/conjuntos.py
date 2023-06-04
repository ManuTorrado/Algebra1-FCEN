# NOTA: Existen los tipos set y frozenset pero voy a utilizar listas

def pertenece(a: any, l:list[any]) -> bool:
    res:bool = False
    
    for  x in l:
        if(a == x):
            res = True
            break
    
    return res

def inlcusion(a:list, b:list) -> bool:
    res:bool = True
    
    for x in a:
        if(not pertenece(x, b)):
            res = False
            break
  
    return res
    
def cardinal(a:list[any]) -> int:
    res = len(a)
    return res


def union(a:list, b:list) -> list:
    res:list = a + b
    return res

# importa el orden
def diferencia(a:list,b:list) ->list:
    res:list=[]
    
    for x in a:
        if(not pertenece(x,b)):
            res.append(x)
    
    return res
    
def sonConjuntosIguales(a:list[any], b:list[any]) -> bool:
    res:bool = inlcusion(a,b) and inlcusion(b,a)
    return res

# no importa el orden
def interseccion(a:list, b:list) -> list:
    res:list = []
    for x in a:
        if(pertenece(x,b)):
            res.append(x)
    return res



def diferenciaSimetrica(a:list, b:list) -> list:
    res:list = diferencia(union(a,b), interseccion(a,b))      
    return res
