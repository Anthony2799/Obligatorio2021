from envio.clases.group import Grupo

class pago_distanica_peso(Grupo):
    precio=180
    def precio_primario(self, peso):
        return float(self.precio*peso)
    
    def execute(self,peso,distancia):
        precio =self.precio_primario(peso)
        porcentajes = 25
        peso = (precio*porcentajes) / 100
        retorno = peso * distancia
        return str(retorno)