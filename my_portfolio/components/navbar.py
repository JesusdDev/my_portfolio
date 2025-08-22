import reflex as rx
from my_portfolio.routes import Route as Route
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.colors import Color, TextColor

def navbar() -> rx.Component:
    return rx.link(
        rx.hstack(
        rx.heading("Bienvenido a mi", color=TextColor.PRIMARY.value),
        rx.heading("Portfolio Interactivo", color=TextColor.SECONDARY.value),
        position="sticky",
        background_color=Color.SECONDARY_BG.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        top=Size.ZERO.value
    ),
    href=Route.INDEX.value,
    
)


          
        