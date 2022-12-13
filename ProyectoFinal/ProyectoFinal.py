from flask import Flask, request, render_template

app = Flask(__name__)

with app.app_context():
    citas = []


@app.route("/", methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        documento = request.form['documento']
        nombre = request.form['nombre'].capitalize()
        telefono = request.form['telefono']
        fecha = request.form['fecha']
        hora = request.form['hora']
        nuevacita = {
            "documento": str(documento),
            "nombre": nombre,
            "telefono": str(telefono),
            "fecha": str(fecha),
            "hora": str(hora)
        }
        citas.append(nuevacita)
        print(citas)
        return render_template("index.html")
    return render_template("index.html")


@app.route("/citas", methods=['GET'])
def show():
    return render_template("citas.html", citas=citas)


if __name__ == '__main__':
    app.run(debug=True)