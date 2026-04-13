document.addEventListener("DOMContentLoaded", () => {
    const filtroRiesgo = document.getElementById("filtro-riesgo");
    const buscador = document.getElementById("buscador-alertas");
    const botonLimpiar = document.getElementById("limpiar-filtros");
    const contador = document.getElementById("contador-alertas");
    const sinResultados = document.getElementById("sin-resultados-alertas");
    const tarjetas = document.querySelectorAll(".alerta-card");

    if (!filtroRiesgo || !buscador || !botonLimpiar || !contador || !sinResultados || tarjetas.length === 0) {
        return;
    }

    const normalizarTexto = (texto) => {
        return texto
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "");
    };

    const aplicarFiltros = () => {
        const riesgoSeleccionado = filtroRiesgo.value;
        const textoBusqueda = normalizarTexto(buscador.value.trim());

        let visibles = 0;

        tarjetas.forEach((tarjeta) => {
            const riesgoTarjeta = tarjeta.dataset.riesgo;
            const tituloTarjeta = normalizarTexto(tarjeta.dataset.titulo || "");
            const descripcionTarjeta = normalizarTexto(tarjeta.dataset.descripcion || "");

            const coincideRiesgo =
                riesgoSeleccionado === "todos" || riesgoTarjeta === riesgoSeleccionado;

            const coincideTexto =
                textoBusqueda === "" ||
                tituloTarjeta.includes(textoBusqueda) ||
                descripcionTarjeta.includes(textoBusqueda);

            if (coincideRiesgo && coincideTexto) {
                tarjeta.classList.remove("alerta-hidden");
                tarjeta.classList.add("alerta-visible");
                visibles++;
            } else {
                tarjeta.classList.add("alerta-hidden");
                tarjeta.classList.remove("alerta-visible");
            }
        });

        contador.textContent = visibles;

        if (visibles === 0) {
            sinResultados.classList.remove("oculto");
        } else {
            sinResultados.classList.add("oculto");
        }
    };

    filtroRiesgo.addEventListener("change", aplicarFiltros);
    buscador.addEventListener("input", aplicarFiltros);

    botonLimpiar.addEventListener("click", () => {
        filtroRiesgo.value = "todos";
        buscador.value = "";
        aplicarFiltros();
    });

    aplicarFiltros();
}); 