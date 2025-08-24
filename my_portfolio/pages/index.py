import reflex as rx
import my_portfolio.utils as utils
from my_portfolio.routes import Route
from my_portfolio.components.navbar import navbar
from my_portfolio.components.footer import footer
from my_portfolio.views.header import header 
from my_portfolio.views.change_section import  TerminalState
from my_portfolio.views.terminal_static import terminal_static
from my_portfolio.styles.styles import Size as Size
import my_portfolio.styles.styles as styles

@rx.page(
    
    title=utils.index_tittle,
    description=utils.index_description,
    meta=utils.index_meta
        
)

def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                rx.box(
                    header(),
                    max_width="600px",
                    width="100%",
                    margin_top=Size.DEFAULT.value
                )                                        
            )
        ),                                                               
            rx.center(
                rx.hstack(
                    terminal_static(),
                    TerminalState.dynamic_main_content,            
                    padding=Size.DEFAULT.value,          
                    spacing="7", 
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y=Size.BIG.value,           
                ),
            ),
            rx.center(
                footer(),
            ),             
    )