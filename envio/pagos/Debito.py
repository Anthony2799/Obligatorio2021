from envio.pagos.Metodo_de_pago import Metodo_de_pago 
from envio.pagos.Debito import Metodo_de_pago

class Debito(Metodo_de_pago):
    def devolucion(self,costo, nro_tarjeta) ->str:
        conexion_con_banco =""
        ##   Logica   ##
        if conexion_con_banco == '':
            
            return "Se efectuó el pago correctamete"
        else:
            return "No se pudo realizar el pago"  
        