"""
Módulo: entidades.py
Descripción: Define la clase abstracta Entidad, que funciona como
estructura base para los objetos principales de Software FJ.
"""
from abc import ABC, abstractmethod
from .excepciones import ValidacionError


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general del sistema.

    Todas las entidades deben tener un identificador único
    y proporcionar una descripción de sus datos.
    """

    def __init__(self, identificador: str):
        # Validación del identificador.
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValidacionError(
                "El identificador debe ser texto no vacío."
            )

        self._identificador = identificador.strip()

    @property
    def identificador(self) -> str:
        """Permite consultar el identificador de la entidad."""
        return self._identificador

    @abstractmethod
    def describir(self) -> str:
        """
        Método abstracto que obliga a las clases hijas
        a implementar una descripción propia.
        """
        raise NotImplementedError(
            "La subclase debe implementar el método describir()."
        )
