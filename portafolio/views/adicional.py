import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Adicional
from portafolio.styles.styles import EmSize, Size


def adicional(adicionales: list[Adicional]) -> rx.Component:
    return rx.vstack(
        heading("Complementos"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=adicional.icon,
                        font_size="24px"
                    ),
                    rx.text(adicional.name),
                    size="2"
                )
                for adicional in adicionales
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
