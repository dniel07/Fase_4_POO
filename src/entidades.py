"""Clase abstracta común."""
from abc import ABC, abstractmethod
from .excepciones import ValidacionError

class Entidad(ABC):
    def __init__(self, identificador: str):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValidacionError("El identificador debe ser texto no vacío.")
        self._identificador = identificador.strip()

    @property
    def identificador(self) -> str:
        return self._identificador

    @abstractmethod
    def describir(self) -> str:
        raise NotImplementedError
