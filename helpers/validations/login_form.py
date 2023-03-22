import pynecone as pc


def form_validate(value):
    if not value:
        return pc.alert(
            pc.alert_icon(),
            pc.alert_title("Nome invalido!")
        )
