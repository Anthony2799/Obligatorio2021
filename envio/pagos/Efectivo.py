from envio.pagos.Metodo_de_pago import Metodo_de_pago


class Efectivo(Metodo_de_pago):
    
    def devolucion(self,costo):
        return "Se efectuó el pago correctamete"