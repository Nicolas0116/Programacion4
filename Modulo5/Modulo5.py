from flask import Flask, render_template, request
import redis
app = Flask(__name__)

r = redis.Redis(host="localhost")

r.flushall()
r.set("MOPRI","Se refiere al hijo del tío de una persona o  también describe a un amigo")
pa = "palabra"
si = "significado"


def existe(valor):
    val = False
    if r.exists(valor.upper()):
        val = True
    return val

def agregar_palabra(palabra, significado):
    r.set(palabra.upper(), significado)

def editar_palabra(palabra, newpalabra):
    r.rename(palabra.upper(), newpalabra.upper())

def editar_significado(palabra, newsignificado):
    r.set(palabra.upper(),newsignificado)

def eliminar_palabra(palabra):
    r.delete(palabra.upper())

def obtener_palabras():
    y = r.keys()
    palabras = []
    for i in y:
        palabras.append({"nombre": i.decode("utf-8")})
    return palabras

def significado_palabra(palabra):
    significados = []
    significados.append({"significado":r.get(palabra.upper()).decode("utf-8")})
    return significados


@app.route('/', methods=['GET', 'POST'])
def index():
    obtenerP = obtener_palabras()
    return render_template("index_m5.html", palabras=obtenerP)


@app.route('/agregar_palabra', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        palabra = request.form['pa']
        significado = request.form['si']
        if existe(palabra) == True:
            return render_template("agregar_m5.html", message=False)
        else:
            agregar_palabra(palabra.upper(), significado)
            return render_template("agregar_m5.html", message=True)

    return render_template("agregar_m5.html")


@app.route('/editar_palabra', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        palabra = request.form["vpa"]
        new = request.form["pa"]
        if existe(palabra):
            editar_palabra(palabra, new)
            return render_template("editar_m5.html", message=False)
        else:

            return render_template("editar_m5.html", message=True)
    return render_template("editar_m5.html")

@app.route('/editar_significado', methods=['GET', 'POST'])
def editar_sig():
    if request.method == 'POST':
        palabra = request.form["vpa"]
        news = request.form["si"]
        if existe(palabra):
            editar_significado(palabra, news)
            return render_template("editar_significado_m5.html", message=False)
        else:
            return render_template("editar_significado_m5.html", message=True)
    return render_template("editar_significado_m5.html")


@app.route('/eliminar_palabra', methods=['GET', 'POST'])
def eliminar():
    if request.method == 'POST':
        palabra = request.form['pa']
        if existe(palabra):
            eliminar_palabra(palabra)
            obtener_palabras()
            return render_template("eliminar_m5.html", message=False)
        else:
            obtener_palabras()
            return render_template("eliminar_m5.html", message=True)
    return render_template("eliminar_m5.html")

@app.route('/significado_palabra', methods=['GET', 'POST'])
def significado():
    if request.method == 'POST':
        palabra = request.form['pa']
        if existe(palabra):
            dato = significado_palabra(palabra)
            return render_template("significado_m5.html", message=False, significado=dato)
        else:
            return render_template("significado_m5.html", message=True)
    return render_template("significado_m5.html")


if __name__ == '__main__':
    app.run(debug=True)