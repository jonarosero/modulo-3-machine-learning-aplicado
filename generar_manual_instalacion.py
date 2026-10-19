from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    PageBreak,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


OUTPUT = "Manual_Instalacion_Git_GitHub_Anaconda_OpenCode.pdf"


def register_fonts():
    regular = r"C:\Windows\Fonts\segoeui.ttf"
    bold = r"C:\Windows\Fonts\segoeuib.ttf"
    mono = r"C:\Windows\Fonts\consola.ttf"
    pdfmetrics.registerFont(TTFont("Segoe", regular))
    pdfmetrics.registerFont(TTFont("Segoe-Bold", bold))
    pdfmetrics.registerFont(TTFont("Consolas", mono))


register_fonts()

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", fontName="Segoe-Bold", fontSize=25, leading=31,
    textColor=colors.HexColor("#12304A"), alignment=TA_CENTER, spaceAfter=12,
))
styles.add(ParagraphStyle(
    name="CoverSub", fontName="Segoe", fontSize=12, leading=18,
    textColor=colors.HexColor("#40566A"), alignment=TA_CENTER, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="H1x", fontName="Segoe-Bold", fontSize=17, leading=21,
    textColor=colors.HexColor("#12304A"), spaceBefore=8, spaceAfter=9,
))
styles.add(ParagraphStyle(
    name="H2x", fontName="Segoe-Bold", fontSize=12.5, leading=16,
    textColor=colors.HexColor("#176B87"), spaceBefore=8, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="Bodyx", fontName="Segoe", fontSize=9.5, leading=14,
    textColor=colors.HexColor("#243746"), spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="Smallx", fontName="Segoe", fontSize=8, leading=11,
    textColor=colors.HexColor("#536574"), spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="CodeX", fontName="Consolas", fontSize=8.2, leading=11,
    textColor=colors.HexColor("#EAF3F7"), backColor=colors.HexColor("#172B3A"),
    borderPadding=8, leftIndent=4, rightIndent=4, spaceBefore=4, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Note", fontName="Segoe", fontSize=8.8, leading=13,
    textColor=colors.HexColor("#40566A"), backColor=colors.HexColor("#EAF5F7"),
    borderColor=colors.HexColor("#89C5D1"), borderWidth=0.5, borderPadding=7,
    spaceBefore=4, spaceAfter=8,
))


def p(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def code(text):
    return Paragraph(text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>"), styles["CodeX"])


def bullet(text):
    return Paragraph("&#8226; " + text, styles["Bodyx"])


def section(title, body):
    return [p(title, "H1x")] + body


def header_footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(colors.HexColor("#D7E4EA"))
    canvas.line(1.8 * cm, height - 1.35 * cm, width - 1.8 * cm, height - 1.35 * cm)
    canvas.setFont("Segoe", 7.5)
    canvas.setFillColor(colors.HexColor("#667985"))
    canvas.drawString(1.8 * cm, height - 1.05 * cm, "Módulo 3 · Machine Learning Aplicado")
    canvas.drawRightString(width - 1.8 * cm, 1.05 * cm, f"Página {doc.page}")
    canvas.drawString(1.8 * cm, 1.05 * cm, "Manual de instalación y puesta en marcha")
    canvas.restoreState()


doc = BaseDocTemplate(
    OUTPUT, pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm,
    topMargin=1.75 * cm, bottomMargin=1.65 * cm,
    title="Manual de instalación: Git, GitHub, Anaconda y OpenCode",
    author="Módulo 3 - Machine Learning Aplicado",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates([PageTemplate(id="all", frames=frame, onPage=header_footer)])

story = []
story += [Spacer(1, 2.2 * cm), p("Manual de instalación", "CoverTitle"),
          p("Git · GitHub · Anaconda · OpenCode", "CoverSub"),
          Spacer(1, 0.4 * cm),
          p("Guía para preparar un equipo Windows y ejecutar los notebooks del repositorio de Machine Learning Aplicado.", "CoverSub"),
          Spacer(1, 1.2 * cm)]
cover_table = Table([
    [p("Objetivo", "H2x"), p("Dejar listo un entorno reproducible para clonar el proyecto, instalar sus dependencias, trabajar con notebooks y usar OpenCode como asistente de desarrollo.", "Bodyx")],
    [p("Sistema objetivo", "H2x"), p("Windows 10/11 de 64 bits, conexión a Internet y permisos para instalar programas.", "Bodyx")],
    [p("Versión de Python", "H2x"), p("Python 3.10 o posterior, gestionado mediante Anaconda Desktop.", "Bodyx")],
], colWidths=[4.0 * cm, 11.6 * cm])
cover_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#E7F2F5")),
    ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#B7D3DC")),
    ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D3E3E8")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
]))
story.append(cover_table)
story += [Spacer(1, 1.0 * cm), p("Las direcciones web se incluyen como referencia. Descarga siempre desde los sitios oficiales y no compartas contraseñas, tokens ni datos institucionales en repositorios públicos.", "Note"), PageBreak()]

