from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_eventos = [
    {
        "id": 1,
        "nombre": "Boda de Ana y Carlos",
        "tipo": "Boda",
        "fecha": "2025-06-15",
        "personas": 150,
        "decoracion": "Floral",
        "precio": 45000
    },
    {
        "id": 2,
        "nombre": "Graduación UAA 2025",
        "tipo": "Graduacion",
        "fecha": "2025-07-20",
        "personas": 80,
        "decoracion": "Elegante",
        "precio": 22000
    },
    {
        "id": 3,
        "nombre": "Cumpleaños de María",
        "tipo": "Cumpleanos",
        "fecha": "2025-05-10",
        "personas": 50,
        "decoracion": "Globos",
        "precio": 12000
    }
]

siguiente_id = 4

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html", eventos=lista_eventos)

@app.route("/eventos/nuevo", methods=["GET"])
def nuevo_evento_form():
    return render_template("nuevo_evento.html")

@app.route("/eventos/nuevo", methods=["POST"])
def nuevo_evento():
    global siguiente_id
    evento = {
        "id": siguiente_id,
        "nombre": request.form["nombre"],
        "tipo": request.form["tipo"],
        "fecha": request.form["fecha"],
        "personas": int(request.form["personas"]),
        "decoracion": request.form["decoracion"],
        "precio": calcular_precio(
            request.form["tipo"],
            int(request.form["personas"]),
            request.form["decoracion"]
        )
    }
    lista_eventos.append(evento)
    siguiente_id += 1
    return redirect(url_for("eventos"))

if __name__ == "__main__":
    app.run(debug=True)