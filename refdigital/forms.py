from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from refdigital.models import Usuario


# Formularios da seção Login
class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    manter_login = BooleanField('Manter Dados')
    botao_login = SubmitField('Fazer Login')


class FormCriarConta(FlaskForm):
    nome = StringField('Nome do Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    confirma_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_criarconta = SubmitField('Criar Conta')

    def validade_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar.")


# Formularios da seção FAQ
class FormCriarFaq(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    resposta = TextAreaField('Resposta', validators=[DataRequired()], render_kw={"rows": 7})
    botao_criarfaq = SubmitField('Criar Faq')


class FormEditarFaq(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    resposta = TextAreaField('Resposta', validators=[DataRequired()], render_kw={"rows": 5})
    botao_editarfaq = SubmitField('Editar Faq')


# Formulários da seção Resultados
class FormCriarResultado(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    texto_titulo = TextAreaField('Texto do Título', validators=[DataRequired()], render_kw={"rows": 3})
    subtitulo1 = StringField('Subtítulo 1')
    texto_subt1 = TextAreaField('Texto do Subtítulo 1', render_kw={"rows": 2})
    subtitulo2 = StringField('Subtítulo 2')
    texto_subt2 = TextAreaField('Texto do Subtítulo 2', render_kw={"rows": 2})
    subtitulo3 = StringField('Subtítulo 3')
    texto_subt3 = TextAreaField('Texto do Subtítulo 3', render_kw={"rows": 2})
    botao_criarresultado = SubmitField('Criar Resultado')


class FormEditarResultado(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    texto_titulo = TextAreaField('Texto do Título', validators=[DataRequired()], render_kw={"rows": 3})
    subtitulo1 = StringField('Subtítulo 1')
    texto_subt1 = TextAreaField('Texto do Subtítulo 1', render_kw={"rows": 2})
    subtitulo2 = StringField('Subtítulo 2')
    texto_subt2 = TextAreaField('Texto do Subtítulo 2', render_kw={"rows": 2})
    subtitulo3 = StringField('Subtítulo 3')
    texto_subt3 = TextAreaField('Texto do Subtítulo 3', render_kw={"rows": 2})
    botao_editarresultado = SubmitField('Editar Card de Resultados')


# Formularios da seção Cliente
class FormCriarCliente(FlaskForm):
    empresa = StringField('Empresa', validators=[DataRequired()])
    nome = StringField('Nome')
    cargo = StringField('Cargo')
    logo = FileField('Incluir logomarca', validators=[FileAllowed(['jpg', 'png'])])
    botao_criarcliente = SubmitField('Criar Cliente')


class FormEditarCliente(FlaskForm):
    empresa = StringField('Empresa', validators=[DataRequired()])
    nome = StringField('Nome')
    cargo = StringField('Cargo')
    logo = FileField('Atualizar logomarca', validators=[FileAllowed(['jpg', 'png'])])
    botao_editarcliente = SubmitField('Editar Cliente')


# Formularios da seção Serviços
class FormCriarServico(FlaskForm):
    servico = StringField('Serviço', validators=[DataRequired()])
    descricao = StringField('Descrição', validators=[DataRequired()])
    botao_criarservico = SubmitField('Criar Serviço')


class FormEditarServico(FlaskForm):
    servico = StringField('Serviço', validators=[DataRequired()])
    descricao = StringField('Descrição', validators=[DataRequired()])
    botao_editarservico = SubmitField('Editar Serviço')


