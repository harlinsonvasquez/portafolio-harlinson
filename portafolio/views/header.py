import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import Size


def header(data: Data) -> rx.Component:#con esto creamos el encabezado de la página y los parametros que recibe son los datos del json que fue convertidos a clases en el archivo data.py
    return rx.hstack(
        rx.avatar(
            src=data.avatar,#data.avatar es la imagen del avatar que se encuentra en el archivo data.py
            size=Size.BIG.value #con esto le damos la propiedad de tamaño grande al avatar
        ),
        rx.vstack(
            heading(data.name, True),
            heading(data.skill),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"
            ),
            media(data.media),
            spacing=Size.SMALL.value,#espaciado entre el avatar y el texto  
        ),
        spacing=Size.DEFAULT.value,#con esto espaciamos el avatar y el texto
    )
