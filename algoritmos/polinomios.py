from divisibilidad import divisoresDe, esPrimo, divideATodos

cuerpo:type = list[complex or float or int]

class Polinomio:

    def __init__(self,coeficientes: list[cuerpo]  ):
      
        self.coeficientes:list = coeficientes
        self.terminoIndependiente = self.coeficientes[len(self.coeficientes)]
        self.coeficientePrincpial = self.coeficientes[0]
        
        
    def Grado(self) -> int:
        return len(self.coeficientes) - 1
    
    def cuerpo(self) -> type:
        res:type = type(self.coeficientes)
        return res
    
    
    def evaluar(self, k:int) -> int:
        res:int = 0
        i:int = len(self.coeficientes)-1
   
        for coeficiente in self.coeficientes:
            
            res += pow(k, i)*coeficiente
            i-=1
        return res
    
    def Coeficientes(self) -> int:
        return self.coeficientes


def esRaiz(k:int, f:Polinomio) -> bool:
    res:bool = f.evaluar(k) == 0
    return res


def criterioGauss(f:Polinomio) -> list[int]:
    res:list[int]
    divisoresPolinomio:list[int] = divisoresDe(f.terminoIndependiente())
    for divisor in divisoresPolinomio:
        if(esRaiz(divisor)):
            res.append(divisor)
            
    return res

def grado(p: Polinomio) -> int:
    res:int = len(p.coeficientes) -1
    return res

def mayorCoeficiente(f:Polinomio) -> cuerpo:
    res:cuerpo = f[0]
    for coeficiente in f.coeficientes:
        if(coeficiente > res):
            res= coeficiente
    return res
        


def criterioEisenstein(f:Polinomio) -> bool:
    res:bool = False
    i:int = 0
    copia:Polinomio = f
    del copia.coeficientes[-1]
    while(i< mayorCoeficiente(f)):
        if(esPrimo(i) and divideATodos(i, copia.coeficientes) and (not (i%copia.terminoIndependiente == 0)) and (not (pow(i,2) % copia.terminoIndependiente == 0))):
            res = True
            break    
        i+=1
        
    return res
    

def esIrreducible(p: Polinomio) -> bool:
    res:bool = False
    if(grado(p) == 1 or criterioEisenstein(p)):
        res= True
        return res
    
def mayorGrado(f:Polinomio, p:Polinomio) -> Polinomio:
    res:Polinomio
    if(f.Grado > p.Grado):
        res = f
    else:
        res = p
    return res


# TODO
def sumaPolinomios(f:Polinomio, p:Polinomio) -> Polinomio:
    res:Polinomio
    aux:list[cuerpo] = []
    if(mayorGrado(f,p) == f):
        i:int = 0
        for coeficiente in  p.coeficientes:
            aux.append(coeficiente + f.coeficientes([grado(p)-i]))
            i+=1
    else:
        i:int = 0
        for coeficiente in  f.coeficientes:
            aux.append(coeficiente + p.coeficientes([grado(f)-i]))
            i+=1   
        
    return res
    
# Asumo f dividio q
def divisionSintetica(f:Polinomio, q:Polinomio) -> Polinomio:
    res:Polinomio
    cociente:Polinomio = Polinomio()
    
    if(not esIrreducible(f)):
        
        nuevoGrado:int = grado(f) - grado(q)
       
        coeficientes:list[cuerpo] = []
        i:int = 0
        while(i < nuevoGrado):
            coeficientes.append(0)
        coeficientes.append(f.coeficientePrincpial)
           
        r:Polinomio = Polinomio(coeficientes)       
        
        res = sumaPolinomios(cociente , divisionSintetica(r, cociente))
        
    
    
    return res
        
   


# Hay que mejorarlo
def imprimirPolinomio(p:Polinomio) -> str:
    res:str = ''
    i:int = len(p.coeficientes)-1
    for coeficiente in p.coeficientes:
        res += '+'+str(coeficiente)+'X^'+str(i)
        i-=1 
    return res

