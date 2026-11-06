"""Registro de eventos y errores."""
import logging
from pathlib import Path

def obtener_logger():
    logger = logging.getLogger("SoftwareFJ")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formato = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        destino = Path(__file__).resolve().parent.parent / "software_fj.log"
        archivo = logging.FileHandler(destino, encoding="utf-8")
        archivo.setFormatter(formato)
        consola = logging.StreamHandler()
        consola.setFormatter(formato)
        logger.addHandler(archivo)
        logger.addHandler(consola)
    return logger
