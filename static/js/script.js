document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".category-btn");

    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            const targetId = btn.getAttribute("data-category");
            const targetEl = document.getElementById(targetId);

            if (targetEl) {
                targetEl.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    });
});
