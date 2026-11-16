"""reportes.py - Reportes diarios (RF11)."""
import pagos


def reporte_diario():
    tickets = pagos.pagos
    return {
        "raciones_servidas": sum(1 for t in tickets if t["usado"]),
        "ingresos": sum(t["monto"] for t in tickets),
        "tickets_emitidos": len(tickets),
    }


if __name__ == "__main__":
    pagos.registrar_pago("182189", es_becario=False)
    print(reporte_diario())
