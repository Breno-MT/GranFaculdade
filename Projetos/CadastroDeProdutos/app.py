from models.Produto import Produto
from models.Categoria import Categoria

def menu():
    print()
    print('1 - Listar Produtos')
    print('2 - Inserir Produtos')
    print('3 - Alterar Produtos')
    print('4 - Excluir Produtos')
    print('0 - Sair')
    print()

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            Produto.listar_todos()
        case 2:
            codigo = input('Digite o código: ')
            nome = input('Digite o nome: ')
            quantidade = input('Digite a quantidade: ')
            valor = input('Digite o valor: ')

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
        case 3:
            Produto.listar_todos()
            selecionado = int(input('Qual item deseja alterar? '))
            item = Produto.ler_arquivo(selecionado)

            quantidade = int(input('Qual a nova quantidade: '))
            valor = int(input('Qual o novo valor: '))

            produto = Produto(item['codigo'], item['nome'], quantidade, valor)
            produto.atualizar(selecionado)

            print('Produto atualizado: ', produto.detalhar())
        case 4:
            Produto.listar_todos()
            selecionado = int(input('Qual item deseja excluir? '))

            Produto.deletar(selecionado)

            Produto.listar_todos()

