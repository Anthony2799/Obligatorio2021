from envio.pagos import Metodo_de_pago

class Mercado_pago(Metodo_de_pago):
    def devolucion(costo, nro_tarjeta) ->str:
        conexion_con_banco =""
        ##   Logica   ##
        if conexion_con_banco == '':
            
            return "Se efectuó el pago correctamete"
        else:
            return "No se pudo realizar el pago"  
        