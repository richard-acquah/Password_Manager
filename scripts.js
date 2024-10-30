document.addEventListener("DOMContentLoaded", () => {
    const text = document.getElementById("centered-text");
    text.style.transition = "transform 0.5s";
    text.addEventListener("mouseover", () => {
        text.style.transform = "scale(1.1)";
    });
    text.addEventListener("mouseout", () => {
        text.style.transform = "scale(1)";
    });
});
