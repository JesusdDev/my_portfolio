import reflex as rx
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.styles import Spacing as Spacing


def button(text: str, image: str, on_click_handler: rx.event) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.image(
                src=image,
                width=Size.LARGE.value,
                height=Size.LARGE.value,                    
            ),
            rx.text(text),
                align="start",
                spacing=Spacing.MEDIUM_SMALL.value,
                margin=Spacing.ZERO.value,
        ),
        on_click= on_click_handler,
        width="auto"
    ),
    