story += section("1. Qué se necesita", [
    p("Antes de instalar, comprueba que tienes al menos 10 GB libres, conexión estable y permisos de administrador. Para este proyecto se utilizarán las siguientes herramientas:", "Bodyx"),
    bullet("Git: control de versiones y clonación del repositorio."),
    bullet("GitHub: cuenta para acceder a repositorios, colaborar y respaldar el código."),
    bullet("Anaconda Distribution + Anaconda Navigator (Desktop): interfaz gráfica para gestionar entornos y aplicaciones de Python."),
    bullet("Jupyter Notebook: interfaz recomendada para abrir los notebooks."),
    bullet("OpenCode: asistente de desarrollo ejecutado desde la terminal."),
    bullet("Editor de texto: VS Code, Notepad++ u otro editor. Es opcional si se trabajará solo en Jupyter Notebook."),
    p("El repositorio ya incluye los datos locales. Los notebooks de los Días 2–7 no necesitan descargar datos desde APIs durante la ejecución.", "Note"),
])

story += section("2. Instalar Git", [
    p("1. Abre <b>https://git-scm.com/download/win</b> y descarga Git para Windows.", "Bodyx"),
    p("2. Ejecuta el instalador. Puedes mantener las opciones predeterminadas; confirma que se instale <b>Git Bash</b> y que Git quede disponible desde la línea de comandos.", "Bodyx"),
    p("3. Abre Símbolo del sistema (CMD) y verifica la instalación:", "Bodyx"),
    code("git --version"),
    p("4. Configura una identidad para que tus commits queden correctamente atribuidos. Usa el correo asociado a tu cuenta de GitHub:", "Bodyx"),
    code('git config --global user.name "Tu Nombre"\ngit config --global user.email "tu-correo@example.com"\ngit config --global init.defaultBranch main'),
    p("5. Comprueba la configuración:", "Bodyx"),
    code("git config --global --list"),
    p("Si el correo es privado en GitHub, puedes usar el correo noreply que GitHub muestra en la configuración de tu cuenta.", "Note"),
])

