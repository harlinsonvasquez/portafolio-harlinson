import reflex as rx
from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.data import Extra
from portafolio.styles.styles import Size


def extra(extras: list[Extra]) -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.mobile_only(
            rx.vstack(#lo pintamos en columna cuando esta en modo movil
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(#lo definimos grid cuando esta en modo tablet o desktop y que se repatrta en 3 columnas
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing=Size.DEFAULT.value,
                columns="3"
            ),
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
