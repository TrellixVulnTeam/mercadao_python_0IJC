from Interface import Interface as GUI
from Database import Database_manager as db_manager


def campos_estao_preenchidos(*campos):
    for campo in campos:
        if isinstance(campo, GUI.get_entry_class()):
            if len(campo.get()) <= 0 or campo.get() == "":
                return False
    return True


def limpar_campos(*campos):
    for campo in campos:
        if isinstance(campo, GUI.get_entry_class()):
            campo.delete(0, len(campo.get()))


def cadastrar_cliente():
    if campos_estao_preenchidos(nome_cliente, cpf_cliente, email_cliente, telefone_cliente):
        db = db_manager()
        db.insert_into_clientes(nome_cliente.get(),
                                cpf_cliente.get(),
                                email_cliente.get(),
                                telefone_cliente.get())
    else:
        print("campos não estão preenchidos")


def cadastrar_produto():
    if campos_estao_preenchidos(codigo_produto, descricao_produto, preco_produto):
        # TODO cadastro de produto no banco de dados
        pass
    else:
        print("campos não estão preenchidos")


tela = GUI(800, 500)

# titulo da pagina
tela.label(30, 20, "Mercadão Python", font=("Arial", 20))

# cadastro de produtos
tela.label(30, 60, "Cadastro de produtos", font=("Arial", 12))

tela.label(30, 100, "Codigo: ")
codigo_produto = tela.entry(200, 100, 30)

tela.label(30, 140, "Descrição: ")
descricao_produto = tela.entry(200, 140, 30)

tela.label(30, 180, "Preço unitário: ")
preco_produto = tela.entry(200, 180, 30)

tela.label(30, 220, "Unidade de medida: ")
radio_unidade_produto = tela.radio_group(200, 200, ["Un", "Kg", "M", "PC"])

tela.button(280, 320, "Cadastrar produto", command=lambda: (
    cadastrar_produto,
    limpar_campos(codigo_produto, descricao_produto, preco_produto)
))
tela.button(170, 320, "Limpar campos", command=lambda: limpar_campos(codigo_produto, descricao_produto, preco_produto))

# cadastro de clientes
tela.label(450, 60, "Cadastro de clientes", font=("Arial", 12))

tela.label(450, 100, "Nome: ")
nome_cliente = tela.entry(580, 100, 30)

tela.label(450, 140, "CPF: ")
cpf_cliente = tela.entry(580, 140, 30)

tela.label(450, 180, "email: ")
email_cliente = tela.entry(580, 180, 30)

tela.label(450, 220, "telefone: ")
telefone_cliente = tela.entry(580, 220, 30)

tela.button(660, 320, "Cadastrar cliente", command=lambda: (
    cadastrar_cliente,
    limpar_campos(nome_cliente, cpf_cliente, email_cliente, telefone_cliente)
))

tela.button(550, 320, "Limpar Campos",
            command=lambda: limpar_campos(nome_cliente, cpf_cliente, email_cliente, telefone_cliente))

tela.start()
