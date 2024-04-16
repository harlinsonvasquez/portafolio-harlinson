import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Framework
from portafolio.styles.styles import EmSize, Size


def framework(frameworks: list[Framework]) -> rx.Component:
    return rx.vstack(
        heading("Frameworks"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=framework.icon,
                        font_size="24px"
                    ),
                    rx.text(framework.name),
                    size="2"
                )
                for framework in frameworks
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
