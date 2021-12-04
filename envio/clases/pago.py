from group import Grupo
class pago:
    estrategia : Grupo
    
    def setStrategy(self, estrategia: Grupo = None) -> None:
        if Grupo is not None:
            self.estrategia = Grupo
        else:
            self.estrategia = Grupo.pago_normal
            
    
    def executeStrategy(self):
        print(str(self.estrategia.execute()))