import reflex as rx
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.colors import Color
from my_portfolio.styles.colors import TextColor
from my_portfolio.styles.styles import Spacing as Spacing

def about() -> rx.Component:
    return rx.stack(
        rx.heading("About page"),
        width="50%",
        height="auto",
        direction="column",
        align="center",
        border_width="1px",
        border_radius="30px",
        border_color="#1dd34a",
        spacing=Spacing.SMALL.value,
        background_color=Color.SECONDARY_BG.value
    )