story += section("3. Terminal desde cero: abrirse y moverse", [
    p("En Windows 11 puedes hacer clic derecho dentro de una carpeta y elegir <b>Abrir en Terminal</b>. En Windows 10 esa opción puede no aparecer. En ese caso, abre primero una terminal y desplázate con comandos.", "Bodyx"),
    p("1. Pulsa la tecla Windows, escribe <b>cmd</b> y abre <b>Símbolo del sistema</b>. Esta guía utiliza CMD, no PowerShell.", "Bodyx"),
    p("2. Comprueba en qué carpeta estás y lista su contenido. En CMD, <b>dir</b> muestra los archivos y carpetas:", "Bodyx"),
    code("cd\ndir"),
    p("3. Ve al Escritorio. En CMD, <b>%USERPROFILE%</b> representa tu carpeta de usuario:", "Bodyx"),
    code("cd %USERPROFILE%\\Desktop\ndir"),
    p("4. Entra en una carpeta escribiendo su nombre. <b>cd</b> significa cambiar de directorio:", "Bodyx"),
    code("cd modulo-3-machine-learning-aplicado\ncd\ndir"),
    p("5. Si la carpeta tiene espacios, escribe la ruta entre comillas. Para subir un nivel usa <b>..</b>; para volver a tu carpeta de usuario usa <b>cd %USERPROFILE%</b>:", "Bodyx"),
    code('cd "C:\\Users\\TU_USUARIO\\Desktop\\modulo-3-machine-learning-aplicado"\ncd ..\ncd %USERPROFILE%'),
    p("6. Para abrir la carpeta actual en el Explorador de archivos usa <b>explorer .</b>. El punto significa la carpeta actual:", "Bodyx"),
    code("cd %USERPROFILE%\\Desktop\\modulo-3-machine-learning-aplicado\nexplorer ."),
    p("Antes de clonar o abrir Jupyter Notebook, comprueba siempre la ubicación escribiendo <b>cd</b> y revisa el contenido con <b>dir</b>.", "Note"),
])

story += section("4. Preparar GitHub", [
    p("1. Entra en <b>https://github.com</b> y crea una cuenta o inicia sesión. Activa la autenticación de dos factores.", "Bodyx"),
    p("2. Abre el repositorio del curso: <b>https://github.com/jonarosero/modulo-3-machine-learning-aplicado</b>. Pulsa el botón verde <b>Code</b>, selecciona <b>HTTPS</b> y copia la URL. No es necesario hacer Fork.", "Bodyx"),
    p("3. Descarga el repositorio clonándolo en una carpeta de trabajo. Abre CMD y ejecuta:", "Bodyx"),
    code("cd %USERPROFILE%\\Desktop\ngit clone https://github.com/jonarosero/modulo-3-machine-learning-aplicado.git\ncd modulo-3-machine-learning-aplicado"),
    p("El repositorio es público, por lo que basta con clonarlo. Si GitHub solicita autenticación, revisa que la URL esté escrita correctamente y que tengas conexión a Internet.", "Bodyx"),
    p("4. Comprueba que la descarga fue correcta:", "Bodyx"),
    code("git status\ndir\ndir notebooks\ndir datos"),
    p("Debes ver la carpeta <b>notebooks</b>, la carpeta <b>datos</b> y el archivo <b>README.md</b>. Esta carpeta descargada será la que abrirás después desde Anaconda Navigator.", "Note"),
    p("Flujo diario del estudiante:", "H2x"),
    code("cd %USERPROFILE%\\Desktop\\modulo-3-machine-learning-aplicado\ngit pull\ngit status"),
    p("Ejecuta <b>git pull</b> al comenzar cada sesión para descargar las actualizaciones del curso. En este manual no se utiliza <b>push</b> ni se solicita publicar cambios.", "Note"),
])

story += section("5. Instalar Anaconda Desktop", [
    p("Este manual utiliza <b>Anaconda Distribution</b> con <b>Anaconda Navigator</b>, su aplicación gráfica de escritorio. No se requiere Miniconda.", "Bodyx"),
    p("1. Descarga el instalador de Windows de 64 bits desde <b>https://www.anaconda.com/download</b>. Elige la distribución completa de Anaconda.", "Bodyx"),
    p("2. Ejecuta el instalador para el usuario actual. Mantén la ubicación predeterminada y permite que Anaconda aparezca en el menú Inicio. No es necesario agregar Anaconda al PATH.", "Bodyx"),
    p("3. Abre <b>Anaconda Navigator</b> desde el menú Inicio. En esta práctica se utilizará directamente el entorno <b>base (root)</b> que trae Anaconda; no crees un entorno nuevo.", "Bodyx"),
    p("4. Selecciona <b>base (root)</b> en Navigator, abre CMD o Anaconda Prompt y verifica:", "Bodyx"),
    code("conda --version\npython --version"),
    p("5. Con <b>base (root)</b> seleccionado en Navigator, instala desde Anaconda Prompt únicamente si alguna librería no está disponible:", "Bodyx"),
    code("python -m pip install --upgrade pip\npip install numpy pandas matplotlib scikit-learn scipy notebook openpyxl"),
    p("Los notebooks pueden ejecutarse con el kernel base de Anaconda. También puedes instalar <b>Jupyter Notebook</b> desde la tarjeta de aplicaciones de Navigator.", "Note"),
])

