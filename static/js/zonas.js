const departamentosRiesgo = {
    "Antioquia": {
        riesgo: "medio",
        estado: "Seguimiento activo",
        prioridad: "Media",
        descripcion: "Departamento con zonas urbanas y rurales que requieren monitoreo preventivo por presencia de posibles focos sanitarios.",
        recomendacion: "Fortalecer la vigilancia comunitaria, eliminar aguas estancadas y reportar acumulación de residuos."
    },
    "Valle del Cauca": {
        riesgo: "alto",
        estado: "Intervención prioritaria",
        prioridad: "Alta",
        descripcion: "Zona con condiciones climáticas y urbanas que pueden favorecer la presencia de vectores en algunos sectores.",
        recomendacion: "Realizar control de criaderos, campañas de prevención y seguimiento frecuente en barrios vulnerables."
    },
    "Cundinamarca": {
        riesgo: "medio",
        estado: "Seguimiento activo",
        prioridad: "Media",
        descripcion: "Departamento con áreas en observación por variación de temperatura, movilidad poblacional y zonas periurbanas.",
        recomendacion: "Mantener monitoreo territorial y reforzar actividades de educación sanitaria."
    },
    "Atlántico": {
        riesgo: "alto",
        estado: "Intervención prioritaria",
        prioridad: "Alta",
        descripcion: "Departamento costero con condiciones ambientales que pueden aumentar la presencia de mosquitos en temporadas cálidas.",
        recomendacion: "Incrementar jornadas de limpieza, control de depósitos de agua y comunicación preventiva."
    },
    "Bolívar": {
        riesgo: "alto",
        estado: "Intervención prioritaria",
        prioridad: "Alta",
        descripcion: "Zona con alta exposición a humedad y focos potenciales en áreas urbanas y rurales.",
        recomendacion: "Priorizar vigilancia sanitaria, control vectorial y reportes tempranos de síntomas."
    },
    "Santander": {
        riesgo: "medio",
        estado: "Seguimiento activo",
        prioridad: "Media",
        descripcion: "Departamento en seguimiento por presencia de zonas cálidas, movilidad territorial y posibles criaderos.",
        recomendacion: "Reforzar campañas educativas y control de aguas estancadas en viviendas y espacios públicos."
    },
    "Chocó": {
        riesgo: "alto",
        estado: "Intervención prioritaria",
        prioridad: "Alta",
        descripcion: "Región con alta humedad y condiciones ambientales que requieren vigilancia constante.",
        recomendacion: "Fortalecer el monitoreo comunitario, la atención temprana y la eliminación de criaderos."
    },
    "Tolima": {
        riesgo: "medio",
        estado: "Seguimiento activo",
        prioridad: "Media",
        descripcion: "Departamento con municipios cálidos en observación por posibles focos de enfermedades tropicales.",
        recomendacion: "Mantener controles preventivos y reportar zonas con agua acumulada."
    },
    "Huila": {
        riesgo: "medio",
        estado: "Seguimiento activo",
        prioridad: "Media",
        descripcion: "Zona con sectores de clima cálido que requieren vigilancia sanitaria preventiva.",
        recomendacion: "Promover limpieza de patios, control de recipientes y educación comunitaria."
    },
    "Meta": {
        riesgo: "medio",
        estado: "Seguimiento activo",
        prioridad: "Media",
        descripcion: "Departamento con áreas rurales y urbanas que pueden presentar focos sanitarios durante temporadas de lluvia.",
        recomendacion: "Reforzar el seguimiento en zonas con acumulación de agua y alta movilidad."
    },
    "Nariño": {
        riesgo: "bajo",
        estado: "Observación preventiva",
        prioridad: "Baja",
        descripcion: "Departamento con zonas de menor riesgo relativo, aunque se recomienda mantener vigilancia preventiva.",
        recomendacion: "Sostener campañas educativas y reportar cambios en las condiciones sanitarias."
    },
    "Amazonas": {
        riesgo: "alto",
        estado: "Intervención prioritaria",
        prioridad: "Alta",
        descripcion: "Región selvática con condiciones ambientales favorables para enfermedades tropicales.",
        recomendacion: "Fortalecer prevención comunitaria, atención temprana y monitoreo de síntomas."
    }
};

const botonesDepartamento = document.querySelectorAll(".departamento");
const panel = document.getElementById("zonaInfoPanel");
const panelNivel = document.getElementById("panelNivel");
const panelDepartamento = document.getElementById("panelDepartamento");
const panelDescripcion = document.getElementById("panelDescripcion");
const panelEstado = document.getElementById("panelEstado");
const panelPrioridad = document.getElementById("panelPrioridad");
const panelRecomendacion = document.getElementById("panelRecomendacion");

function aplicarClaseRiesgo(elemento, baseClase, riesgo) {
    elemento.classList.remove(`${baseClase}-alto`, `${baseClase}-medio`, `${baseClase}-bajo`);
    elemento.classList.add(`${baseClase}-${riesgo}`);
}

function actualizarPanel(nombreDepartamento) {
    const datos = departamentosRiesgo[nombreDepartamento];

    if (!datos) return;

    panelDepartamento.textContent = nombreDepartamento;
    panelDescripcion.textContent = datos.descripcion;
    panelEstado.textContent = datos.estado;
    panelPrioridad.textContent = datos.prioridad;
    panelRecomendacion.textContent = datos.recomendacion;

    panelNivel.textContent = `Riesgo ${datos.riesgo.charAt(0).toUpperCase() + datos.riesgo.slice(1)}`;

    panel.classList.remove("riesgo-alto", "riesgo-medio", "riesgo-bajo");
    panel.classList.add(`riesgo-${datos.riesgo}`);

    panelNivel.classList.remove("riesgo-alto", "riesgo-medio", "riesgo-bajo");
    panelNivel.classList.add(`riesgo-${datos.riesgo}`);

    botonesDepartamento.forEach((boton) => {
        boton.classList.remove("activo");
    });

    const botonActivo = document.querySelector(`[data-departamento="${nombreDepartamento}"]`);
    if (botonActivo) {
        botonActivo.classList.add("activo");
    }
}

botonesDepartamento.forEach((boton) => {
    const departamento = boton.dataset.departamento;
    const datos = departamentosRiesgo[departamento];

    if (datos) {
        boton.classList.add(`dept-riesgo-${datos.riesgo}`);
    }

    boton.addEventListener("click", () => {
        actualizarPanel(departamento);
    });
});

actualizarPanel("Antioquia");