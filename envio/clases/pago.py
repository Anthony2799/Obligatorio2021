from envio.clases.group import Grupo

class pago:
    estrategia: Grupo
    
    def setStrategy(self, estrategia: Grupo = None) -> None:
        if estrategia is not None:
            self.estrategia = estrategia
        else:
            self.estrategia = Grupo.pago_normal
            
    
    def executeStrategy(self):
        print(str(self.estrategia.execute()))