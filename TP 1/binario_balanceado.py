def string_inverso(t:str) -> str: #funciÃ³n auxiliar
    '''
       Requiere: nada.
       Devuelve: el string ingresado con los caracteres re-ordenados de atras
       hacia adelante.
    '''
    pos:int = len(t) - 1
    res:str = ''
    while pos >= 0:
        res = res + t[pos]
        pos = pos - 1
    return res
print(string_inverso('dumbledore'))

def decimal_a_binario(n:int) -> str:
    '''
       Requiere: n > 0.
       Devuelve: el nÃºmero decimal ingresado, en binario.
    '''
    rv:str = ''
    while n >= 1:
        rv = rv + str(n % 2)
        n = n // 2
    rv = string_inverso(rv)
    return rv

def es_binario_balanceado(n: int) -> bool:
    '''
        Requiere: n > 0
        Devuelve: True si el nÃºmero binario dado es balanceado y False en caso contrario.     
    '''
    i:int = 0
    bina:str = decimal_a_binario(n)
    unos:int = 0
    ceros:int = 0
    #A
    while i < len(bina):
        #B
        if bina[i] == "1":
            unos = unos + 1
        else:
            ceros = ceros + 1
        i = i + 1
        #C
    #D
    return unos == ceros

def cantidad_binarios_balanceados_entre(n:int, m:int) -> int:
    '''
        Requiere: n y m son numeros naturales y n <= m.
        Devuelve: la cantidad de binarios balanceados mayores
        e iguales que n y menores e iguales que m.
    '''
    res: int = 0
    while n <= m:
        if es_binario_balanceado(n):
            res = res + 1
        n = n + 1
    return res

def siguiente_binario_balanceado (n: int) -> int:
    '''
        Requiere: n > 0.
        Devuelve: el menor número balanceado estrictamente mayor que n.
    '''
    i: int = n
    encontrado: bool = False
    #A
    while not encontrado:
        #B
        i = i + 1 
        encontrado = (es_binario_balanceado(i))
        #C
    #D
    return i

def anterior_binario_balanceado(n:int) -> int:
    '''
        Requiere: n >= 3.
        Devuelve: el mayor número balanceado estrictamente menor que n y mayor o igual a 3.
    '''
    i:int = n
    encontrado:bool = False
    while not encontrado:
        i = i - 1
        encontrado = es_binario_balanceado(i)
    return i

def binario_balanceado_mas_cercano(n:int) -> int:
    '''
        Requiere: n > 0.
        Devuelve: el número balanceado mas cercano a n (o n si n es balanceado).
    '''
    res:int = 0
    menor:str = anterior_binario_balanceado(n)
    mayor:str = siguiente_binario_balanceado(n)
    if n == 1:
        res = 2    
    elif es_binario_balanceado(n):
        res = n
    elif n - menor == mayor - n:
        res = mayor
    elif n - menor < mayor - n:
        res = menor
    else:
        res = mayor
    return res
  