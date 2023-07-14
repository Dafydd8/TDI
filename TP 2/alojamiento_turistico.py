from haversine import haversine, Unit
from typing import Tuple

class AlojamientoTuristico:
    ''' Encapsula la entidad 'Alojamiento Turístico' del Dataset '''
    
    def __init__(self, nom:str, lat:float, long:float, nom_calle:str, alt_calle:int, tel:str, email:str):
        ''' Inicializa un Alojamiento Turístico con:
            - nombre nom
            - latitud lat
            - longuitud long 
            - nombre de calle nom_calle
            - altura de calle alt_calle
            - teléfono tel
            - e-mail email
        '''
        self.nombre:str = nom
        self.latitud:float = lat
        self.longitud:float = long
        self.calle_nombre:str = nom_calle
        self.calle_altura:str = alt_calle
        if tel == '':
            self.telefono:str = 'N/D'
        else: 
            self.telefono:str = tel
        if email == '':
            self.email:str = 'N/D'
        else:
            self.email:str = email
        
    def __repr__(self) -> str:
       '''
       Requiere: nada.
       Devuelve: la representación compo string de un alojamiento.
       '''
       return 'ALOJAMIENTO:' + self.nombre 
        
    def contacto(self) -> str:
        '''
        Requiere: nada.
        Devuelve: la concatenación de teléfono y mail con el formato 'teléfono \ mail'. En caso de conocerse un solo atributo
        el valor devuelto es ese mismo; en caso de ser ambos desconocidos, se devuelve 'N/D' 
        '''
        if self.telefono == 'N/D' and self.email != 'N/D':
            return self.email
        elif self.email == 'N/D' and self.telefono != 'N/D':
            return self.telefono
        elif self.email == self.telefono == 'N/D':
            return 'N/D'
        else: 
            return self.telefono + ' | ' + self.email

    def distancia(self, lat:float , lng:float) -> float:
        '''
        Requiere: nada.
        Devuelve: la distancia entre un punto dado y el alojamiento.
        '''
        alojamiento:Tuple[float, float] = (self.latitud, self.longitud)    
        punto:Tuple[float, float] = (lat, lng)                             
        distancia:float = haversine(alojamiento, punto, unit=Unit.METERS)  
        return distancia
    
    def __lt__(self, other) -> bool:
        return self.nombre < other.nombre