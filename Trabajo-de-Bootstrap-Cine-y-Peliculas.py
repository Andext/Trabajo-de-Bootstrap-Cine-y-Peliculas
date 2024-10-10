<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cine y Películas</title>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Estilos personalizados */
        .hero {
            background-image: url('https://cine-background.jpg'); /* Cambia la URL por una imagen de cine */
            background-size: cover;
            background-position: center;
            height: 70vh;
            color: white;
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .hero h1 {
            font-size: 4rem;
        }
    </style>
</head>
<body>


<nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">CineManía</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link" href="#inicio">Inicio</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#acerca">Acerca de</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#peliculas">Películas</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#contacto">Contacto</a>
            </li>
        </ul>
    </div>
</nav>


<section id="inicio" class="hero">
    <div>
        <h1>CineManía</h1>
        <p>El lugar donde el séptimo arte cobra vida</p>
    </div>
</section>


<section id="acerca" class="container mt-5">
    <h2>Acerca de CineManía</h2>
    <p>Somos apasionados del cine y nos dedicamos a compartir información sobre las mejores películas de todos los tiempos. Aquí encontrarás recomendaciones, críticas, y mucho más para verdaderos cinéfilos.</p>
</section>


<section id="peliculas" class="container mt-5">
    <h2>Películas Recomendadas</h2>
    <div class="row">
        <div class="col-md-4">
            <div class="card">
                <img src="https://pelicula1.jpg" class="card-img-top" alt="Película 1">
                <div class="card-body">
                    <h5 class="card-title">Película 1</h5>
                    <p class="card-text">Una obra maestra del cine que debes ver.</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card">
                <img src="https://pelicula2.jpg" class="card-img-top" alt="Película 2">
                <div class="card-body">
                    <h5 class="card-title">Película 2</h5>
                    <p class="card-text">Una historia épica con un guión impecable.</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card">
                <img src="https://pelicula3.jpg" class="card-img-top" alt="Película 3">
                <div class="card-body">
                    <h5 class="card-title">Película 3</h5>
                    <p class="card-text">Una película que ha dejado huella en la historia del cine.</p>
                </div>
            </div>
        </div>
    </div>
</section>


<section id="contacto" class="container mt-5 mb-5">
    <h2>Contáctanos</h2>
    <form>
        <div class="form-group">
            <label for="nombre">Nombre</label>
            <input type="text" class="form-control" id="nombre" placeholder="Tu nombre" required>
        </div>
        <div class="form-group">
            <label for="email">Correo electrónico</label>
            <input type="email" class="form-control" id="email" placeholder="Tu correo electrónico" required>
        </div>
        <div class="form-group">
            <label for="mensaje">Mensaje</label>
            <textarea class="form-control" id="mensaje" rows="3" placeholder="Escribe tu mensaje" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Enviar</button>
    </form>
</section>


<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

