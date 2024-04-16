import reflex as rx
from portafolio.components.heading import heading


def about(description: str) -> rx.Component:#creamos el componente que va a contener la descripcion
    return rx.vstack(
        heading("Sobre mí"),
        rx.text(description)
    )
