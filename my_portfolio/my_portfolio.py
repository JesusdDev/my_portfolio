import reflex as rx
from my_portfolio.components.navbar import navbar
from my_portfolio.components.footer import footer
from my_portfolio.views.header.header import header
from my_portfolio.views.change_section import  TerminalState
from my_portfolio.components.terminal_static import terminal_static
from my_portfolio.styles.styles import Size as Size
import my_portfolio.styles.styles as styles


# --- 4. Inicialización de la Aplicación ---
# Se define la página principal usando los componentes importados.
def index() -> rx.Component:
    return rx.box(
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
                    spacing="9",  
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y=Size.BIG.value,           
                ),
            ),
            rx.center(
                footer(),
            )                  
    )    
app = rx.App(
    _state=TerminalState,
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index, "/")

