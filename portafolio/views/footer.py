import reflex as rx
from portafolio.components.media import media
from portafolio.data import Media
from portafolio.styles.styles import Size


def footer(data: Media) -> rx.Component:#como parametro recibe un objeto de tipo Media que contiene la informacion de los medios como email, github, linkedin, etc
    return rx.vstack(
        rx.text("Nombre"),#con rx.text creamos un texto que va a contener el nombre
        media(data),
        spacing=Size.SMALL.value
    )
