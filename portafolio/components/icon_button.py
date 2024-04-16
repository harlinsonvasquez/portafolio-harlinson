import reflex as rx


def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:#creamos el componente que va dibujar los iconos
    return rx.link(#creamos un link que va a contener el icono
        rx.button(#creamos un boton que va a contener el icono
            rx.icon(icon),#creamos el icono
            text,
            variant="solid" if solid else "surface"
        ),
        href=url,
        is_external=True#con esto le decimos que el link va a ser externo o abrir en otra pestaña
    )
