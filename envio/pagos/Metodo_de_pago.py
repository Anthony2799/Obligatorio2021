from abc import ABC, abstractmethod

class Metodo_de_pago:
    
    @abstractmethod
    def execute(self) -> str:
         pass