story += section("6. Abrir y ejecutar desde Anaconda Desktop", [
    p("1. Abre <b>Anaconda Navigator</b> y entra en <b>Home</b>. En el selector de entorno, elige <b>base (root)</b>.", "Bodyx"),
    p("2. En la tarjeta de <b>Jupyter Notebook</b>, pulsa <b>Launch</b>. Si no aparece, instálalo desde la tarjeta o desde Anaconda Prompt.", "Bodyx"),
    p("3. Como alternativa, abre CMD, sitúate en la carpeta raíz del repositorio y ejecuta:", "Bodyx"),
    code("cd C:\\Users\\TU_USUARIO\\Desktop\\modulo-3-machine-learning-aplicado\njupyter notebook"),
    p("Se abrirá una pestaña en el navegador. Entra en <b>notebooks/</b>, abre el notebook correspondiente y ejecuta las celdas en orden.", "Bodyx"),
    p("La estructura importante es:", "H2x"),
    code("modulo-3-machine-learning-aplicado/\n  datos/          # CSV y otros datos locales\n  notebooks/      # prácticas del Día 0 al Día 7\n  material_clase/ # presentaciones e instrumentos\n  README.md       # descripción del proyecto"),
    p("Si Jupyter no encuentra <b>datos/</b>, confirma que lo abriste desde la raíz del repositorio o inicia Jupyter con el comando ejecutado en esa carpeta.", "Note"),
])

story += section("7. Instalar y usar OpenCode", [
    p("El trabajo diario se hará en CMD. Para el instalador oficial, abre Git Bash únicamente porque el comando termina en <b>| bash</b>:", "Bodyx"),
    code("curl -fsSL https://opencode.ai/v2/install | bash"),
    p("Si el comando anterior no funciona, instala Node.js LTS desde <b>https://nodejs.org</b> y usa esta alternativa desde CMD:", "Bodyx"),
    code("npm install -g @opencode/cli"),
    p("Comprueba la instalación y abre OpenCode desde la raíz del proyecto:", "Bodyx"),
    code("opencode --version\ncd C:\\Users\\TU_USUARIO\\Desktop\\modulo-3-machine-learning-aplicado\nopencode"),
    p("Configura el proveedor de modelo siguiendo la pantalla de inicio. No pegues claves API en el código ni las guardes en Git. Si el proyecto usa variables de entorno, mantén el archivo fuera de Git.", "Bodyx"),
    p("Usa OpenCode para explicar un notebook, proponer una prueba, localizar un error o revisar un cambio. Revisa y ejecuta tú mismo cualquier código generado.", "Bodyx"),
    p("Regla de seguridad: no envíes a un proveedor externo datos confidenciales, microdatos institucionales, credenciales ni archivos con información personal.", "Note"),
])

