"""
excepciones.py
Define los errores personalizados del sistema Software FJ.
"""

class SoftwareFJError(Exception):
    """Excepción base de todos los errores controlados del sistema."""
    pass


class ValidacionError(SoftwareFJError):
    """Error cuando un dato no cumple las reglas establecidas."""
    pass


class ClienteInvalidoError(ValidacionError):
    """Error relacionado con los datos de un cliente."""
    pass


class ServicioInvalidoError(ValidacionError):
    """Error relacionado con los datos o parámetros de un servicio."""
    pass


class ReservaError(SoftwareFJError):
    """Error general durante la gestión de una reserva."""
    pass


class EstadoReservaError(ReservaError):
    """Error cuando se intenta una operación no permitida por el estado de la reserva."""
    pass


class RecursoNoDisponibleError(ReservaError):
    """Error cuando un servicio o recurso no está disponible."""
    pass


class CalculoCostoError(SoftwareFJError):
    """Error cuando no se puede calcular un costo válido."""
    pass

