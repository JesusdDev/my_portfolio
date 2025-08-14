# Importaciones necesarias de Reflex y otras librerías.
import reflex as rx
import datetime
import random

# --- 1. Definición del Estado de la Aplicación ---
# La clase State de Reflex reemplaza los hooks useState y useRef de React.
# Todas las variables de estado y la lógica de la terminal residen aquí.
class TerminalState(rx.State):
    """Maneja el estado y la lógica de la terminal."""

    # Variables de estado que reemplazan a `useState`.
    history: list[dict] = [
        {"type": "system", "content": "Portfolio Terminal v1.0"},
        {"type": "system", "content": "Escribe 'help' para ver los comandos disponibles."},
        {"type": "system", "content": ""},
    ]
    current_input: str = ""
    command_history: list[str] = []
    history_index: int = -1
    # navigation_stack para rastrear el directorio actual.
    navigation_stack: list[str] = []
    # `current_section` para saber qué contenido mostrar en la parte central.
    current_section: str = "home"
    
    # --- Lógica de la terminal (Reemplaza las funciones de JS) ---

    @rx.var
    def current_path(self) -> str:
        """Propiedad para obtener el path actual para el prompt."""
        if not self.navigation_stack:
            return "home"
        return "/".join(self.navigation_stack)

    @rx.var
    def prompt_path(self) -> str:
        """Propiedad para formatear el path para mostrar en el prompt."""
        path = self.current_path
        return "~" if path == "home" else f"~/{path}"

    def handle_submit(self):
        """Maneja la lógica cuando el usuario presiona Enter en la terminal."""
        # Se agrega el comando al historial.
        self.command_history.append(self.current_input)
        self.history.append({
            "type": "input",
            "content": f"portfolio:{self.prompt_path}$ {self.current_input}",
        })

        # Se ejecuta el comando y se obtiene el output.
        output = self.execute_command(self.current_input)
        for line in output:
            self.history.append({"type": "output", "content": line})

        # Limpiamos el input y el índice del historial.
        self.current_input = ""
        self.history_index = -1
        
    def handle_key_up(self, key_code: str):
        """Maneja los eventos de teclado para las flechas arriba/abajo."""
        if key_code == "ArrowUp":
            if len(self.command_history) > 0:
                new_index = len(self.command_history) - 1 if self.history_index == -1 else max(0, self.history_index - 1)
                self.history_index = new_index
                self.current_input = self.command_history[new_index]
        elif key_code == "ArrowDown":
            if self.history_index != -1:
                new_index = self.history_index + 1
                if new_index >= len(self.command_history):
                    self.current_input = ""
                    self.history_index = -1
                else:
                    self.history_index = new_index
                    self.current_input = self.command_history[new_index]

    def execute_command(self, cmd: str) -> list[str]:
        """Lógica para ejecutar un comando de la terminal."""
        trimmed_cmd = cmd.strip().lower()
        parts = trimmed_cmd.split(' ')
        command = parts[0]
        args = parts[1:]

        # Comandos definidos, similar a tu objeto `commands` en React.
        projects = [
            'ecommerce-platform',
            'task-manager',
            'weather-dashboard'
        ]
        
        output = []

        if command == "help":
            output = [
                'Comandos disponibles:',
                '  help                  - Muestra esta ayuda',
                '  clear                 - Limpia la terminal',
                '  ls [directorio]       - Lista contenido del directorio',
                '  cd <directorio>       - Cambia de directorio',
                '  cd ..                 - Retrocede un directorio',
                '  cat aboutme.txt       - Muestra mi biografía',
                '  contact --email       - Abre el formulario de contacto',
                '  whoami                - Información básica',
                '  pwd                   - Directorio actual',
                '  date                  - Fecha y hora actual',
                '',
                'Ejemplos:',
                '  cd projects           - Ir a la sección de proyectos',
                '  ls projects           - Listar todos los proyectos'
            ]
        elif command == "clear":
            self.history = []
            return []
        elif command == "ls":
            # Lógica para listar directorios.
            current_path = self.current_path
            if not args or (args[0] == "projects" and current_path == "home"):
                if current_path == "home":
                    output = ['aboutme.txt', 'projects/', 'contact/', '']
                elif current_path == "projects":
                    output = [f'{p}/' for p in projects] + ['']
                else:
                    output = ["Directorio vacío"]
            else:
                 output = [f"Directorio no encontrado: {args[0]}"]
        elif command == "cd":
            if not args or args[0] == "home":
                self.navigation_stack = []
                self.current_section = "home"
                output = ["Navegando a directorio home..."]
            elif args[0] == "..":
                if self.navigation_stack:
                    self.navigation_stack.pop()
                    self.current_section = self.current_path
                    output = [f"Navegando a {self.current_path}..."]
                else:
                    output = ["Ya estás en el directorio raíz"]
            elif args[0] == "projects":
                self.navigation_stack = ["projects"]
                self.current_section = "projects"
                output = ["Navegando a sección de proyectos..."]
            elif args[0] == "about":
                self.navigation_stack = ["about"]
                self.current_section = "about"
                output = ["Navegando a biografía..."]
            elif args[0] == "contact":
                self.navigation_stack = ["contact"]
                self.current_section = "contact"
                output = ["Navegando a contacto..."]
            elif self.current_path == "projects" and args[0] in projects:
                self.navigation_stack.append(args[0])
                self.current_section = "project_detail"
                output = [f"Navegando a proyecto {args[0]}..."]
            else:
                output = [f"Directorio no encontrado: {args[0]}"]
        elif trimmed_cmd == "cat aboutme.txt":
            self.current_section = "about"
            self.navigation_stack = ["about"]
            output = ["Cargando biografía..."]
        elif trimmed_cmd == "contact --email":
            self.current_section = "contact"
            self.navigation_stack = ["contact"]
            output = ["Abriendo formulario de contacto..."]
        elif trimmed_cmd == "whoami":
            output = [
                'Desarrollador Full Stack',
                'Especializado en Reflex y tecnologías web modernas'
            ]
        elif trimmed_cmd == "pwd":
            output = [self.prompt_path]
        elif trimmed_cmd == "date":
            output = [datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')]
        else:
            output = [f"Comando no encontrado: {trimmed_cmd}. Escribe 'help' para ver los comandos disponibles."]

        # Manejamos un caso especial para el comando `clear`
        if trimmed_cmd == "clear":
            self.history = []
            return []
        
        return output

    def set_current_section(self, section: str):
        """Método para cambiar la sección desde los botones."""
        self.current_section = section
        # Ajustamos el navigation_stack para que sea consistente con la sección actual
        if section == "home":
            self.navigation_stack = []
        else:
            self.navigation_stack = [section]

# --- 2. Componentes de la Interfaz (UI) ---
# Recreamos el JSX y Tailwind CSS con componentes y estilos de Reflex.

def terminal_header() -> rx.Component:
    """Componente para la cabecera de la terminal."""
    return rx.box(
        rx.hstack(
            rx.box(width="0.75rem", height="0.75rem", background_color="blue"),
            rx.box(width="0.75rem", height="0.75rem", background_color="yellow"),
            rx.box(width="0.75rem", height="0.75rem", background_color="green"),
            # Corrección: El spacing debe ser un valor numérico como string.
            spacing="2",
        ),
        rx.text("portfolio-terminal", color="gray", font_size="0.875rem", margin_left="0.5rem"),
        background_color="#222222",
        border_bottom="1px solid #444444",
        padding_x="1rem",
        padding_y="0.5rem",
        display="flex",
        align_items="center",
        gap="0.5rem",
    )

def terminal_output() -> rx.Component:
    """Componente para mostrar el historial de la terminal."""
    return rx.box(
        rx.foreach(
            TerminalState.history,
            lambda line: rx.text(
                line["content"],
                color=rx.cond(
                    line["type"] == "error",
                    "red",
                    rx.cond(
                        line["type"] == "input",
                        "lime",
                        rx.cond(
                            line["type"] == "system",
                            "gray",
                            "lime",
                        ),
                    ),
                ),
            ),
        ),
        # Simulamos el scroll de la terminal.
        on_mount=lambda: rx.scroll_to(
            f"bottom_{random.randint(0, 1000)}"
        ),
        padding="1rem",
        overflow_y="auto",
        height="100%",
        max_height="calc(100% - 3rem)",
    )

def terminal_input() -> rx.Component:
    """Componente para la línea de entrada de la terminal."""
    return rx.form(
        rx.hstack(
            rx.text(
                f"portfolio:{TerminalState.prompt_path}$",
                color="lime",
            ),
            rx.input(
                value=TerminalState.current_input,
                on_change=TerminalState.set_current_input,
                on_key_up=TerminalState.handle_key_up,
                placeholder="",
                border_color="transparent",
                background_color="transparent",
                color="lime",
                flex_grow=1,
                font_family="monospace",
                _focus={"outline": "none"},
            ),
            # Se ha corregido 'rx.span' a 'rx.text'
            rx.text("_", color="lime", animation="blink 1s step-end infinite;"),
        ),
        on_submit=TerminalState.handle_submit,
        width="100%",
        padding_x="1rem",
        padding_bottom="1rem",
    )

def terminal_component() -> rx.Component:
    """Componente principal de la terminal."""
    return rx.vstack(
        terminal_header(),
        terminal_output(),
        terminal_input(),
        align_items="start",
        spacing="0",
        background_color="black",
        border="1px solid lime",
        border_radius="0.5rem",
        overflow="hidden",
        width="100%",
        height="100%",
    )

# --- 3. Componentes de la interfaz completa ---
# Aquí se define el layout completo, incluyendo la terminal y los otros bloques.

def sidebar_menu() -> rx.Component:
    """Bloque de botones de navegación."""
    return rx.vstack(
        rx.button("Inicio", on_click=TerminalState.set_current_section("home")),
        rx.button("Sobre Mi", on_click=TerminalState.set_current_section("about")),
        rx.button("Proyectos", on_click=TerminalState.set_current_section("projects")),
        rx.button("Contacto", on_click=TerminalState.set_current_section("contact")),
        spacing="4",
    )

def home_content() -> rx.Component:
    """Bloques de información de la página principal."""
    return rx.grid(
        rx.box("Bloque 1", border="1px solid lime", padding="4"),
        rx.box("Bloque 2", border="1px solid lime", padding="4"),
        rx.box("Bloque 3", border="1px solid lime", padding="4"),
        rx.box("Bloque 4", border="1px solid lime", padding="4"),
        columns="2",
        spacing="4",
        width="100%",
    )

def about_content() -> rx.Component:
    """Contenido para la sección 'Sobre Mí'."""
    return rx.box(
        rx.text("Aquí va el contenido de 'Sobre Mí'.")
    )

def projects_content() -> rx.Component:
    """Contenido para la sección 'Proyectos'."""
    return rx.box(
        rx.text("Aquí va el contenido de 'Proyectos'.")
    )

def contact_content() -> rx.Component:
    """Contenido para la sección 'Contacto'."""
    return rx.box(
        rx.text("Aquí va el contenido de 'Contacto'.")
    )

def main_content_area() -> rx.Component:
    """Área principal que cambia según la sección actual."""
    return rx.cond(
        TerminalState.current_section == "home",
        home_content(),
        rx.cond(
            TerminalState.current_section == "about",
            about_content(),
            rx.cond(
                TerminalState.current_section == "projects",
                projects_content(),
                rx.cond(
                    TerminalState.current_section == "contact",
                    contact_content(),
                    rx.box(rx.text("Sección no encontrada")),
                )
            )
        )
    )

def main_layout() -> rx.Component:
    """Layout principal de la página, unificando todos los componentes."""
    return rx.hstack(
        # Columna izquierda: Menú y Terminal
        rx.vstack(
            rx.box(sidebar_menu(), border="1px solid lime", padding="4"),
            rx.box(terminal_component(), flex_grow=1),
            spacing="4",
            width="50%",
        ),
        # Columna derecha: Bloques de información que cambian dinámicamente
        rx.vstack(
            main_content_area(),
            width="50%",
        ),
        spacing="4",
        padding="4",
        width="100%",
        height="100vh",
    )