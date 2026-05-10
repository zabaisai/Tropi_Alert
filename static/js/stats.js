document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll("[data-target]");

    counters.forEach(counter => {
        const updateCounter = () => {
            const target = +counter.getAttribute("data-target");
            const current = +counter.innerText;
            const increment = Math.ceil(target / 30);

            if (current < target) {
                counter.innerText = current + increment > target ? target : current + increment;
                setTimeout(updateCounter, 40);
            }
        };

        updateCounter();
    });
});