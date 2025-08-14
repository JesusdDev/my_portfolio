import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "1280px"
FADEIN_ANIMATION = "animate__animated animate__fadeIn"
BOUNCEIN_ANIMATION = "animate__animated animate__bounceIn"

# Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Audiowide:wght@400;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Smooch+Sans:wght@400;500&display=swap",
    #"https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    #"/css/styles.css"
]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    MEDIUM_SMALL = "2"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

# Styles


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.REGULAR.value,
    "background_color": Color.BACKGROUND.value,
    #"background_image": "url('/bg_dark_pattern.jpg')",
    #"background_repeat": "repeat",
    #"background_attachment": "fixed",
    rx.text:{
        "color": TextColor.SECONDARY.value,
        "font_family": Font.DEFAULT.value,
        "font_weight": FontWeight.REGULAR.value
    },
    rx.heading: {
        "color": TextColor.PRIMARY.value,
        "font_family": Font.TITTLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "background": Color.BACKGROUND.value,
        "width": "100%",
        "height": "100%",
        "font_weight": FontWeight.MEDIUM.value,
        "text_align": "start",
        "cursor": "pointer",
        "transition": "transform 0.05s ease",
        "color": TextColor.PRIMARY.value,
        "border": f"1px solid {"#1dd34a"}",
        "box_shadow": f"3px 3px 0px 0px {"#1dd34a"}",
        "_hover": {
            "box_shadow": "none",
            "transform": "translate(3px, 3px)"
        }
    },
    rx.link: {
        "color": TextColor.SECONDARY.value,
        "text_decoration": "none",
        ""
        "_hover": {}
    }
}
title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value,
    font_weight=FontWeight.BOLD.value,
)
image_style = {
    "border": f"1px solid {Color.SECONDARY_BG.value}",
    "box_shadow": f"3px 3px 0px 0px {Color.SECONDARY_BG.value}",
    "_hover": {
        "box_shadow": f"6px 6px 0px 0px {Color.SECONDARY_BG.value}",
        "transform": "translate(-3px, -3px)"
    }
}

