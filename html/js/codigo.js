// Espera a que se cargue el documento HTML
document.addEventListener("DOMContentLoaded", function(event) {
	// Oculta el preloader
	var preloader = document.querySelector(".preloader");
	preloader.classList.add("oculto");

	// Muestra el contenido del sitio web
	var contenidoSitio = document.querySelector(".contenido-sitio");
	contenidoSitio.classList.remove("oculto");
});
