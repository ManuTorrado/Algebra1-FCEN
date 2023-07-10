from divisibilidad import divisoresDe, esPrimo, divideATodos

cuerpo:type = list[complex or float or int]

class Polinomio:

    def __init__(self,coeficientes: list[cuerpo]  ):
      
        self.coeficientes:list[cuerpo] = coeficientes
        self.terminoIndependiente:cuerpo = self.coeficientes[len(self.coeficientes) - 1]
        self.coeficientePrincpial:cuerpo = self.coeficientes[0]
        self.grado:int = len(self.coeficientes) - 1
        self.cuerpo:type = type(self.coeficientes)
    
    def __add__(self, otro_polinomio):
        coeficientes_resultantes = []
        max_grado = max(len(self.coeficientes), len(otro_polinomio.coeficientes))

        for i in range(max_grado):
            coeficiente_1 = self.coeficientes[i] if i < len(self.coeficientes) else 0
            coeficiente_2 = otro_polinomio.coeficientes[i] if i < len(otro_polinomio.coeficientes) else 0
            coeficiente_resultante = coeficiente_1 + coeficiente_2
            coeficientes_resultantes.append(coeficiente_resultante)

        return Polinomio(coeficientes_resultantes)
    
    
    
    def evaluar(self, k:int) -> int:
        res:int = 0
        i:int = len(self.coeficientes)-1
   
        for coeficiente in self.coeficientes:
            
            res += pow(k, i)*coeficiente
            i-=1
        return res
    

def esRaiz(k:int, f:Polinomio) -> bool:
    res:bool = f.evaluar(k) == 0
    return res


# Criterio de Gauss, solo para enteros
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
        

# Criterio de determinacion de la irreducibilidad de polinomios
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
    if(f.grado > p.grado):
        res = f
    else:
        res = p
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
        
        res = cociente + divisionSintetica(r,cociente)
        
    
    
    return res
        
   


# Hay que mejorarlo
def imprimirPolinomio(p:Polinomio) -> str:
    res:str = ''
    i:int = len(p.coeficientes)-1
    for coeficiente in p.coeficientes:
        res += '+'+str(coeficiente)+'X^'+str(i)
        i-=1 
    return res

