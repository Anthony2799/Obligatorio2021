from envio.clases.group import Grupo

class pago_peso(Grupo):
    precio = 180
    
    def execute(self, peso) -> str:
        resultado = self.precio*peso
        return str(resultado)