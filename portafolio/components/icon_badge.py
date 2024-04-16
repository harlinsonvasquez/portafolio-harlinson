import reflex as rx

from portafolio.styles.styles import EmSize


def icon_badge(icon: str) -> rx.Component:
    return rx.badge(#retornamos un badge con el icono
        rx.icon(
            icon,
            size=32
        ),
        aspect_ratio="1",#le damos un aspecto de 1 para que sea cuadrado
        variant="soft"
    )