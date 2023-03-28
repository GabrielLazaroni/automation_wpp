import pynecone as pc
from styles import login_styles, register_styles
from components import login_components, register_components
from helpers.db import user_helper


def index():
    register_container = pc.container(
        pc.form_control(
            pc.vstack(register_components.label_component,
                      register_components.load_input("Nome", "text"),
                      register_components.load_input("Email", "email"),
                      register_components.load_input("Senha", "password"),
                      register_components.load_button("Cadastrar"),
                      register_components.footer_text,
                      style=register_styles.vstack_style,
                      ),
            style=register_styles.register_container_style,
        )
    )

    _main = pc.container(
        register_container,
        id='/',
        center_content=True,
        justifyContent='center',
        maxWidth='auto',
        height='100vh',
        bg='#143A34'

    )
    return _main


def login():
    login_container = pc.container(
        pc.form_control(
            pc.vstack(
                login_components.label_component,
                login_components.load_input("Nome", "text"),
                login_components.load_input("Senha", "password"),
                login_components.load_button("Login"),
                login_components.footer_text,
                style=login_styles.vstack_style),
            style=login_styles.login_container_style,
        )
    )

    _main = pc.container(
        login_container,
        id='login',
        center_content=True,
        justifyContent='center',
        maxWidth='auto',
        height='100vh',
        bg='#143A34'
    )
    return _main


# Add state and page to the app.
app = pc.App(stylesheets=[
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap",
],)
app.add_page(index, route='/')
app.add_page(login, route='/login')
app.compile()
