import reflex as rx
from portafolio.data import Extra

from portafolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(#retornamos un card con la imagen, el titulo y la descripcion
        rx.link(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(extra.title),
            rx.text(#creamos un texto con la descripcion
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray"
            )
        ),
        width="100%",
        href=extra.url,
        is_external=True
    )
