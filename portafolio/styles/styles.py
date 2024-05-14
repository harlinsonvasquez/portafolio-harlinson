from enum import Enum
import reflex as rx

MAX_WIDTH = "900px"#ancho maximo de la pagina
IMAGE_HEIGHT = "200px"#altura de la imagen


class EmSize(Enum):#medidas que vamos a usar en portafolio.py en la propiedad padding_x y padding_y
    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"
    BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px


STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"
    }
}
background_color = "#f0f0f0"
