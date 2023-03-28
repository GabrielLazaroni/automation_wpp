import pynecone as pc
from styles import login_styles
from helpers.validations import login_form


label_component = pc.text("Entrar", style=login_styles.label_style)

footer_text = pc.text(
    'Nao e casdatrado? ',
    pc.link("Cadastre-se",
            href='/',
            is_external=True,
            style=login_styles.footer_text),
)


def load_button(text):
    return pc.button(
        text, style=login_styles.button_style)


def load_input(text, type_input):
    return pc.input(placeholder=text, style=login_styles.input_style, focus_border_color='#5f837d', error_border_color='#FF0000', type_=type_input, is_required=True)
