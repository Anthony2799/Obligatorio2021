from envio.clases.group import Grupo

class pago_peso(Grupo):
    precio =0
    
    def execute(self, peso):
        return float((self.precio)* peso)