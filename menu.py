"""menu.py - Menú del día y semanal (RF3)."""
from config import NOMBRE_COMEDOR

menus = {}  # fecha (str) -> lista de platos


def publicar_menu(fecha, platos):
    """Publica el menú de una fecha."""
    menus[fecha] = list(platos)


def menu_del_dia(fecha):
    return menus.get(fecha, [])


def menu_semanal(fechas):
    return {f: menu_del_dia(f) for f in fechas}


if __name__ == "__main__":
    publicar_menu("2026-11-16", ["Sopa de quinua", "Seco de pollo", "Mazamorra"])
    print(NOMBRE_COMEDOR)
    print("Menú del día:", menu_del_dia("2026-11-16"))
