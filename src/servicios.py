"""Servicios abstractos y especializados."""
from abc import ABC, abstractmethod
from .entidades import Entidad
from .excepciones import ServicioInvalidoError, CalculoCostoError

class Servicio(Entidad, ABC):
    def __init__(self, identificador, nombre, tarifa_base):
        super().__init__(identificador)
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise ServicioInvalidoError("Nombre de servicio inválido.")
        if isinstance(tarifa_base, bool) or not isinstance(tarifa_base, (int, float)) or tarifa_base < 0:
            raise ServicioInvalidoError("La tarifa debe ser un número no negativo.")
        self._nombre = nombre.strip()
        self._tarifa_base = float(tarifa_base)

    @property
    def nombre(self): return self._nombre
    @property
    def tarifa_base(self): return self._tarifa_base

    @abstractmethod
    def validar_cantidad(self, cantidad): pass
    @abstractmethod
    def describir(self): pass
    @abstractmethod
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0): pass

    def _total(self, cantidad, impuesto, descuento):
        self.validar_cantidad(cantidad)
        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 1:
            raise CalculoCostoError("Impuesto fuera del rango 0 a 1.")
        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)) or not 0 <= descuento <= 1:
            raise CalculoCostoError("Descuento fuera del rango 0 a 1.")
        return round(self.tarifa_base * cantidad * (1-descuento) * (1+impuesto), 2)

class ReservaSala(Servicio):
    def validar_cantidad(self, cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ServicioInvalidoError("Las horas deben ser mayores que cero.")
    def describir(self): return f"{self.nombre}: sala por hora."
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        return self._total(cantidad, impuesto, descuento)

class AlquilerEquipo(Servicio):
    def validar_cantidad(self, cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ServicioInvalidoError("Los días deben ser mayores que cero.")
    def describir(self): return f"{self.nombre}: alquiler por día."
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        return self._total(cantidad, impuesto, descuento)

class AsesoriaEspecializada(Servicio):
    def validar_cantidad(self, cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ServicioInvalidoError("Las sesiones deben ser mayores que cero.")
    def describir(self): return f"{self.nombre}: asesoría por sesión."
    def calcular_costo(self, cantidad=1, impuesto=0.0, descuento=0.0):
        return self._total(cantidad, impuesto, descuento)
