import pynecone as pc
from styles import register_styles
from helpers.validations import login_form
from name import name


label_component = pc.text("Cadastrar", style=register_styles.label_style)


footer_text = pc.text(
    'Ja tem cadastro?',
    pc.link("Login.",
            href='/login',
            is_external=True,
            style=register_styles.footer_text),
)


def load_button(text):
    return pc.button(
        text, style=register_styles.button_style)


def load_input(text, type_input):
    return pc.input(placeholder=text, style=register_styles.input_style, focus_border_color='#5f837d', error_border_color='#FF0000', type_=type_input, is_required=True)
