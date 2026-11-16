"""pagos.py - Tarifa, pago y ticket (RF6, RF7)."""
import uuid
from config import PRECIO_RACION

pagos = []


def calcular_tarifa(es_becario):
    """Becarios no pagan; ajustar según la política del comedor."""
    return 0.0 if es_becario else PRECIO_RACION


def registrar_pago(codigo_estudiante, es_becario):
    """Registra el pago y devuelve el ticket."""
    ticket = {
        "codigo_estudiante": codigo_estudiante,
        "monto": calcular_tarifa(es_becario),
        "qr": uuid.uuid4().hex,  # contenido que se codificará en el código QR
        "usado": False,
    }
    pagos.append(ticket)
    return ticket


if __name__ == "__main__":
    print(registrar_pago("182189", es_becario=False))
