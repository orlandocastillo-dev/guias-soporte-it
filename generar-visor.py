"""
Genera ver-guias.html: un visor de una sola página con todas las guías y scripts.

Se abre con doble clic, sin servidor. Volver a ejecutar después de editar cualquier guía:

    pip install markdown
    python generar-visor.py
"""
import html
import json
import re
from pathlib import Path

import markdown

RAIZ = Path(__file__).parent


def md_a_html(texto: str) -> str:
    # Los bloques mermaid se convierten en <div class="mermaid"> para que los dibuje mermaid.js.
    texto = re.sub(
        r"```mermaid\n(.*?)```",
        lambda m: f'<div class="mermaid">{html.escape(m.group(1))}</div>',
        texto,
        flags=re.S,
    )
    cuerpo = markdown.markdown(texto, extensions=["tables", "fenced_code"])
    # Los enlaces entre archivos .md apuntan a la sección del visor.
    cuerpo = re.sub(r'href="(?:\.\./)?(?:guias/)?([\w-]+)\.md"', r'href="#\1"', cuerpo)
    cuerpo = re.sub(r'href="(?:\.\./)?scripts/([\w-]+)\.ps1"', r'href="#\1"', cuerpo)
    # Las casillas "- [ ]" se muestran como checkbox.
    cuerpo = cuerpo.replace("<li>[ ] ", '<li class="check"><input type="checkbox"> ')
    return cuerpo


paginas = [{"id": "inicio", "titulo": "Inicio", "grupo": "", "html": md_a_html((RAIZ / "README.md").read_text("utf-8"))}]

for archivo in sorted((RAIZ / "guias").glob("*.md")):
    texto = archivo.read_text("utf-8")
    titulo = texto.splitlines()[0].lstrip("# ").strip()
    paginas.append({"id": archivo.stem, "titulo": titulo, "grupo": "Guías", "html": md_a_html(texto)})

for archivo in sorted((RAIZ / "scripts").glob("*.ps1")):
    codigo = archivo.read_text("utf-8-sig")
    contenido = (
        f"<h1>{archivo.name}</h1>"
        f'<p>Script de PowerShell. Para ejecutarlo: <code>powershell -ExecutionPolicy Bypass -File .\\scripts\\{archivo.name}</code></p>'
        f'<pre><code>{html.escape(codigo)}</code></pre>'
    )
    paginas.append({"id": archivo.stem, "titulo": archivo.name, "grupo": "Scripts", "html": contenido})

paginas.append({
    "id": "plantilla-guia",
    "titulo": "Plantilla para nuevas guías",
    "grupo": "Recursos",
    "html": md_a_html((RAIZ / "plantilla-guia.md").read_text("utf-8")),
})

plantilla = (RAIZ / "visor-plantilla.html").read_text("utf-8")
salida = plantilla.replace("/*__PAGINAS__*/[]", json.dumps(paginas, ensure_ascii=False).replace("</", "<\\/"))
(RAIZ / "ver-guias.html").write_text(salida, "utf-8")
print(f"ver-guias.html generado con {len(paginas)} páginas.")
