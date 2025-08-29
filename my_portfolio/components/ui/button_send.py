import reflex as rx
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.styles import Spacing as Spacing


def button_send(text: str, image: str) -> rx.Component:
    return rx.link(
        rx.button(
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
             width="100%",
             type="submit",
        ),
        width="auto",
    )

