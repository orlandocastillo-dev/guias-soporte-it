# Documentación de soporte técnico (IT Support)

Guías de solución de problemas para usuarios de Windows en un entorno de oficina o centro de contacto. Están escritas para que otro técnico de primer nivel pueda seguirlas sin ayuda y para que el caso quede bien registrado en el ticket.

**Estas guías son la base de conocimiento de [MesaTI](https://github.com/orlandocastillo-dev/mesa-ti)**, la mesa de ayuda: allí se le sugieren al empleado mientras reporta el problema y al técnico dentro de cada ticket. Pruébalo en https://mesa-ti-chi.vercel.app/#/guias. Este repositorio es la fuente en Markdown, con los scripts de PowerShell y un visor que funciona sin internet.

## Cómo verlas

- **En tu computador:** abre `ver-guias.html` con doble clic. Es un visor con todas las guías, los diagramas y los scripts, sin instalar nada.
- **En GitHub:** los archivos `.md` se ven formateados directamente en el repositorio.
- **En VS Code:** abre cualquier `.md` y presiona `Ctrl + Shift + V` para ver la vista previa.

Si editas una guía, regenera el visor con `pip install markdown` y luego `python generar-visor.py`.

## Guías

| # | Problema | Categoría | Tiempo |
| --- | --- | --- | --- |
| 01 | [Wi-Fi o cable "Conectado, sin internet"](guias/01-conectado-sin-internet.md) | Red | 10 a 20 min |
| 02 | [Equipo lento al iniciar y disco al 100 %](guias/02-equipo-lento-disco-al-100.md) | Rendimiento / hardware | 30 a 60 min |
| 03 | [La impresora no imprime: cola atascada](guias/03-impresora-cola-atascada.md) | Periféricos | 5 a 15 min |
| 04 | [Diadema sin micrófono en el softphone](guias/04-diadema-sin-microfono-softphone.md) | Audio / telefonía | 5 a 15 min |

## Scripts de apoyo (PowerShell)

| Script | Para qué sirve | Administrador |
| --- | --- | --- |
| [`diagnostico-red.ps1`](scripts/diagnostico-red.ps1) | Revisa IP, puerta de enlace, DNS, salida a internet y proxy. Guarda un informe en el escritorio para adjuntarlo al ticket. Con `-Reparar` vacía la caché DNS y renueva la IP. | Solo con `-Reparar` |
| [`limpiar-cola-impresion.ps1`](scripts/limpiar-cola-impresion.ps1) | Detiene el Spooler, borra los trabajos atascados y lo vuelve a iniciar. | Sí |
| [`info-equipo.ps1`](scripts/info-equipo.ps1) | Ficha técnica del equipo (modelo, serie, SO, RAM, discos con su salud, red) con avisos automáticos. Exporta a JSON o CSV. | No |

Para ejecutarlos en un equipo con la política de ejecución restringida, sin cambiarla de forma permanente:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\diagnostico-red.ps1
```

## Cómo están escritas

Todas las guías siguen la misma [plantilla](plantilla-guia.md), pensada para el trabajo real de una mesa de ayuda:

1. **Ficha inicial:** a qué aplica, nivel de soporte, tiempo estimado, riesgo y permisos necesarios. El técnico sabe antes de empezar si puede hacerlo él o debe escalar.
2. **Síntoma** descrito como lo reporta el usuario, no como lo nombraría un técnico.
3. **Causas más comunes**, de la más probable a la menos probable.
4. **Diagrama de diagnóstico** para descartar primero lo que no es del equipo (la red, la impresora, la diadema) antes de tocar la configuración.
5. **Pasos numerados** con el comando exacto y el resultado esperado.
6. **Lista de verificación** para confirmar con el usuario antes de cerrar.
7. **Criterio de escalamiento** con la información que necesita el siguiente nivel.
8. **Nota para el ticket** lista para copiar, con síntoma, diagnóstico, acciones y resultado.

Los diagramas usan [Mermaid](https://mermaid.js.org/), que GitHub muestra como imagen directamente.

## Capturas de pantalla

Cada guía indica qué captura va en cada paso (`Captura sugerida: capturas/...`). La lista completa con los nombres de archivo está en [`capturas/README.md`](capturas/README.md).

## Buenas prácticas que aplico

- **Preguntar antes de tocar.** "¿A tus compañeros les pasa?" ahorra la mitad de los diagnósticos.
- **Un cambio a la vez** y probar después de cada uno, para saber qué lo arregló.
- **Avisar antes de cualquier paso con impacto** (reinicios, trabajos de impresión que se pierden).
- **El usuario confirma el cierre**, no el técnico.
- **Documentar aunque se haya resuelto rápido.** Los casos repetidos son los que justifican un cambio de fondo (una IP fija para la impresora, un SSD para el equipo lento).

---

Orlando Castillo, estudiante de Ingeniería de Sistemas.
