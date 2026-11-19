"""Registro de eventos y errores."""  # Docstring del módulo: describe para qué sirve este archivo
import logging  # Módulo estándar de Python para registrar mensajes (logs)
from pathlib import Path  # Permite manejar rutas de archivos sin importar el sistema operativo


def obtener_logger():  # Función que crea (o recupera) el logger único del sistema
    # Obtiene el logger llamado "SoftwareFJ"; si ya existe, devuelve el mismo objeto
    logger = logging.getLogger("SoftwareFJ")
    # Solo configura los handlers la primera vez; evita mensajes duplicados en cada llamada
    if not logger.handlers:
        # Registra mensajes de nivel INFO o superior (INFO, WARNING, ERROR, CRITICAL)
        logger.setLevel(logging.INFO)
        # Define cómo se ve cada línea: fecha y hora | nivel | mensaje
        formato = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        # Ruta del archivo de log: sube dos carpetas desde src/logs.py hasta la raíz del proyecto
        destino = Path(__file__).resolve().parent.parent / "software_fj.log"
        # Handler que escribe los mensajes en el archivo, con codificación UTF-8 para tildes y ñ
        archivo = logging.FileHandler(destino, encoding="utf-8")
        # Aplica el formato definido al handler del archivo
        archivo.setFormatter(formato)
        # Handler que muestra los mensajes en la consola (terminal)
        consola = logging.StreamHandler()
        # Aplica el mismo formato a la consola
        consola.setFormatter(formato)
        # Conecta el handler del archivo al logger
        logger.addHandler(archivo)
        # Conecta el handler de la consola al logger
        logger.addHandler(consola)
    # Devuelve el logger listo para usar en los demás módulos
    return logger