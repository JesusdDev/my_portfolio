import reflex as rx
from my_portfolio.components.ui.button_page import button_page

def links_page() -> rx.Component:
    return rx.hstack(
        button_page("Inicio", "/inicio"),
        button_page("about", "/about"),
        button_page("Proyectos", "/projects"),
        button_page("Contacto", "/contact")
    )

