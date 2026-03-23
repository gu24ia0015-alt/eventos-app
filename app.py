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

if __name__ == "__main__":
    app.run(debug=True)