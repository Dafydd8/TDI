from typing import List
#################
## EJERCICIO 1 ##
#################
from typing import List
def esta_en(s: str, xs: List[str]) -> bool:
    """
	Requiere: xs está ordenada alfabéticamente
	Devuelve: devuelve True si y solo si hay algún i con 0 <= i < len(xs) tal que xs[i] == s
	Complejidad algorítmica: O(log(len(xs)))
	"""
    izq:int = 0
    der:int = len(xs)
    while izq < der:
        med:int = (izq + der) // 2
        if xs[med] == s:
            return True
        elif xs[med] < s:
            izq = med + 1
        else:
            der = med
    return False


#################
## EJERCICIO 2 ##
#################



def padrones_donde_vota(padrones: List[List[str]], nombre: str) -> List[int]:
    """
	Requiere: Para todo i, 0 <= i < len(padrones), padrones[i] está ordenado alfabéticamente
	Devuelve: Para cada elemento e de vr, vale que padrones[e] contiene el nombre "nombre"
	"""
    res:List[int] = [] #O(1)
    for i in range(len(padrones)): #O(n) (n = len(padrones))
       if esta_en(nombre, padrones[i]): #O(log2p)
           res.append(i)#O(1)
       #O(n*log2p)
    return res
        
        
        
        
        
        
        
