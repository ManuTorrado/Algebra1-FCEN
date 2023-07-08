class Polinomio:

    def __init__(self,coeficientes: list[complex or float or int]  ):
      
        self.coeficientes:list = coeficientes
        
    def Grado(self) -> int:
        return len(self.coeficientes) + 1
    
    def terminoIndependiente(self) ->int:
        res:int=self.coeficientes[len(self.coeficientes)]
        return res
    
    def evaluar(self, k:int) ->int:
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


# Hay que mejorarlo
def imprimirPolinomio(p:Polinomio) -> str:
    res:str = ''
    i:int = len(p.coeficientes)-1
    for coeficiente in p.coeficientes:
        res += '+'+str(coeficiente)+'X^'+str(i)
        i-=1 
    return res

