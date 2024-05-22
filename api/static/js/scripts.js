document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll('.result-item');
    items.forEach((item, index) => {
        setTimeout(() => {
            item.style.opacity = 1;
        }, index * 200);
    });
});
