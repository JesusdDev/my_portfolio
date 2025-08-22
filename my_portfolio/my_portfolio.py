import reflex as rx
from my_portfolio.pages.index import index 
from my_portfolio.pages.about_page import  about 
from my_portfolio.pages.projects_page import projects
from my_portfolio.pages.contact_page import contact
from my_portfolio.views.change_section import  TerminalState
import my_portfolio.styles.styles as styles

#Aquí solo vamos a tener el punto de entrada de la app
    
app = rx.App(
    _state=TerminalState,
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

