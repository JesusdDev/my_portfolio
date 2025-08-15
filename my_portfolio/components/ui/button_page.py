import reflex as rx
from my_portfolio.styles.styles import Size as Size
from my_portfolio.styles.styles import Spacing as Spacing


def button_page(text: str, image: str, url: str) -> rx.Component:
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
                margin=Spacing.ZERO.value
            )
            
        ),
        href=url,
        is_external=False,
        width="100%"
    )

