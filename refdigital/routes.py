from flask import render_template, url_for, redirect, flash, request, abort
from refdigital import app, bcrypt, database
from flask_login import login_required, login_user, logout_user, current_user
from refdigital.forms import FormLogin, FormCriarConta, FormEditarFaq, FormCriarFaq, FormEditarResultado, FormCriarResultado, FormCriarCliente, FormEditarCliente, FormCriarServico, FormEditarServico
from refdigital.models import Usuario, Faq, Resultado, Servico, Cliente
from PIL import Image
import secrets
import os

@app.route("/")
def home():
    logo = url_for('static', filename='imagens/r.png')
    font = url_for('static', filename='fonts/monda.otf')
    faqs = Faq.query.all()
    resultados = Resultado.query.all()
    clientes =  Cliente.query.all()
    servicos =  Servico.query.order_by(Servico.id.desc()).limit(4).all()
    number = "5534991059999"
    message = "Olá! Gostaria de mais informações sobre seus serviços."
    whatsapp_link = f"https://wa.me/{number}?text={message.replace(' ', '%20')}"
    return render_template('home.html', logo=logo, font=font, faqs=faqs, resultados=resultados, clientes=clientes, servicos=servicos, whatsapp_link=whatsapp_link)


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.manter_login.data)
            flash('Login efetuado com suceesso!', 'alert-success')
            return redirect(url_for("principal"))
        else:
            flash('Falha do login, e-mail ou senha invalidos!', 'alert-danger')
    return render_template("admin.html", form_login=form_login)


@app.route("/criarconta", methods=['GET', 'POST'])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha_crypt = bcrypt.generate_password_hash(form_criarconta.senha.data).decode('utf-8')
        usuario = Usuario(nome=form_criarconta.nome.data, email=form_criarconta.email.data, senha=senha_crypt)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        flash('Usuário criado com sucesso!', 'alert-success')
        return redirect(url_for("principal"))

    return render_template('criarconta.html', form_criarconta=form_criarconta)


@app.route("/principal")
@login_required
def principal():
    return render_template('principal.html')


@app.route("/faq")
@login_required
def faq():
    faqs = Faq.query.order_by(Faq.id.desc()).all()
    return render_template('faq.html', faqs=faqs)


@app.route('/criarfaq', methods=["GET", "POST"])
@login_required
def criar_faq():
    form = FormCriarFaq()
    if form.validate_on_submit():
        faq = Faq(titulo=form.titulo.data, resposta=form.resposta.data)
        database.session.add(faq)
        database.session.commit()
        flash('Faq criada com sucesso!', 'alert-success')
        return redirect(url_for("faq"))

    return render_template('criarfaq.html', form=form)


@app.route('/editarfaq/<faq_id>', methods=["GET", "POST"])
@login_required
def editar_faq(faq_id):
    faq = Faq.query.get(faq_id)
    if faq:
        form = FormEditarFaq()
        if request.method == "GET":
            form.titulo.data = faq.titulo
            form.resposta.data = faq.resposta
        elif form.validate_on_submit():
            faq.titulo = form.titulo.data
            faq.resposta = form.resposta.data
            database.session.commit()
            flash('Faq atualizada com sucesso!', 'alert-success')
            return redirect(url_for("faq"))
    else:
        form = None
    return render_template("editarfaq.html", form=form, faq_id=faq_id)


@app.route('/faq/<faq_id>/excluir', methods=["GET", "POST"])
@login_required
def excluir_faq(faq_id):
    faq = Faq.query.get(faq_id)
    if faq:
        database.session.delete(faq)
        database.session.commit()
        flash('Faq deletada com sucesso!', 'alert-danger')
        return redirect(url_for("faq"))
    else:
        abort(403)



@app.route("/resultado")
@login_required
def resultado():
    resultados = Resultado.query.order_by(Resultado.id.desc()).all()
    return render_template('resultado.html', resultados=resultados)


@app.route('/criarresultado', methods=["GET", "POST"])
@login_required
def criar_resultado():
    form = FormCriarResultado()
    if form.validate_on_submit():
        resultado = Resultado(titulo=form.titulo.data,texto_titulo=form.texto_titulo.data,subtitulo1=form.subtitulo1.data,texto_subt1=form.texto_subt1.data,subtitulo2=form.subtitulo2.data,texto_subt2=form.texto_subt2.data,subtitulo3=form.subtitulo3.data,texto_subt3=form.texto_subt3.data)
        database.session.add(resultado)
        database.session.commit()
        flash('Resultado criado com sucesso!', 'alert-success')
        return redirect(url_for("resultado"))

    return render_template('criarresultado.html', form=form)


