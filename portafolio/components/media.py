import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.data import Media
from portafolio.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.flex(#con esto creamos un contenedor flexible
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,#link del correo
            True
        ),
        rx.hstack(
            icon_button(
                "file-text",#icono de cv
                data.cv#link del cv 
            ),
            icon_button(
                "github",
                data.github
            ),
            icon_button(
                "linkedin",
                data.likedin
            ),
            spacing=Size.SMALL.value#espaciado entre los iconos de tamaño pequeño
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]#con esto le damos una dirección al contenedor flexible
    )
