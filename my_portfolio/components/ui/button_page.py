import reflex as rx

def button_page(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="monitor"
                ),
                rx.text(text),
            )
        ),
        href=url,
        is_external=False,
        width="100%"
    )

