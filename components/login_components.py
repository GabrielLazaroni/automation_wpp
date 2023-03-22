import pynecone as pc
from styles import login_styles
from helpers.validations import login_form


label_component = pc.text("Cadastrar", style=login_styles.label_style)


def load_button(text):
    return pc.button(
        text, style=login_styles.button_style)


def load_input(text, type_input):
    return pc.input(placeholder=text, style=login_styles.input_style, type_=type_input, is_required=True)
