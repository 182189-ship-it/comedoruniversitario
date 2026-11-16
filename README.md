# Comedor Universitario – UNAMBA

Sistema de gestión del comedor universitario (Ingeniería de Software I, Escuela Profesional de Ingeniería Informática y Sistemas, UNAMBA).
Proyecto de práctica de **control de versiones con Git, GitHub y P4Merge**.

## Equipo y roles

| Colaborador | Rol | Responsabilidad |
| --- | --- | --- |
| master | Dueño del repositorio e integrador | Crea el repositorio, integra las ramas, resuelve el conflicto con P4Merge y publica las versiones |
| nombre | Desarrollador 1 | Menú del día y pagos |
| test | Desarrollador 2 | Reservas y aforo |

## Plan de versiones

| Versión | Contenido | Rama | Desarrolla |
| --- | --- | --- | --- |
| v1.0 | Estructura base, README, requisitos y `config.py` | main | master |
| v2.0 | Menú del día (RF3) | feature-menu | nombre |
| v3.0 | Reservas y control de aforo (RF4, RF5) | feature-reservas | test |
| v4.0 | Pagos y ticket (RF6, RF7) | feature-pagos | nombre |
| v5.0 | Reportes diarios (RF11) | feature-reportes | master |

## Estructura

```
comedor-universitario/
├── README.md
├── requisitos.md
├── config.py      # parámetros generales
├── menu.py        # RF3
├── reservas.py    # RF4, RF5
├── pagos.py       # RF6, RF7
└── reportes.py    # RF11
```

## Flujo de trabajo

- Rama principal: `main`. Cada módulo se desarrolla en `feature-<módulo>`.
- Solo master integra a `main` (`git merge origin/feature-<módulo>`) y publica la etiqueta de versión.
- Los conflictos se resuelven con `git mergetool` (P4Merge).

## Ejecución

Requiere Python 3.8 o superior.

```
python menu.py
python reservas.py
python pagos.py
python reportes.py
```
