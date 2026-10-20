# Capturas de pantalla

Lista de las capturas que acompañan cada guía. Guardar en esta carpeta con el nombre exacto para que los enlaces funcionen.

**Recomendaciones**

- Usar `Win + Shift + S` (Recorte de pantalla) y capturar solo la ventana relevante, no la pantalla completa.
- Resaltar el dato importante con un recuadro rojo (la herramienta Recortes lo permite).
- **Ocultar datos sensibles:** nombre de usuario, nombre del equipo, IP pública, correos. Basta un recuadro negro encima.
- Formato PNG, ancho máximo de 1200 px.

## 01. Conectado, sin internet

| Archivo | Qué debe mostrar |
| --- | --- |
| `01-icono-red.png` | Ícono de red en la barra de tareas con el aviso "Sin internet" |
| `01-ipconfig.png` | Resultado de `ipconfig /all` con IPv4, puerta de enlace y DNS resaltados |
| `01-ncpa.png` | Ventana de Conexiones de red (`ncpa.cpl`) con el menú Deshabilitar / Habilitar |

## 02. Equipo lento, disco al 100 %

| Archivo | Qué debe mostrar |
| --- | --- |
| `02-administrador-tareas.png` | Pestaña Procesos ordenada por la columna Disco |
| `02-inicio.png` | Pestaña Aplicaciones de inicio con la columna Impacto de inicio |
| `02-get-physicaldisk.png` | Resultado de `Get-PhysicalDisk` en PowerShell |

## 03. Impresora con cola atascada

| Archivo | Qué debe mostrar |
| --- | --- |
| `03-cola.png` | Ventana de la cola de impresión con un trabajo en estado Error |
| `03-spooler.png` | Resultado de `net stop spooler` y `net start spooler` |

## 04. Diadema sin micrófono

| Archivo | Qué debe mostrar |
| --- | --- |
| `04-mmsys-grabacion.png` | Pestaña Grabación de `mmsys.cpl` con la barra de nivel de la diadema activa |
| `04-privacidad.png` | Configuración > Privacidad > Micrófono con las tres opciones activadas |
