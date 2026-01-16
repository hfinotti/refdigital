from refdigital import database, app
from refdigital.models import Usuario, Faq, Cliente, Servico


with app.app_context():
    database.drop_all()
    database.create_all()