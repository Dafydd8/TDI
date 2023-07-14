from typing import List 

def frutas_n_cortas_v1(frutas:List[str], n:int) -> List[str]:
    '''
    Requiere: 'frutas' está formado unicamente por strings de nombres de frutas.
    Devuelve: Una lista con el nombre de las frutas que aparecian en 'frutas' y que tienen menos de n letras.
    '''
    i:int = 0
    res:List(str) = []
    while i < len(frutas):
        if len(frutas[i]) < n:
            res.append(frutas[i])
        i = i + 1
    return res
prueba = ['kiwi', 'manzana', 'uva', 'banana', 'frutilla','pera', 'naranja']
print(frutas_n_cortas_v1(prueba, 7))

def frutas_n_cortas_v2(frutas:List[str], n:int) -> List[str]:
    '''
    Requiere: 'frutas' está formado únicamente por strings de nombres de frutas.
    Devuelve: Una lista con el nombre de las frutas que aparecian en 'frutas' y que tienen menos de n letras.
    '''
    res:List(str) = []
    for i in frutas:
        if len(frutas[i]) < n:
            res.append(frutas[i])
    return res
prueba = ['kiwi', 'manzana', 'uva', 'banana', 'frutilla','pera', 'naranja']
print(frutas_n_cortas_v1(prueba, 7))    