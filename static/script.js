document.addEventListener("DOMContentLoaded", function() {
    let currentPage = location.pathname.split('/').pop().replace('.html', '');

    if(currentPage === "") {
        currentPage = "home";  // Assuming your default home page file is home.html
    }

    const activeLink = document.querySelector(`.navbar a[data-page="${currentPage}"]`);
    if (activeLink) {
        activeLink.classList.add("active");
    }
});
