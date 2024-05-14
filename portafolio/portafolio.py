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
from portafolio.views.adicional import adicional


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
            adicional(DATA.adicionales),
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
            width="100%"#con esto le damos un ancho del 100% al contenedorr
            
        ),
        
        #background="radial-gradient(circle at 22% 11%, rgba(62, 180, 137, .40), hsla(0, 0%, 100%, 0) 19%), radial-gradient(circle at 82% 25%, rgba(33, 150, 243, .36), hsla(0, 0%, 100%, 0) 35%), radial-gradient(circle at 25% 61%, rgba(250, 128, 114, .56), hsla(0, 0%, 100%, 0) 55%)"
       # background="radial-gradient(circle at 22% 11%, rgba(255, 140, 0, .40), hsla(0, 0%, 100%, 0) 19%), radial-gradient(circle at 82% 25%, rgba(255, 20, 147, .36), hsla(0, 0%, 100%, 0) 35%), radial-gradient(circle at 25% 61%, rgba(65, 105, 225, .56), hsla(0, 0%, 100%, 0) 55%)"
       background="radial-gradient(circle at 22% 11%, rgba(255, 192, 203, .40), hsla(0, 0%, 100%, 0) 19%), radial-gradient(circle at 82% 25%, rgba(0, 255, 127, .36), hsla(0, 0%, 100%, 0) 35%), radial-gradient(circle at 25% 61%, rgba(255, 20, 147, .56), hsla(0, 0%, 100%, 0) 55%)"
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
