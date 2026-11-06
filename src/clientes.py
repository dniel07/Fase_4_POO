"""Clientes y validaciones."""
import re
from .entidades import Entidad
from .excepciones import ClienteInvalidoError

class Cliente(Entidad):
    def __init__(self, identificador: str, nombre: str, correo: str, telefono: str):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self): return self._nombre
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ClienteInvalidoError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self): return self._correo
    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", valor.strip()):
            raise ClienteInvalidoError("El correo no tiene un formato válido.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self): return self._telefono
    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str):
            raise ClienteInvalidoError("El teléfono debe ser texto.")
        digitos = re.sub(r"\D", "", valor)
        if not 7 <= len(digitos) <= 15:
            raise ClienteInvalidoError("El teléfono debe tener entre 7 y 15 dígitos.")
        self._telefono = valor.strip()

    def describir(self):
        return f"Cliente {self.identificador}: {self.nombre} | {self.correo} | {self.telefono}"
