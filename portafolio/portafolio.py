import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack
from portafolio.views.framework import framework

DATA = data.data#con esto importamos los datos de la página que se encuentran en el archivo data.py


def index() -> rx.Component:
    return rx.center(
         #rx.theme_panel(),
        rx.vstack(
            header(DATA),#le pasamos al header los datos que vienen del archivo data.py que a su vez vienen del archivo data.json
            about(DATA.about),
            rx.divider(),#con esto creamos una linea divisoria
            tech_stack(DATA.technologies),
            framework(DATA.frameworks),
            info("Experiencia", DATA.experience),#con esto mostramos la información de la experiencia en la página
            info("Proyectos", DATA.projects),#con esto mostramos la información de los proyectos en la página
            info("Formación,", DATA.training),#con esto mostramos la información de la formación en la página   
            extra(DATA.extras),#con esto mostramos la información extra en la página
            rx.divider(),#con esto creamos una linea divisoria
            footer(DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"#con esto le damos un ancho del 100% al contenedor
        )
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        #accent_color="grass",
        radius="large",
        panelBackground="solid",
        grayColor="sand"
    )
)


title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)
