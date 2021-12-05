from _typeshed import Self
from group import Grupo

class pago_distanica_peso(Grupo):
      
    def precio_primario(self, peso):
        return float((self.precio)* peso)
    
    def execute(self,peso, distancia):
        precio =self.precio_primario(peso)
        porcentajes = 25
        peso = float((self.precio*self.porcentajes)/100)
        retorno = (peso * distancia)
        return str(retorno)