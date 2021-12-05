from envio.pagos import Metodo_de_pago 
from envio.pagos import Efectivo

class Envio:
    metodo_pago: Metodo_de_pago
    
    def setEstrategia (self, metodo_pago : Metodo_de_pago = None) -> None:
        if metodo_pago is not None:
            self.metodo_pago = metodo_pago
        else:
            self.metodo_pago = Efectivo()
            
    def ejecturarPago(self) -> str:
        return str(self.metodo_pago.execute())
    
    