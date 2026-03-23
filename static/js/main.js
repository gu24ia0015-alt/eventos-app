// Función para calcular el presupuesto en tiempo real
function simularPresupuesto() {
    // 1. Obtenemos los valores de los inputs del HTML
    const tipo = document.getElementById("tipo_simulador").value;
    const personas = parseInt(document.getElementById("personas_simulador").value) || 0;
    const decoracion = document.getElementById("deco_simulador").value;

    // 2. Definimos los precios (deben coincidir con tu lógica de Python en app.py)
    const preciosBase = {
        "Boda": 200,
        "Cumpleanos": 100,
        "Graduacion": 120,
        "Corporativo": 180
    };

    const preciosDeco = {
        "Floral": 50,
        "Elegante": 80,
        "Globos": 30,
        "Minimalista": 40
    };

    // 3. Realizamos el cálculo
    const costoBase = preciosBase[tipo] || 100;
    const costoDeco = preciosDeco[decoracion] || 30;
    const total = (costoBase + costoDeco) * personas;

    // 4. Mostramos el resultado en la página con formato de moneda
    const resultadoDiv = document.getElementById("resultado_simulacion");
    resultadoDiv.innerHTML = `<h3>Presupuesto Estimado: $${total.toLocaleString()}</h3>`;
    
    // Añadimos una animación ligera de aparición
    resultadoDiv.style.opacity = 0;
    setTimeout(() => { resultadoDiv.style.opacity = 1; }, 10);
}