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
    
def sonConjuntosIguales(a:list[any], b:list[any]) -> bool:
    res:bool = inlcusion(a,b) and inlcusion(b,a)
    return res

