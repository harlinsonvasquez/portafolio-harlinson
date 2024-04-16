import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(  #creamos un contenedor horizontal
            icon_badge(info.icon),
            rx.vstack(#creamos un contenedor vertical
                rx.text.strong(info.title),#creamos un texto en negrita con el titulo
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"#le damos un color gris al texto de la descripcion
                ),
                rx.cond(
                    info.technologies,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(class_name=technology.icon),
                                technology.name,
                                color_scheme="gray"
                            )
                            for technology in info.technologies#recorremos la lista de tecnologias y creamos un badge con el icono y el nombre de la tecnologia 
                        ],
                        wrap="wrap",
                        spacing=Size.SMALL.value
                    )
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url
                        )
                    ),
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github
                        )
                    )
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.cond(
            info.image != "",
            rx.image(
                src=info.image,#|image| es la propiedad que contiene la url de la imagen
                height=IMAGE_HEIGHT,#|IMAGE_HEIGHT| es la propiedad que contiene la altura de la imagen
                width="auto",#|auto| es la propiedad que le da un ancho automatico a la imagen
                border_radius=EmSize.DEFAULT.value,#|EmSize.DEFAULT.value| es la propiedad que contiene el radio del borde de la imagen
                object_fit="cover"#|cover| es la propiedad que le da un ajuste de imagen de portada a la imagen
            )
        ),
        rx.vstack(
            rx.cond(
                info.date != "",
                rx.badge(info.date)
            ),
            rx.cond(
                info.certificate != "",
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            spacing=Size.SMALL.value,
            align="end"#alineamos los elementos al final
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
