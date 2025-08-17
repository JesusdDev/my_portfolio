import reflex as rx
from my_portfolio.components.ui.button import button
from my_portfolio.views.change_section import TerminalState

def links_section() -> rx.Component:
    return rx.hstack(
        button("Home", 
                    "icons/house-plus.svg",
                    on_click_handler= lambda: TerminalState.set_current_section("home")
                    ),
        button("About", 
                    "icons/hand-metal.svg", 
                    on_click_handler= lambda: TerminalState.set_current_section("about")
                    ),
        button("Projects", 
                    "icons/kanban.svg", 
                    on_click_handler= lambda: TerminalState.set_current_section("projects")
                    ),
        button("Contact", 
                    "icons/mail.svg", 
                    on_click_handler= lambda: TerminalState.set_current_section("contact")
                    )
    )

