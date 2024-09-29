import json
import os

# Nome do JSON onde os dados serão armazenados
arquivo_produtos = "produtos.json"


# carregar os produtos do arquivo JSON
def carregar_produtos():
    if os.path.exists(arquivo_produtos):
        with open(arquivo_produtos, "r") as file:
            return json.load(file)
    return []


# salvar os produtos no JSON
def salvar_produtos():
    with open(arquivo_produtos, "w") as file:
        json.dump(produtos, file, indent=4)


# adicionar produto
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    salvar_produtos()
    print(f"Produto '{nome}' adicionado com sucesso!")


# listar os produtos
def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de produtos cadastrados:")
        for idx, produto in enumerate(produtos):
            print(f"{idx + 1}> Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")


# buscar um produto pelo nome
def buscar_produto():
    nome = input("Digite o nome do produto que deseja buscar: ")
    encontrado = False
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            print(
                f"Produto encontrado - Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
            encontrado = True
            break
    if not encontrado:
        print(f"Produto '{nome}' não encontrado.")


# editar um produto
def editar_produto():
    listar_produtos()
    if not produtos:
        return
    try:
        indice = int(input("Digite o número do produto que deseja editar: ")) - 1
        if 0 <= indice < len(produtos):
            produto = produtos[indice]
            print(f"Editando produto: {produto['nome']}")
            produto['nome'] = input(f"Novo nome (atual: {produto['nome']}): ") or produto['nome']
            produto['preco'] = float(input(f"Novo preço (atual: {produto['preco']}): ") or produto['preco'])
            produto['quantidade'] = int(
                input(f"Nova quantidade (atual: {produto['quantidade']}): ") or produto['quantidade'])
            salvar_produtos()
            print(f"Produto '{produto['nome']}' atualizado com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")


# Menu principal
def menu():
    while True:
        print("\nSistema de Cadastro de Produtos")
        print("1-> Adicionar Produto")
        print("2-> Listar Produtos")
        print("3-> Buscar Produto")
        print("4-> Editar Produto")
        print("9-> Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            buscar_produto()
        elif opcao == '4':
            editar_produto()
        elif opcao == '9':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    # variável global para armazenar os produtos carregando do JSON
    produtos = carregar_produtos()
    # executar o menu
    menu()
