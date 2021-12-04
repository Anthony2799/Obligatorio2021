from group import Grupo

class pago_normal(Grupo):
    precio =0
    
    def execute(self):
        return float(self.precio)