story += section("8. OpenCode: cómo escribir instrucciones y comandos principales", [
    p("Para trabajar de forma interactiva, abre CMD en la carpeta del repositorio y ejecuta:", "Bodyx"),
    code("cd %USERPROFILE%\\Desktop\\modulo-3-machine-learning-aplicado\nopencode"),
    p("Cuando aparezca la interfaz de OpenCode, escribe tu instrucción en la zona de entrada y pulsa <b>Enter</b>. No se escribe el texto después de <b>opencode</b> dentro de la misma pantalla: primero se inicia OpenCode y después se escribe la solicitud.", "Bodyx"),
    p("Ejemplo de una buena instrucción:", "Bodyx"),
    code("Explica el notebook notebooks/00_Dia0_Fundamentos_Python_NumPy_Pandas_Matplotlib.ipynb. No modifiques archivos; indica primero qué hace cada sección."),
    p("Comandos principales dentro de la interfaz de OpenCode. Escríbelos en la caja de mensaje y pulsa <b>Enter</b>:", "H2x"),
    code("/models    # consultar o cambiar el modelo de IA\n/sessions  # ver o cambiar entre sesiones de trabajo\n/plan      # pedir un plan antes de realizar cambios\n/build     # ejecutar o continuar la implementación del plan\n/help      # mostrar la ayuda disponible\n/exit      # salir de OpenCode"),
    p("Flujo recomendado: primero usa <b>/models</b> para seleccionar el modelo; después escribe una solicitud y utiliza <b>/plan</b> para revisar los pasos. Cuando estés de acuerdo, usa <b>/build</b> para implementar. Utiliza <b>/sessions</b> para recuperar una conversación anterior.", "Bodyx"),
    p("Si un comando no aparece en tu versión, escribe <b>/help</b> dentro de OpenCode. La lista puede cambiar según la versión instalada y el proveedor configurado.", "Note"),
    p("Buenas prácticas: indica el archivo exacto, describe el objetivo, pide primero una explicación si no quieres cambios y escribe explícitamente <b>no modifiques archivos</b> cuando solo deseas analizar. Revisa cualquier propuesta antes de aceptarla.", "Bodyx"),
])

story += section("9. Comprobación final", [
    p("Ejecuta estos comandos y confirma que no aparezcan errores:", "Bodyx"),
    code("git --version\nconda --version\npython --version\npython -c \"import numpy, pandas, matplotlib, sklearn, scipy; print('Dependencias OK')\njupyter notebook --version\nnode --version\nnpm --version\nopencode --version"),
    p("Después, abre el notebook <b>notebooks/00_Dia0_Fundamentos_Python_NumPy_Pandas_Matplotlib.ipynb</b> y ejecuta una celda que importe NumPy, pandas y Matplotlib. Si termina sin errores, el entorno básico está listo.", "Bodyx"),
    p("Lista de control:", "H2x"),
    bullet("Git responde con una versión y tiene nombre/correo configurados."),
    bullet("El repositorio está clonado y <b>git status</b> funciona."),
    bullet("Anaconda Navigator está usando el entorno <b>base (root)</b>."),
    bullet("Jupyter Notebook abre los notebooks con el kernel correcto."),
    bullet("Las dependencias importan sin errores."),
    bullet("OpenCode responde con una versión y se ejecuta desde la carpeta del proyecto."),
])

