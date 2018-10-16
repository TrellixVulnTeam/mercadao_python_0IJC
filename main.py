from Interface import Interface as GUI
def campos_estao_preenchidos(*campos):
    for campo in campos:
        if len(campo.get()) <= 0 or campo.get() == "":
            return False
    return True

tela = GUI(800, 500)

# titulo da pagina
tela.label(30, 20, "Mercadão Python", font=("Arial", 20))

tela.label(30, 60, "Cadastro de produtos", font=("Arial", 12))

tela.label(30, 100, "Codigo: ")
codigo_produto = tela.entry(200, 100, 30)

tela.label(30, 140, "Descrição: ")
descricao_produto = tela.entry(200, 140, 30)

tela.label(30, 180, "Preço unitário: ")
preco_produto = tela.entry(200, 180, 30)

tela.label(30, 220, "Unidade de medida: ")
radio_unidade_produto = tela.radio_group(200, 200, ["Un", "Kg", "M", "PC"])

tela.button(280, 320, "Cadastrar produto")

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
    print(campos_estao_preenchidos(nome_cliente, cpf_cliente, email_cliente, telefone_cliente))
))
tela.start()