@app.route('/editarresultado/<resultado_id>', methods=["GET", "POST"])
@login_required
def editar_resultado(resultado_id):
    resultado = Resultado.query.get(resultado_id)
    if resultado:
        form = FormEditarResultado()
        if request.method == "GET":
            form.titulo.data = resultado.titulo
            form.texto_titulo.data = resultado.texto_titulo
            form.subtitulo1.data = resultado.subtitulo1
            form.texto_subt1.data = resultado.texto_subt1
            form.subtitulo2.data = resultado.subtitulo2
            form.texto_subt2.data = resultado.texto_subt2
            form.subtitulo3.data = resultado.subtitulo3
            form.texto_subt3.data = resultado.texto_subt3
        elif form.validate_on_submit():
            resultado.titulo = form.titulo.data
            resultado.texto_titulo = form.texto_titulo.data
            resultado.subtitulo1 = form.subtitulo1.data
            resultado.texto_subt1 = form.texto_subt1.data
            resultado.subtitulo2 = form.subtitulo2.data
            resultado.texto_subt2 = form.texto_subt2.data
            resultado.subtitulo3 = form.subtitulo3.data
            resultado.texto_subt3 = form.texto_subt3.data
            database.session.commit()
            flash('Resultado atualizado com sucesso!', 'alert-success')
            return redirect(url_for("resultado"))
    else:
        form = None
    return render_template("editarresultado.html", form=form, resultado_id=resultado_id)


@app.route('/resultado/<resultado_id>/excluir', methods=["GET", "POST"])
@login_required
def excluir_resultado(resultado_id):
    resultado = Resultado.query.get(resultado_id)
    if resultado:
        database.session.delete(resultado)
        database.session.commit()
        flash('Resultado deletado com sucesso!', 'alert-danger')
        return redirect(url_for("resultado"))
    else:
        abort(403)


def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, r'static/imagens_cliente', nome_arquivo)
    tamanho = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)

    return nome_arquivo


@app.route("/cliente")
@login_required
def cliente():
    clientes = Cliente.query.order_by(Cliente.id.desc()).all()
    return render_template('cliente.html', clientes=clientes)


@app.route('/criarcliente', methods=["GET", "POST"])
@login_required
def criar_cliente():
    form = FormCriarCliente()
    if form.validate_on_submit():
        if form.logo.data:
            logo = salvar_imagem(form.logo.data)
        else:
            logo = "default.png"
        cliente = Cliente(empresa=form.empresa.data, nome=form.nome.data, cargo=form.cargo.data, logo=logo)
        database.session.add(cliente)
        database.session.commit()
        flash('Cliente criado com sucesso!', 'alert-success')
        return redirect(url_for("cliente"))

    return render_template('criarcliente.html', form=form)


@app.route('/editarcliente/<cliente_id>', methods=["GET", "POST"])
@login_required
def editar_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        form = FormEditarCliente()
        if request.method == "GET":
            form.empresa.data = cliente.empresa
            form.nome.data = cliente.nome
            form.cargo.data = cliente.cargo
            form.logo.data = cliente.logo
        elif form.validate_on_submit():
            cliente.empresa = form.empresa.data
            cliente.nome = form.nome.data
            cliente.cargo = form.cargo.data
            if cliente.logo != "default.png":
                caminho_imagem = os.path.join(app.root_path.strip(), 'static/imagens_cliente', cliente.logo)
                if os.path.exists(caminho_imagem):
                    os.remove(caminho_imagem)
            if form.logo.data:
                cliente.logo = salvar_imagem(form.logo.data)
            database.session.commit()
            flash('Cliente atualizado com sucesso!', 'alert-success')
            return redirect(url_for("cliente"))
    else:
        form = None
    return render_template("editarcliente.html", form=form, cliente_id=cliente_id)


@app.route('/cliente/<cliente_id>/excluir', methods=["GET", "POST"])
@login_required
def excluir_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        if cliente.logo != "default.png":
            caminho_imagem = os.path.join(app.root_path.strip(), r'static/imagens_cliente', cliente.logo)
            if os.path.exists(caminho_imagem):
                os.remove(caminho_imagem)
        database.session.delete(cliente)
        database.session.commit()
        flash('Cliente deletado com sucesso!', 'alert-danger')
        return redirect(url_for("cliente"))
    else:
        abort(403)


@app.route("/servico")
@login_required
def servico():
    servicos = Servico.query.order_by(Servico.id.desc()).all()
    return render_template('servico.html', servicos=servicos)


@app.route('/criarservico', methods=["GET", "POST"])
@login_required
def criar_servico():
    form = FormCriarServico()
    if form.validate_on_submit():
        servico = Servico(servico=form.servico.data, descricao=form.descricao.data)
        database.session.add(servico)
        database.session.commit()
        flash('Servico criado com sucesso!', 'alert-success')
        return redirect(url_for("servico"))

    return render_template('criarservico.html', form=form)


@app.route('/editarservico/<servico_id>', methods=["GET", "POST"])
@login_required
def editar_servico(servico_id):
    servico = Servico.query.get(servico_id)
    if faq:
        form = FormEditarServico()
        if request.method == "GET":
            form.servico.data = servico.servico
            form.descricao.data = servico.descricao
        elif form.validate_on_submit():
            servico.servico = form.servico.data
            servico.descricao = form.descricao.data
            database.session.commit()
            flash('Servico atualizado com sucesso!', 'alert-success')
            return redirect(url_for("servico"))
    else:
        form = None
    return render_template("editarservico.html", form=form, servico_id=servico_id)


@app.route('/servico/<servico_id>/excluir', methods=["GET", "POST"])
@login_required
def excluir_servico(servico_id):
    servico = Servico.query.get(servico_id)
    if servico:
        database.session.delete(servico)
        database.session.commit()
        flash('Servico deletado com sucesso!', 'alert-danger')
        return redirect(url_for("servico"))
    else:
        abort(403)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))



