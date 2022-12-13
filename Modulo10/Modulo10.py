from flask import Flask, render_template, request
app = Flask(__name__)

slang = [{"palabra":"MOPRI","significado":"compa"}]


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index_m10.html", palabras=slang)


@app.route('/agregar_palabra', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        palabra = request.form['pa'].capitalize()
        significado = request.form['si']
        nuevoslang = {"palabra":palabra.upper(),
                      "significado":significado
                      }
        for i in slang:
            if i["palabra"] == palabra.upper():
                existe = i["palabra"]
                if len(existe) > 0:
                  return render_template("agregar_m10.html", message=False)
        slang.append(nuevoslang)
        return render_template("agregar_m10.html", message=True)

    return render_template("agregar_m10.html")


@app.route('/editar_palabra', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        palabra = request.form["vpa"].capitalize()
        j = 0
        for i in slang:
            if i["palabra"] == palabra.upper():
                existe = i["palabra"]
                if len(existe) > 0:
                    new = request.form["pa"]
                    slang[j]["palabra"] = new.upper()
                    return render_template("editar_m10.html", message=False)
            j = j+1
        return render_template("editar_m10.html", message=True)

    return render_template("editar_m10.html")

@app.route('/editar_significado', methods=['GET', 'POST'])
def editar_sig():
    if request.method == 'POST':
        palabra = request.form["vpa"]
        news = request.form["si"]
        j = 0
        for i in slang:
            if i["palabra"] == palabra.upper():
                existe = i["palabra"]
                if len(existe) > 0:
                    slang[j]["significado"] = news
                    return render_template("editar_significado_m10.html", message=False)
            j = j + 1

        return render_template("editar_significado_m10.html", message=True)
    return render_template("editar_significado_m10.html")


@app.route('/eliminar_palabra', methods=['GET', 'POST'])
def eliminar():
    if request.method == 'POST':
        palabra = request.form['pa']
        j = 0
        for i in slang:
            if i["palabra"] == palabra.upper():
                existe = i["palabra"]
                if len(existe) > 0:
                    slang.pop(j)
                    return render_template("eliminar_m10.html", message=False)
            j = j + 1

        return render_template("eliminar_m10.html", message=True)
    return render_template("eliminar_m10.html")

@app.route('/significado_palabra', methods=['GET', 'POST'])
def significado():
    if request.method == 'POST':
        palabra = request.form['pa']
        j = 0
        for i in slang:
            if i["palabra"] == palabra.upper():
                existe = i["palabra"]
                if len(existe) > 0:
                    dato = []
                    dato.append(slang[j])
                    print(dato)
                    return render_template("significado_m10.html", message=False, significado=dato)
            j = j + 1

        return render_template("significado_m10.html", message=True)
    return render_template("significado_m10.html")


if __name__ == '__main__':
    app.run(debug=True)