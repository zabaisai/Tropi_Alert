document.addEventListener("DOMContentLoaded", () => {
    const formLogin = document.querySelector(".form-login");
    const formRegistro = document.querySelector(".form-registro");
    const formReporte = document.querySelector(".reporte-form");

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    const limpiarErrores = (form) => {
        form.querySelectorAll(".input-error").forEach((el) => el.classList.remove("input-error"));
        form.querySelectorAll(".error-text").forEach((el) => el.remove());
    };

    const mostrarError = (input, mensaje) => {
        input.classList.add("input-error");

        const error = document.createElement("small");
        error.classList.add("error-text");
        error.textContent = mensaje;

        input.parentElement.appendChild(error);
    };

    const validarLogin = () => {
        if (!formLogin) return;

        formLogin.addEventListener("submit", (e) => {
            limpiarErrores(formLogin);

            const correo = document.getElementById("correo");
            const contrasena = document.getElementById("contrasena");

            let valido = true;

            if (!correo.value.trim()) {
                mostrarError(correo, "El correo es obligatorio.");
                valido = false;
            } else if (!emailRegex.test(correo.value.trim())) {
                mostrarError(correo, "Ingresa un correo válido.");
                valido = false;
            }

            if (!contrasena.value.trim()) {
                mostrarError(contrasena, "La contraseña es obligatoria.");
                valido = false;
            } else if (contrasena.value.trim().length < 6) {
                mostrarError(contrasena, "La contraseña debe tener al menos 6 caracteres.");
                valido = false;
            }

            if (!valido) {
                e.preventDefault();
            }
        });
    };

    const validarRegistro = () => {
        if (!formRegistro) return;

        formRegistro.addEventListener("submit", (e) => {
            limpiarErrores(formRegistro);

            const nombre = document.getElementById("nombre");
            const correo = document.getElementById("correo");
            const contrasena = document.getElementById("contrasena");
            const rol = document.getElementById("rol");

            let valido = true;

            if (!nombre.value.trim()) {
                mostrarError(nombre, "El nombre es obligatorio.");
                valido = false;
            } else if (nombre.value.trim().length < 3) {
                mostrarError(nombre, "El nombre debe tener al menos 3 caracteres.");
                valido = false;
            }

            if (!correo.value.trim()) {
                mostrarError(correo, "El correo es obligatorio.");
                valido = false;
            } else if (!emailRegex.test(correo.value.trim())) {
                mostrarError(correo, "Ingresa un correo válido.");
                valido = false;
            }

            if (!contrasena.value.trim()) {
                mostrarError(contrasena, "La contraseña es obligatoria.");
                valido = false;
            } else if (contrasena.value.trim().length < 6) {
                mostrarError(contrasena, "La contraseña debe tener al menos 6 caracteres.");
                valido = false;
            }

            if (!rol.value.trim()) {
                mostrarError(rol, "Debes seleccionar un rol.");
                valido = false;
            }

            if (!valido) {
                e.preventDefault();
            }
        });
    };

    const validarReporte = () => {
        if (!formReporte) return;

        const descripcion = document.getElementById("descripcion");

        if (descripcion) {
            const contador = document.createElement("small");
            contador.classList.add("char-counter");
            contador.textContent = `0 / 300 caracteres`;
            descripcion.parentElement.appendChild(contador);

            descripcion.addEventListener("input", () => {
                contador.textContent = `${descripcion.value.length} / 300 caracteres`;
            });
        }

        formReporte.addEventListener("submit", (e) => {
            limpiarErrores(formReporte);

            const ubicacion = document.getElementById("ubicacion");
            const tipoFoco = document.getElementById("tipo_foco");
            const fechaReporte = document.getElementById("fecha_reporte");
            const nivelRiesgo = document.getElementById("nivel_riesgo");
            const descripcion = document.getElementById("descripcion");

            let valido = true;

            if (!ubicacion.value.trim()) {
                mostrarError(ubicacion, "La ubicación es obligatoria.");
                valido = false;
            } else if (ubicacion.value.trim().length < 5) {
                mostrarError(ubicacion, "La ubicación debe ser más específica.");
                valido = false;
            }

            if (!tipoFoco.value.trim()) {
                mostrarError(tipoFoco, "Debes seleccionar el tipo de foco.");
                valido = false;
            }

            if (!fechaReporte.value.trim()) {
                mostrarError(fechaReporte, "Debes seleccionar la fecha.");
                valido = false;
            }

            if (!nivelRiesgo.value.trim()) {
                mostrarError(nivelRiesgo, "Debes seleccionar el nivel de riesgo.");
                valido = false;
            }

            if (!descripcion.value.trim()) {
                mostrarError(descripcion, "La descripción es obligatoria.");
                valido = false;
            } else if (descripcion.value.trim().length < 15) {
                mostrarError(descripcion, "La descripción debe tener al menos 15 caracteres.");
                valido = false;
            } else if (descripcion.value.trim().length > 300) {
                mostrarError(descripcion, "La descripción no debe superar los 300 caracteres.");
                valido = false;
            }

            if (!valido) {
                e.preventDefault();
            }
        });
    };

    validarLogin();
    validarRegistro();
    validarReporte();
});