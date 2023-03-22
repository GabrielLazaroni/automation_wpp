from models import user_model
import pynecone as pc


def create_user(name, password, email):
    with pc.session() as session:
        session.add(
            user_model.User(
                name,
                password,
                email
            )
        )
    session.commit()
