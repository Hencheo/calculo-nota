// Fecha menu mobile ao clicar em um item
document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
    link.addEventListener('click', () => {
        const navbarToggler = document.querySelector('.navbar-toggler');
        const navbarCollapse = document.querySelector('.navbar-collapse');
        if (window.getComputedStyle(navbarToggler).display !== 'none') {
            navbarCollapse.classList.remove('show');
        }
    });
});

// Previne zoom em inputs em iOS
document.addEventListener('touchstart', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') {
        e.target.style.fontSize = '16px';
    }
});

// Adiciona suporte a pull-to-refresh
let touchstartY = 0;
document.addEventListener('touchstart', e => {
    touchstartY = e.touches[0].clientY;
});

document.addEventListener('touchmove', e => {
    const touchY = e.touches[0].clientY;
    const touchDiff = touchY - touchstartY;
    if (touchDiff > 100 && window.scrollY === 0) {
        window.location.reload();
    }
});