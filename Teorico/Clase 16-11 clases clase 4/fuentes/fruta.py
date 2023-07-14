class Fruta:
    ''' Encapsula la entidad 'fruta'.
        Una fruta f tiene atributos:
            - f.nombre (str)
            - f.precio (float)
        y métodos:
            - representación como string
            - igual a: =, cuando tienen el mismo nombre
    '''

    def __init__(self, n:str, p:float):
        ''' Inicializa una fruta con nombre n, precio p. '''
        self.nombre:str = n
        self.precio:float = p

    def __repr__(self) -> str:
        ''' Devuelve un string con los datos de la fruta.'''
        return self.nombre + ' ($' + str(self.precio) + '/kg)'

