# Portafolio "perfecto" para programadores

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.5+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)

[![HTML](https://img.shields.io/badge/HTML-orange?style=for-the-badge&logo=html5&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-blue?style=for-the-badge&logo=css3&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-yellow?style=for-the-badge&logo=javascript&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/JavaScript)

## Plantilla de portafolio web minimalista configurable a nivel gráfico y de contenido.

Desarrollado utilizando [Python](https://python.org) y [Reflex](https://reflex.dev), disponible para desplegar de forma estática (HTML, CSS, JS).



## Instalación

Puedes seguir la [guía oficial](https://reflex.dev/docs/getting-started/installation/) de Reflex.

Clona el proyecto, crea un entorno virtual, instala Reflex y ejecútalo para acceder al proyecto desde [http://localhost:3000](http://localhost:3000).

`pip install reflex`

`reflex init`

`reflex run`

## Configuración

Principalmente puedes configurar el contenido y el aspecto gráfico del sitio web.

* Contenido: Edita el archivo [data.json](./assets/data/data.json) con la información de tu portafolio.
	* Campos opcionales dentro de `experience`, `projects` y `training`: *technologies, date, certificate, image, url y github*.
	* Los iconos generales se corresponden con los identificadores de [Lucide icons](https://lucide.dev/icons/).
	* Los iconos de las tecnologías se corresponden con los identificadores de [Devicon](https://devicon.dev/).
* Tema: Edita el tema gráfico de la web.
	* Descomenta la línea `rx.theme_panel()` en `portafolio.py`. 
	* Inicia el proyecto, selecciona la configuración que quieras y pulsa `Copy Theme`.
	* Añade esa información dentro de `theme=rx.theme()` en `portafolio.py`.

## Despliegue

![Vercel](https://img.shields.io/github/stars/vercel/vercel?label=Vercel&style=social)

El proyecto utiliza [Vercel](https://vercel.com) como hosting de recursos estáticos.

Se configura el despliegue automático desde los archivos [vercel.json](./vercel.json) y [build.sh](./build.sh).

Aquí tienes la [demo](https://portafolio-template.vercel.app/).

