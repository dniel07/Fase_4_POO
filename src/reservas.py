"""Reservas y transiciones de estado."""
from datetime import datetime
from .entidades import Entidad
from .clientes import Cliente
from .servicios import Servicio
from .excepciones import ReservaError, EstadoReservaError

class Reserva(Entidad):
    def __init__(self, identificador, cliente, servicio, cantidad, impuesto=0.0, descuento=0.0):
        super().__init__(identificador)
        if not isinstance(cliente, Cliente):
            raise ReservaError("Se requiere un cliente válido.")
        if not isinstance(servicio, Servicio):
            raise ReservaError("Se requiere un servicio válido.")
        servicio.validar_cantidad(cantidad)
        self._cliente, self._servicio = cliente, servicio
        self._cantidad, self._impuesto, self._descuento = cantidad, impuesto, descuento
        self._estado = "pendiente"
        self._creada_en = datetime.now().isoformat(timespec="seconds")
        self._costo_final = None

    @property
    def cliente(self): return self._cliente
    @property
    def servicio(self): return self._servicio
    @property
    def estado(self): return self._estado
    @property
    def costo_final(self): return self._costo_final

    def confirmar(self):
        if self._estado != "pendiente":
            raise EstadoReservaError(f"No se puede confirmar una reserva {self._estado}.")
        self._estado = "confirmada"

    def cancelar(self):
        if self._estado in {"cancelada", "procesada"}:
            raise EstadoReservaError(f"No se puede cancelar una reserva {self._estado}.")
        self._estado = "cancelada"

    def procesar(self):
        if self._estado != "confirmada":
            raise EstadoReservaError("Solo se procesan reservas confirmadas.")
        try:
            total = self._servicio.calcular_costo(self._cantidad, self._impuesto, self._descuento)
        except Exception as error:
            raise ReservaError("No se pudo calcular el costo de la reserva.") from error
        self._costo_final, self._estado = total, "procesada"
        return total

    def describir(self):
        costo = "sin calcular" if self._costo_final is None else f"${self._costo_final:.2f}"
        return f"Reserva {self.identificador} | {self.cliente.nombre} | {self.servicio.nombre} | {self.estado} | {costo}"
