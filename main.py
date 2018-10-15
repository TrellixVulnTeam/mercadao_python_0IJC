from Interface import Interface as GUI

tela = GUI(800, 500)

# titulo da pagina
tela.label(30, 20, "Mercadão Python", font=("Arial", 20))

tela.label(30, 60, "Cadastro de produtos", font=("Arial", 12))

tela.label(30, 100, "Codigo: ")
codigo = tela.entry(200, 100, 30)

tela.label(30, 140, "Descrição: ")
descricao = tela.entry(200, 140, 30)

tela.label(30, 180, "Preço unitário: ")
preco = tela.entry(200, 180, 30)

tela.label(30, 220, "Unidade de medida")
radio_unidade = tela.radio_group(200, 200, ["Un", "Kg", "M", "PC"])

tela.button(280, 320, "Cadastrar produto")
tela.start()
