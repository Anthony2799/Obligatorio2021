from envio.clases.group import Grupo


class pago_normal(Grupo):
    precio = 180
    def execute(self) -> str:
        return str(self.precio)
