from typing import List

class Naipe:
    def __init__(self, numero:int, palo:str):
        ''' Inicializa el naipe con el palo y numero dados.
            Requiere: numero es un entero entre 1 y 12 inclusive;
                 palo vale 'oros', 'copas', 'espadas' o 'bastos'. '''
        self.numero:int = numero
        self.palo:str = palo
        
    def __repr__(self):
        ''' Representación str de un naipe. 
            Requiere: Nada. '''
        return str(self.numero) +' de ' + self.palo

    def __lt__(self, other) -> bool:
        ''' Requiere: Nada.
            Devuelve: True si un naipe viene antes que otro en el mazo,
                primero según el palo (oros < copas < espadas < bastos)
                y segundo según el número. '''
        if self.palo == other.palo:
            return self.numero < other.numero
        elif self.palo == 'oros' and other.palo == 'copas':
            return True
        elif self.palo == 'oros' and other.palo == 'espadas':
            return True
        elif self.palo == 'oros' and other.palo == 'bastos':
            return True
        elif self.palo == 'copas' and other.palo == 'espadas':
            return True
        elif self.palo == 'copas' and other.palo == 'bastos':
            return True
        elif self.palo == 'espadas' and other.palo == 'bastos':
            return True
        else:
            return False
        
class Mazo:
    def __init__(self):
        ''' Inicializa el mazo sin ningún naipe. 
            Requiere: Nada.'''
        self.naipes:List[Naipe] = []
        self.mayor:Naipe = Naipe(0, 'oros') #creado

    def agregar(self, naipe:Naipe):
        ''' Agrega el naipe al mazo. 
            Requiere: Nada. ''' 
        self.naipes.append(naipe)
        if len(self.naipes) == 1: # de aca para abajo agregado
            self.mayor = naipe
        if len(self.naipes) > 1:
            if naipe > self.mayor:
                self.mayor = naipe
                
    def naipe_mas_alto(self) -> Naipe:
        ''' Requiere: hay al menos un naipe en el mazo. 
            Devuelve: el naipe más alto del mazo.'''
        return self.mayor

    def ordenar(self):
        ''' Ordena los naipes del mazo de menor a mayor. 
            Requiere: Nada. '''
        self.naipes.sort()

    def __repr__(self):
        ''' Representación str de un mazo de naipes. 
            Requiere: Nada. '''
        return str(self.naipes)

