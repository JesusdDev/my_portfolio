import reflex as rx
from my_portfolio.views.links.links import links_section
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.colors import Color
from my_portfolio.styles.colors import TextColor

def terminal_static() -> rx.Component:
    return rx.vstack(
        rx.text("~/ Portfolio", 
                color=TextColor.EXTRA.value,
                margin=Size.SMALL.value
        ),
            links_section(),
        rx.text("💡 Tip: Usa comandos como cd projects o cd .. en la terminal",
                margin=Size.SMALL.value
        ),
        border_width="1px",
        border_color="#1dd34a",
        background_color=Color.SECONDARY_BG.value,
        border_radius="30px",
        width="auto",
        padding=Size.SMALL.value,
    )