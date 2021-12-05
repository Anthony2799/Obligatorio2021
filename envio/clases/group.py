from abc import ABC, abstractmethod

## Strategy interface
class Grupo(ABC):
    
    @abstractmethod
    def execute(self) -> str:
       pass