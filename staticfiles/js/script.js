document.querySelectorAll('.settings-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        // Remove active class from all buttons and sections
        document.querySelectorAll('.settings-btn, .settings-section').forEach(el => {
            el.classList.remove('active');
        });

        // Add active class to clicked button and corresponding section
        btn.classList.add('active');
        const sectionId = btn.getAttribute('data-section');
        document.getElementById(sectionId).classList.add('active');
    });
});
