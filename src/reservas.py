"""
Módulo: reservas.py
Descripción: Administra las reservas, su estado y su procesamiento.
"""

from datetime import datetime
from .entidades import Entidad
from .clientes import Cliente
from .servicios import Servicio
from .excepciones import ReservaError, EstadoReservaError

class Reserva(Entidad):
    """
    Relaciona un cliente con un servicio y controla
    el ciclo de vida de una reserva.
    """

    ESTADOS = {
        "pendiente",
        "confirmada",
        "cancelada",
        "procesada"
    }
    
    def __init__(self, identificador, cliente, servicio, cantidad, impuesto=0.0, descuento=0.0):
        super().__init__(identificador)
        if not isinstance(cliente, Cliente):
            raise ReservaError("Se requiere un cliente válido.")
        if not isinstance(servicio, Servicio):
            raise ReservaError("Se requiere un servicio válido.")
            
        # Validar que el recurso esté disponible.
        servicio.validar_disponibilidad() 
        
        # Validar la cantidad solicitada.
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
    def cantidad(self):
        return self._cantidad        
    @property
    def estado(self): return self._estado
    @property
    def costo_final(self): return self._costo_final
    @property
    def creada_en(self):
        return self._creada_en

    def confirmar(self):
        """Confirma una reserva que esté pendiente."""
        
        if self._estado != "pendiente":
            raise EstadoReservaError(f"No se puede confirmar una reserva {self._estado}.")
            
        self._servicio.validar_disponibilidad()    
        self._estado = "confirmada"

    def cancelar(self):
        """Cancela una reserva que no haya sido procesada."""
        
        if self._estado in {"cancelada", "procesada"}:
            raise EstadoReservaError(f"No se puede cancelar una reserva {self._estado}.")
        self._estado = "cancelada"

    def procesar(self):
        """
        Procesa una reserva confirmada y calcula
        el costo final del servicio.
        """
        
        if self._estado != "confirmada":
            raise EstadoReservaError("Solo se procesan reservas confirmadas.")
        try:
            total = self._servicio.calcular_costo(self._cantidad, self._impuesto, self._descuento)
        except Exception as error:
            raise ReservaError("No se pudo calcular el costo de la reserva.") from error
        self._costo_final, self._estado = total, "procesada"
        return total

    def describir(self):
        """Devuelve el resumen de la reserva."""
        
        costo = "sin calcular" if self._costo_final is None else f"${self._costo_final:.2f}"
        return f"Reserva {self.identificador} | {self.cliente.nombre} | {self.servicio.nombre} | {self.estado} | {costo}"
