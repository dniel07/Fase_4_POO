"""
entidades.py
Define la clase abstracta base para las entidades de Software FJ.
"""

from abc import ABC, abstractmethod

from .excepciones import ValidacionError


class Entidad(ABC):
    """
    Clase abstracta que establece las características comunes
    de las entidades del sistema.
    """

    def __init__(self, identificador: str):
        """
        Inicializa una entidad con un identificador obligatorio.
        """

       
        if not isinstance(identificador, str):
            raise ValidacionError(
                "El identificador debe ser una cadena de texto."
            )

        identificador = identificador.strip()

        if not identificador:
            raise ValidacionError(
                "El identificador no puede estar vacío."
            )

        self._identificador = identificador

    @property
    def identificador(self) -> str:
        """
        Permite consultar el identificador de forma controlada.
        """
        return self._identificador

    @abstractmethod
    def describir(self) -> str:
        """
        Obliga a las clases hijas a implementar una descripción.
        """
        raise NotImplementedError(
            "Cada entidad debe implementar el método describir()."
        )
