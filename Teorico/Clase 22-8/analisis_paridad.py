def es_par(n:int) -> bool:
    ''' Requiere: nada.
        Devuelve: True si n es par, False si es impar.
    '''
    b:bool = (n % 2 == 0)
    return b

def describir_paridad(n:int) -> str:
    ''' Requiere: nada.
        Devuelve: "El número es par/impar", según corresponda.
    '''
    if es_par(n):
       vr:str =  'El numero ' + str(n) + ' es par'
    else:
       vr:str = 'El numero ' + str(n) + ' es impar'
      
    return vr

#_______Cuerpo principal del programa_______#

print(es_par(7))  # imprime: False
print(es_par(8))  # imprime: True

print(describir_paridad(7))  # imprime: El número es impar
print(describir_paridad(8))  # imprime: El número es par
