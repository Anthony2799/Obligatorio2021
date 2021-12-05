from envio.clases.group import Grupo
from envio.clases.pago_normal import pago_normal


class pago:
    estrategia: Grupo

    def setStrategy(self, estrategia: Grupo = None) -> None:
        if estrategia is not None:
            self.estrategia = estrategia
        else:
            self.estrategia = pago_normal()

    def executeStrategy(self) -> str:
        return str(self.estrategia.execute())
