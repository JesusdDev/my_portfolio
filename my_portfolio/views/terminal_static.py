import reflex as rx
from my_portfolio.views.links_section import links_section
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.colors import Color
from my_portfolio.styles.colors import TextColor

def terminal_static() -> rx.Component:
    return rx.vstack(
        rx.text("~/ Portfolio", 
                color=TextColor.EXTRA.value,
            ),
        links_section(),
        rx.text("💡 Tip: Usa comandos como cd projects o cd .. en la terminal",
        ),
        border_width="1px",
        border_color=Color.BORDER_COLOR.value,
        background_color=Color.SECONDARY_BG.value,
        border_radius="30px",
        width="90%",
        padding=Size.SMALL.value
    )