story += section("10. Problemas frecuentes", [
    p("<b>Anaconda Navigator no abre:</b> reinicia el equipo y vuelve a abrirlo desde el menú Inicio. Si persiste, usa la terminal integrada de Navigator para comprobar el entorno.", "Bodyx"),
    p("<b>bash no se reconoce, 1:</b> abre <b>Git Bash</b> desde el menú Inicio; el instalador de OpenCode requiere Bash.", "Bodyx"),
    p("<b>bash no se reconoce, 2:</b> si Git no está instalado, descarga Git for Windows desde <b>https://git-scm.com/download/win</b> y vuelve a abrir Git Bash.", "Bodyx"),
    p("<b>bash no se reconoce, 3:</b> cierra todas las terminales y abre una nueva; las variables PATH no se actualizan en ventanas ya abiertas.", "Bodyx"),
    p("<b>bash no se reconoce, 4:</b> busca <b>Git Bash</b> en el menú Inicio; no escribas el comando en una ventana de Python ni en Anaconda Navigator Home.", "Bodyx"),
    p("<b>bash no se reconoce, 5:</b> ejecuta el comando desde Git Bash y no desde el Símbolo del sistema clásico (<b>cmd</b>).", "Bodyx"),
    p("<b>bash no se reconoce, 6:</b> en Git Bash ejecuta <b>which bash</b>; debe mostrar una ruta similar a <b>/usr/bin/bash</b>.", "Bodyx"),
    p("<b>bash no se reconoce, 7:</b> en Git Bash ejecuta <b>which curl</b>; si no aparece una ruta, actualiza o reinstala Git for Windows.", "Bodyx"),
    p("<b>bash no se reconoce, 8:</b> reinicia Windows y prueba de nuevo Git Bash desde el menú Inicio.", "Bodyx"),
    p("<b>bash no se reconoce, 9:</b> si el script sigue fallando, instala Node.js LTS y usa <b>npm install -g @opencode/cli</b> desde CMD o Anaconda Prompt.", "Bodyx"),
    p("<b>bash no se reconoce, 10:</b> después de instalar por npm, abre otra terminal y ejecuta <b>opencode --version</b>. Si no aparece, revisa <b>npm prefix -g</b> y agrega esa carpeta al PATH.", "Bodyx"),
    p("<b>ModuleNotFoundError:</b> instala la librería faltante en el entorno base con <b>python -m pip install paquete</b> y comprueba el kernel seleccionado en Jupyter.", "Bodyx"),
    p("<b>El notebook no encuentra datos:</b> inicia Jupyter desde la raíz de <b>modulo-3-machine-learning-aplicado</b> y revisa que exista la carpeta <b>datos</b>.", "Bodyx"),
    p("<b>git pull falla:</b> verifica que estás dentro de la carpeta del repositorio escribiendo <b>cd</b> y que tienes conexión a Internet.", "Bodyx"),
    p("<b>Falla la instalación por red o proxy:</b> prueba otra conexión, revisa la configuración corporativa y evita descargar instaladores desde sitios no oficiales.", "Bodyx"),
])

