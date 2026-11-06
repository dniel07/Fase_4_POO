"""Excepciones personalizadas del sistema."""
class SoftwareFJError(Exception):
    """Clase base de errores controlados."""
class ValidacionError(SoftwareFJError):
    """Error general de validación."""
class ClienteInvalidoError(ValidacionError):
    """Datos incorrectos de cliente."""
class ServicioInvalidoError(ValidacionError):
    """Datos incorrectos de servicio."""
class ReservaError(SoftwareFJError):
    """Error general de reservas."""
class EstadoReservaError(ReservaError):
    """Transición de estado no permitida."""
class RecursoNoDisponibleError(ReservaError):
    """Recurso no disponible."""
class CalculoCostoError(SoftwareFJError):
    """Error de cálculo."""
