# Guías de soporte técnico

Guías para resolver los problemas más comunes en equipos con Windows en una oficina o un centro de llamadas. Las escribí para que otro técnico de primer nivel las pueda seguir sin ayuda y para que el caso quede bien anotado en el ticket.

Estas guías son la base de conocimiento de [MesaTI](https://github.com/orlandocastillo-dev/mesa-ti): allá se le sugieren al empleado mientras reporta el problema y al técnico dentro de cada ticket. Se pueden ver en https://mesa-ti-chi.vercel.app/#/guias.

## Verlas

- Con doble clic en `ver-guias.html`: tiene todas las guías, los diagramas y los scripts, sin internet.
- En GitHub, abriendo cualquier `.md`.

Si cambias una guía, regenera el visor con `pip install markdown` y `python generar-visor.py`.

## Las guías

1. [Wi-Fi o cable "Conectado, sin internet"](guias/01-conectado-sin-internet.md)
2. [Equipo lento al iniciar y disco al 100 %](guias/02-equipo-lento-disco-al-100.md)
3. [La impresora no imprime: cola atascada](guias/03-impresora-cola-atascada.md)
4. [Diadema sin micrófono en el softphone](guias/04-diadema-sin-microfono-softphone.md)

Todas siguen la misma [plantilla](plantilla-guia.md): a qué aplica y cuánto tarda, el síntoma como lo cuenta el usuario, las causas más comunes, un diagrama para descartar primero lo que no es del equipo, los pasos con el comando exacto, qué confirmar antes de cerrar, cuándo escalar y una nota lista para copiar en el ticket.

## Scripts de PowerShell

- [`diagnostico-red.ps1`](scripts/diagnostico-red.ps1): revisa IP, puerta de enlace, DNS, salida a internet y proxy, y guarda un informe en el escritorio. Con `-Reparar` vacía la caché DNS y renueva la IP (pide administrador).
- [`limpiar-cola-impresion.ps1`](scripts/limpiar-cola-impresion.ps1): detiene el Spooler, borra los trabajos atascados y lo vuelve a iniciar (pide administrador).
- [`info-equipo.ps1`](scripts/info-equipo.ps1): ficha del equipo (modelo, serie, sistema, RAM, discos y red), con opción de exportar a JSON o CSV.

Si la política de ejecución está restringida:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\diagnostico-red.ps1
```

## Lo que he aprendido haciendo soporte

- Preguntar antes de tocar: "¿a tus compañeros también les pasa?" ahorra la mitad del diagnóstico.
- Cambiar una cosa a la vez y probar, para saber qué lo arregló.
- Avisar antes de reiniciar o de borrar trabajos de impresión.
- El que confirma que quedó resuelto es el usuario.
- Anotar el caso aunque se haya resuelto rápido, porque los que se repiten son los que justifican un cambio de fondo.

Las capturas que van en cada paso están listadas en [`capturas/README.md`](capturas/README.md).
