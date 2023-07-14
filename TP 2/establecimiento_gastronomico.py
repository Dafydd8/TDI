class EstablecimientoGastronomico:
    '''Encapsula la entidad 'Establecimiento Gastronómico' del Dataset'''
    
    def __init__(self, nom: str, calle:str, altura:int, rubro:str, long:float, lat:float):
        ''' Inicializa un Establecimiento Gastronómico con:
        - nombre nom 
        - rubro rubro
        - calle_nombre calle
        - calle_altura altura
        - longitud long
        - latitud lat
        '''
        self.nombre:str = nom
        self.rubro:str = rubro
        self.calle_nombre:str = calle
        self.calle_altura:int = altura
        self.latitud:float = lat
        self.longitud:float = long
        
    def __repr__(self) -> str:
        """
        Requiere: nada.
        Devuelve: la representacion en forma de string del establecimiento gastronomico.
        """
        return self.nombre + "@" + self.calle_nombre + " " + str(self.calle_altura)