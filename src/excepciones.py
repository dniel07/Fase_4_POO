"""
Módulo: excepciones.py
Descripción: Define las excepciones personalizadas utilizadas
para controlar errores en el sistema Software FJ.
"""

class SoftwareFJError(Exception):
    """Excepción base de la aplicación."""
    pass

class ValidacionError(SoftwareFJError):
    """Error general relacionado con datos inválidos."""
    pass

class ClienteInvalidoError(ValidacionError):
    """Error producido por datos incorrectos de clientes."""
    pass

class ServicioInvalidoError(ValidacionError):
    """Error producido por datos incorrectos de servicios."""
    pass

class ReservaError(SoftwareFJError):
    """Error general relacionado con las reservas."""
    pass

class EstadoReservaError(ReservaError):
    """Error por intentar una transición de estado no permitida."""
    pass

class RecursoNoDisponibleError(ReservaError):
    """Error cuando un servicio o recurso no está disponible."""
    pass

class CalculoCostoError(SoftwareFJError):
    """Error producido durante la validación de costos."""
    pass
