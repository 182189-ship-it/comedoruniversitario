"""reservas.py - Reservas y control de aforo (RF4, RF5)."""
from config import AFORO_MAXIMO

reservas = {}  # turno -> lista de códigos de estudiante


def reservar(turno, codigo_estudiante):
    """Reserva una ración en un turno. Devuelve False si el aforo está completo."""
    lista = reservas.setdefault(turno, [])
    if codigo_estudiante in lista:
        return True
    if len(lista) >= AFORO_MAXIMO:
        return False
    lista.append(codigo_estudiante)
    return True


def cupos_disponibles(turno):
    return AFORO_MAXIMO - len(reservas.get(turno, []))


if __name__ == "__main__":
    print(reservar("12:00", "182189"))
    print("Cupos disponibles:", cupos_disponibles("12:00"))
