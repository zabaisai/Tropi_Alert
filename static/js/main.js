document.addEventListener("DOMContentLoaded", () => {

    // =========================
    // NAVBAR LINK ACTIVO
    // =========================
    const links = document.querySelectorAll(".navbar a");
    const currentPath = window.location.pathname;

    links.forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active-link");
        }
    });

    // =========================
    // SCROLL ANIMATIONS
    // =========================
    const animElements = document.querySelectorAll(".fade-in");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    }, { threshold: 0.15 });

    animElements.forEach(el => observer.observe(el));

    // =========================
    // HOVER EFECTO EN CARDS
    // =========================
    const cards = document.querySelectorAll(".dashboard-card, .alerta-card, .admin-item-card");

    cards.forEach(card => {
        card.addEventListener("mousemove", (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            card.style.setProperty("--x", `${x}px`);
            card.style.setProperty("--y", `${y}px`);
        });
    });

    // =========================
    // BOTÓN SCROLL TOP
    // =========================
    const scrollBtn = document.createElement("button");
    scrollBtn.innerText = "↑";
    scrollBtn.classList.add("scroll-top-btn");
    document.body.appendChild(scrollBtn);

    window.addEventListener("scroll", () => {
        if (window.scrollY > 300) {
            scrollBtn.classList.add("show");
        } else {
            scrollBtn.classList.remove("show");
        }
    });

    scrollBtn.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });

    // =========================
    // EFECTO CLICK BOTONES
    // =========================
    const botones = document.querySelectorAll("button, .btn");

    botones.forEach(btn => {
        btn.addEventListener("click", () => {
            btn.classList.add("btn-click");
            setTimeout(() => {
                btn.classList.remove("btn-click");
            }, 200);
        });
    });

    // =========================
    // AUTO OCULTAR MENSAJES FLASH
    // =========================
    const flashes = document.querySelectorAll(".flash-message");

    flashes.forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = "0";
            msg.style.transform = "translateY(-10px)";
            setTimeout(() => msg.remove(), 400);
        }, 3000);
    });

});