story += section("11. Instrucciones para un agente que ayude al usuario", [
    p("Esta sección está dirigida a un agente de IA que reciba este PDF y deba acompañar al usuario durante toda la instalación. El agente debe explicar cada paso con lenguaje sencillo, confirmar el resultado antes de avanzar y ofrecer ayuda paso a paso, especialmente en GitHub y en el uso de la terminal.", "Bodyx"),
    p("<b>Objetivo final:</b> dejar instalado Git, descargar el repositorio del curso, preparar Anaconda Desktop usando el entorno <b>base (root)</b>, abrir los notebooks con Jupyter Notebook e instalar OpenCode. El usuario trabajará principalmente con CMD.", "Note"),
    p("<b>Orden que debe seguir el agente:</b>", "H2x"),
    bullet("Preguntar primero qué versión de Windows utiliza, si tiene permisos para instalar programas y si ya tiene Git, Anaconda o Node.js instalados."),
    bullet("Preguntar si el usuario quiere una explicación completa o acompañamiento paso a paso, esperando su confirmación después de cada bloque."),
    bullet("Explicar cómo abrir CMD: tecla Windows, escribir <b>cmd</b> y abrir Símbolo del sistema."),
    bullet("Instalar Git for Windows y confirmar que Git Bash también quedó instalado. Usar CMD para el trabajo normal; Git Bash se usa únicamente para el instalador de OpenCode que termina en <b>| bash</b>."),
    bullet("Configurar Git con el nombre y correo del usuario, sin pedir ni almacenar contraseñas."),
    bullet("Abrir GitHub y explicar que basta con clonar el repositorio público; no pedir al usuario que haga Fork, commit ni push."),
    bullet("Clonar exactamente <b>https://github.com/jonarosero/modulo-3-machine-learning-aplicado.git</b> en el Escritorio mediante CMD."),
    bullet("Comprobar con <b>dir</b> que existen <b>notebooks</b>, <b>datos</b>, <b>material_clase</b> y <b>README.md</b>."),
    bullet("Explicar que el repositorio contiene notebooks de los Días 0 a 7, datos locales, material de clase y documentación del módulo."),
    bullet("Instalar Anaconda Distribution y abrir Anaconda Navigator. No crear entornos nuevos: utilizar siempre <b>base (root)</b>."),
    bullet("Instalar las dependencias en base solo si hacen falta: NumPy, pandas, Matplotlib, scikit-learn, SciPy, Notebook y openpyxl."),
    bullet("Abrir Jupyter Notebook desde Anaconda Navigator o ejecutar <b>jupyter notebook</b> desde CMD ubicado en la carpeta del repositorio."),
    bullet("Instalar OpenCode con <b>curl -fsSL https://opencode.ai/v2/install | bash</b> desde Git Bash. Si falla, usar Node.js y <b>npm install -g @opencode/cli</b> desde CMD."),
    bullet("Abrir OpenCode desde la carpeta del repositorio y enseñar `/models`, `/sessions`, `/plan`, `/build`, `/help` y `/exit`."),
    p("<b>Regla de actualización diaria:</b> al comenzar cada sesión, el agente debe llevar al usuario a la carpeta del repositorio y ejecutar por él <b>git pull</b> desde CMD. Debe comprobar el resultado y avisar si hay conflictos o cambios locales. El agente no debe ejecutar <b>git push</b> ni enseñar un flujo de publicación para este curso.", "Note"),
    p("<b>Preguntas que debe hacer al usuario:</b>", "H2x"),
    bullet("¿Qué versión de Windows tienes: Windows 10 o Windows 11?"),
    bullet("¿Puedes abrir CMD escribiendo `cmd` en el menú Inicio?"),
    bullet("¿Ya tienes Git instalado? ¿Qué resultado aparece con `git --version`?"),
    bullet("¿Ya tienes Anaconda Navigator instalado y puedes abrirlo?"),
    bullet("¿El repositorio se clonó correctamente y puedes ver las carpetas `notebooks` y `datos`?"),
    bullet("¿Quieres que te acompañe paso a paso o prefieres ejecutar todos los comandos de una vez?"),
    bullet("¿Tienes alguna duda sobre GitHub, la terminal, Anaconda, Jupyter Notebook u OpenCode?"),
    p("<b>Forma de explicar el repositorio:</b> el agente debe decir que <b>notebooks/</b> contiene las prácticas de clase; <b>datos/</b> contiene los archivos CSV y otros datos locales; <b>material_clase/</b> contiene presentaciones e instrumentos; <b>material_apoyo/</b> contiene imágenes de apoyo; y <b>README.md</b> describe la organización, ejecución, datos y criterios del módulo. Debe aclarar que los notebooks se ejecutan desde la raíz del repositorio para que encuentren la carpeta `datos`.", "Bodyx"),
    p("<b>Seguridad:</b> el agente nunca debe pedir contraseñas, tokens, claves API ni datos confidenciales. Antes de ejecutar una acción que modifique archivos, debe explicarla y pedir confirmación. Si el usuario se confunde, debe detenerse, explicar el paso actual y preguntar si desea continuar.", "Note"),
])

story += [Spacer(1, 0.4 * cm), p("Referencias oficiales", "H1x"),
          p("Git: https://git-scm.com/book/es/v2 · GitHub: https://docs.github.com/es · Conda: https://docs.conda.io · Anaconda: https://www.anaconda.com/download · Jupyter: https://jupyter.org · OpenCode: https://opencode.ai", "Smallx"),
          p("Documento preparado para el repositorio modulo3_ml. Verifica las instrucciones y versiones oficiales antes de una instalación nueva, ya que pueden cambiar.", "Smallx")]

doc.build(story)
print(OUTPUT)
