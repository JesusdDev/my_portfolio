import reflex as rx
from my_portfolio.views.links.links import links_page
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.colors import Color
from my_portfolio.styles.colors import TextColor

def terminal_static() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text("~/ Portfolio", 
            color=TextColor.EXTRA.value, 
            margin=Size.SMALL.value
            ),
            links_page(),
            rx.text("💡 Tip: Usa comandos como cd projects o cd .. en la terminal",
            margin=Size.SMALL.value
            ),
            border_width="1px",
            border_color="#1dd34a",
            background_color=Color.SECONDARY_BG.value,
            border_radius="30px",
            width="100%",
            padding=Size.SMALL.value,
            ),
        rx.box(
            rx.text("PortFolio Terminal v1.0", 
            color=TextColor.EXTRA.value,
            margin=Size.SMALL.value
            ),
            rx.text("Escribe 'help' para ver los comandos disponibles",
            margin=Size.SMALL.value
            ),
            border_width="1px",
            border_color="#1dd34a",
            background_color=Color.SECONDARY_BG.value,
            border_radius="30px",
            width="100%",
            height="55vh",
            padding=Size.SMALL.value
            )
        )