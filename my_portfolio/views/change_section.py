# my_portfolio/views/change_section.py
import reflex as rx
from my_portfolio.components.home import home
from my_portfolio.components.about import about
#from my_portfolio.components.projects import projects 
#from my_portfolio.components.contact import contact 


class TerminalState(rx.State):
    
    navigation_stack: list[str] = []
    current_section: str = "home"

    def set_current_section(self, section: str):
        self.current_section = section
        if section == "home":
            self.navigation_stack = []
        else:
            self.navigation_stack = [section]
    
    # Define la función como un método del estado
    @rx.var
    def dynamic_main_content(self) -> rx.Component:
        if self.current_section == "home":
            return home()
        if self.current_section == "about":
            return about()
        return rx.box(rx.text("Sección no encontrada", color_scheme="red"))