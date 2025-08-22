import reflex as rx
from my_portfolio.routes import Route
from my_portfolio.components.ui.button_section import button_section


def links_section() -> rx.Component:
    return rx.hstack(
        button_section("Inicio", 
                       "icons/house-plus.svg",
                        Route.INDEX.value
                    ),
        button_section("Sobre mi", 
                       "icons/hand-metal.svg", 
                        Route.ABOUT.value
                    ),
        button_section("Proyectos", 
                       "icons/kanban.svg", 
                        Route.PROJECTS.value
                    ),
        button_section("Contáctame", 
                       "icons/mail.svg", 
                        Route.CONTACT.value
                    )
    )

