import reflex as rx
import my_portfolio.utils as utils
from my_portfolio.routes import Route
from my_portfolio.components.navbar import navbar
from my_portfolio.components.contact import contact
from my_portfolio.components.footer import footer
from my_portfolio.views.header import header 
from my_portfolio.views.terminal_static import terminal_static
from my_portfolio.styles.styles import Size as Size
import my_portfolio.styles.styles as styles

@rx.page(
        route=Route.CONTACT.value,
    title=utils.contact_tittle,
    description=utils.contact_description,
    meta=utils.contact_meta
        
)

def contact_page() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                rx.box(
                    header(details= False),
                    max_width="600px",
                    width="100%",
                    margin_top=Size.DEFAULT.value
                )                                        
            )
        ),                                                               
            rx.center(
                rx.hstack(
                    terminal_static(),
                    contact(),          
                    spacing="9",  
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y=Size.BIG.value,           
                ),
            ),
            rx.center(
                footer(),
            ),             
    )