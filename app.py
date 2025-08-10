# Importamos las clases necesarias de Flask:
# - Flask: Para crear la aplicación web
# - render_template: 
# Para renderizar archivos HTML desde la carpeta 'templates'
from flask import Flask, render_template

# Creamos una instancia de la aplicación Flask.
# __name__ es una variable especial que le dice a Flask 
# dónde buscar recursos (plantillas, archivos estáticos, etc.)
app = Flask(__name__)

# lista de proyectos
proyectos = [
    {
        "nombre": "Sistema ded gestion de materiales TovWareMen",
        "descripcion": "Sistema web desarrollado con Symfony y MySQL para asociaciones, con filtros dinámicos y exportación a Excel.",
        "tecnologias": "Symfony, PHP, MySQL",
        "link": "https://tovwaremen.com.co/",
    },
    {
        "nombre": "pagina web WORK AND TRAVEL",
        "descripcion": "trabajar con jóvenes de bajos recursos para ampliar sus oportunidades laborales y académicas mediante el intercambio cultural en el exterior.",
        "tecnologias": "Symfony, PHP",
        "link": "https://workandtravelaupair.org",
    },
    {
        "nombre": "Mi portafolio",
        "descripcion": "creacion de mi primer portafolio con mi experiencia como desarrollador.",
        "tecnologias": "python, flask",
        "link": "https://github.com/fabioleyton/mi-portafolio-F-L.git",
    },
    {
        "nombre": "divicion de numeros para planillas",
        "descripcion": "el objetivo es dividir los numeros en partes desiguales pero que la suma de el mismo numero total",
        "tecnologias": "php, html, css, JS",
        "link": "https://github.com/fabioleyton/divicion_nu_planilla.git",
    },
    {
        "nombre": "peticiones",
        "descripcion": "se crea una lista de peticiones con un contador de fecha para tener el control de las peticiones y terminan automaticamente despues de un tiempo determinado",
        "tecnologias": "php, html, css",
        "link": "https://github.com/fabioleyton/peticiones.git",
    },
    {
        "nombre": "lector de archivos ESCEL",
        "descripcion": "lector de archivos EXCEL, se refleja sin formato en pantalla",
        "tecnologias": "php, html, css",
        "link": "https://github.com/fabioleyton/lector_excel.git",
    },
    {
        "nombre": "proyecto SENA",
        "descripcion": "proyecto de inventarios donde se puede ingresar, productos, personas y usuarios para el control de inventarios de los almacenes",
        "tecnologias": "php, html, css, js",
        "link": "https://github.com/yerermid/inventarios.git",
    },
    {
        "nombre": "PAGINA VENTA DE VINOS",
        "descripcion": "pagina web de vinos",
        "tecnologias": "html, css",
        "link": "https://github.com/fabioleyton/vinos-leyton.git",
    },
]

# Definimos una ruta (endpoint) para la URL principal ("/").
# Cuando un usuario visite la raíz del sitio, 
# se ejecutará esta función.
@app.route("/")
def home():
    # Renderizamos y devolvemos la plantilla 'index.html' 
    # que debe estar en la carpeta 'templates'
    return render_template("index.html", proyecto=proyectos)

@app.route("/gracias")
def gracias():
    return render_template("gracias.html")

@app.route("/hoja_de_vida")
def hojaDeVida():
    return render_template ("hoja_de_vida.html")

# Este bloque verifica si el script se está ejecutando directamente 
# (no importado como módulo)
if __name__ == "__main__":
    # Iniciamos el servidor web de Flask:
    # - debug=True: Habilita el modo depuración 
    # (muestra errores detallados, reinicia el servidor al hacer cambios)
    # - Por defecto, el servidor se ejecuta en http://127.0.0.1:5000/
    app.run(debug=True)


