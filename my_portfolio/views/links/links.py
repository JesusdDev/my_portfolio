import reflex as rx
from my_portfolio.components.ui.button_page import button_page

def links_page() -> rx.Component:
    return rx.hstack(
        button_page("Home", "icons/house-plus.svg", "/home"),
        button_page("About", "icons/hand-metal.svg","/about"),
        button_page("Projects", "icons/kanban.svg","/projects"),
        button_page("Contact", "icons/mail.svg","/contact")
    )

