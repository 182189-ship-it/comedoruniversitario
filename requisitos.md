# Requisitos del sistema

## Requerimientos funcionales

| ID | Requerimiento | Prioridad |
| --- | --- | --- |
| RF1 | Registrar e iniciar sesión de estudiantes | Alta |
| RF2 | Gestionar beneficiarios, distinguiendo becarios y no becarios | Alta |
| RF3 | Publicar el menú diario y semanal | Alta |
| RF4 | Reservar una ración en un turno y horario | Alta |
| RF5 | Controlar el aforo máximo por turno | Alta |
| RF6 | Calcular la tarifa según la configuración del usuario y registrar el pago | Alta |
| RF7 | Emitir un ticket con código QR | Mediana |
| RF8 | Validar el ingreso (QR o código de estudiante) y marcar el ticket como usado | Alta |
| RF9 | Cancelar o reprogramar una reserva con anticipación mínima | Mediana |
| RF10 | Gestionar el inventario de insumos y alertar sobre stock mínimo | Mediana |
| RF11 | Generar reportes de raciones servidas, ingresos, asistencia y merma | Mediana |
| RF12 | Enviar notificaciones sobre el menú y los cambios | Baja |
| RF13 | Registrar sugerencias, quejas y encuestas de satisfacción | Baja |

## Requerimientos no funcionales

| ID | Categoría | Requerimiento |
| --- | --- | --- |
| RNF1 | Rendimiento | Respuesta en 2 segundos o menos con 500 usuarios simultáneos en hora pico |
| RNF2 | Disponibilidad | 99 % durante el horario de atención |
| RNF3 | Seguridad | Contraseña cifrada, control de acceso por roles y conexión HTTPS |
| RNF4 | Usabilidad | Interfaz simple y adaptable a celular, que se aprenda en 10 minutos |
| RNF5 | Escalabilidad | Soporte para más turnos |
| RNF6 | Mantenibilidad | Código modular, pruebas unitarias y control de versiones con Git |
| RNF7 | Compatibilidad | Navegadores actuales, Android e iOS |
| RNF8 | Integridad | Copia de seguridad diaria de la base de datos |
| RNF9 | Privacidad | Cumplir la Ley de Protección de Datos Personales (Ley 29733) |
