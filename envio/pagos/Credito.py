from envio.pagos.Metodo_de_pago import Metodo_de_pago 
from envio.pagos.Credito import Metodo_de_pago


class Credito(Metodo_de_pago):

    def devolucion(self, costo, nro_tarjeta, cuotas) -> str:
        return "Se efectuó el pago correctamete"

