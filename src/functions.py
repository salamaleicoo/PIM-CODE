import os

def cadastrar(listall):
    os.system('cls')
    print('----------CADASTRAR ITEM----------')
    try:
        id = len(listall) + 1

        while True:
            nome = input('Insira o nome do item: ').strip()
            if not nome:
                print('Erro! Nome não pode estar vazio!')
            elif len(nome) > 100:
                print('Erro! Nome excede 100 caracteres!')
            else:
                break

        while True:
            desc = input('Insira uma descrição (limite de 300 caracteres): ').strip()
            if not desc:
                print('Erro! Descrição não pode estar vazia!')
            elif len(desc) > 300:
                print('Erro! Descrição excede 300 caracteres!')
            else:
                break

        while True:
            try:
                valor = float(input('Digite o valor em Reais: '))
                if valor < 0:
                    print('Erro! Valor deve ser positivo!')
                else:
                    break
            except ValueError:
                print('Erro! Valor deve ser um número válido!')

        while True:
            try:
                qtd = int(input('Digite a Quantidade: '))
                if qtd <= 0:
                    print('Erro! Quantidade deve ser maior que zero(0)!')
                elif qtd > 1000:
                    print('Erro! Quantidade maior que 1000!')
                else:
                    break
            except ValueError:
                print('Erro! Quantidade deve ser um número inteiro válido!')

        while True:
            try:
                nota_fiscal = int(input('Digite o número da Nota Fiscal(NF): '))
                if len(str(nota_fiscal)) > 44:
                    print('Erro! Nota Fiscal excede 44 caracteres!')
                else:
                    break
            except ValueError:
                print('Erro! Valor deve ser um número válido!')
        while True:
            ativo = input('Este produto é ativo? (S/N): ').strip().upper()
            if ativo in ['S', 'N']:
                break
            else:
                print('Erro! Responda somente com "S" para sim ou "N" para não.')

        produto = {
            'id': id,
            'nome': nome,
            'desc': desc,
            'valor': valor,
            'qnt': qtd,
            'notaF': nota_fiscal,
            'ativo': ativo
        }

        listall.append(produto)
        print(f'Ativo cadastrado com sucesso!')
        print('Id:', produto['id'])
        print('Nome:', produto['nome'])
        print('Descrição:', produto['desc'])
        print('Valor:', produto['valor'])
        print('Quantidade:', produto['qnt'])
        print('Nota Fiscal:', produto['notaF'])
        print('Ativo:', produto['ativo'])
        input('Pressione Enter para continuar...')

    except Exception as e:
        print(f'Erro inesperado: {e}')
        input('Pressione Enter para continuar...')

import os

def consultar(listall, isAlterar: bool = False, isExcluir: bool = False):
    if not listall:
        print('Você não cadastrou nenhum produto ainda!')
        input("Pressione Enter para sair...")
        return

    repeat = 'S'
    while repeat != 'N':
        os.system('cls')

        if isAlterar:
            selectedProduct = int(input('Insira o id do produto que deseja alterar: '))
        elif isExcluir: 
            selectedProduct = int(input('Insira o id do produto que deseja excluir: '))
        else:
            selectedProduct = int(input('Insira o id do produto que deseja consultar: '))

        produto_encontrado = next((p for p in listall if p['id'] == selectedProduct), None)

        if produto_encontrado:
            if isAlterar or isExcluir:
                return produto_encontrado
            else:
                print(f'Produto encontrado')
                print('Id:', produto_encontrado['id'])
                print('Nome:', produto_encontrado['nome'])
                print('Descrição:', produto_encontrado['desc'])
                print('Valor:', produto_encontrado['valor'])
                print('Quantidade:', produto_encontrado['qnt'])
                print('Nota Fiscal:', produto_encontrado['notaF'])
                print('Ativo:', produto_encontrado['ativo'])
        else:
            print('Produto não encontrado.')

        repeat = input('Deseja procurar novamente? (S/N): ').strip().upper()

def alterar(listall):
    os.system('cls')

    produto = consultar(listall, True)
    if produto:
        while True:
            try:
                acao = int(input(f'''
Qual item você deseja alterar?
1 - Nome: {produto['nome']}
2 - Descrição: {produto['desc']}
3 - Valor: {produto['valor']}
4 - Quantidade: {produto['qnt']}
5 - Nota Fiscal: {produto['notaF']}
6 - Ativo: {produto['ativo']}
0 - Salvar
'''))
            except ValueError:
                print("Digite um número válido.")
                continue

            if acao == 0:
                print("Alterações concluídas.")
                input('Pressione ENTER para sair...')
                break

            campos = {
                1: 'nome',
                2: 'desc',
                3: 'valor',
                4: 'qnt',
                5: 'notaF',
                6: 'ativo'
            }

            if acao not in campos:
                print("Opção inválida.")
                continue

            campo = campos[acao]
            atual = produto[campo]
            novoValor = input(f'Digite um novo valor (atual: {atual}): ')

            if len(str(novoValor)) == 0:
                print('Não podem ser inseridos valores vazios!')
                continue

            if campo == 'valor':
                try:
                    novoValor = float(novoValor)
                except ValueError:
                    print("Valor inválido. Deve ser numérico (ex: 10.99).")
                    continue
            elif campo == 'qnt':
                try:
                    novoValor = int(novoValor)
                except ValueError:
                    print("Quantidade inválida. Deve ser um número inteiro.")
                    continue
            elif campo == 'ativo':
                novoValor = novoValor.strip().upper()
                if novoValor not in ['S', 'N']:
                    print("Valor inválido para 'ativo'. Use 'S' (sim) ou 'N' (não).")
                    continue
            elif campo == 'notaF':
                try:
                    novoValor = int(novoValor)
                    if len(str(novoValor)) > 44:
                        print('Erro! Nota Fiscal excede 44 caracteres!')
                        continue
                except ValueError:
                    print('Erro! Valor deve ser um número válido!')
                    continue
                    
                    


            confirmacao = input(f'Tem certeza que deseja substituir "{atual}" por "{novoValor}"? (S/N): ').strip().upper()
            if confirmacao == 'S' or confirmacao == '':
                produto[campo] = novoValor
                print('Alterado com sucesso!')
            else:
                print("Alteração cancelada.")

def listar(listall):
    os.system('cls')
<<<<<<< HEAD
    print('----------LISTA DE ITENS----------')
=======
    print('----------RELATÓRIO DOS PRODUTOS----------')
>>>>>>> de8000c41b4999540cb3c90f7f3dc4a60640d381
    
    for item in listall:
        print('Id:', item['id'])
        print('Nome:', item['nome'])
        print('Descrição:', item['desc'])
        print('Valor:', item['valor'])
        print('Quantidade:', item['qnt'])
        print('Nota Fiscal:', item['notaF'])
        print('Ativo:', item['ativo'])
        print('-----------------------------------')

    input("Pressione Enter para sair...")

def excluir(listall):
    repeat = 'S'

    while repeat == 'S' or repeat == '':
        os.system('cls')
        produto = consultar(listall, False, True)
        
        if produto:
            print('Tem certeza que deseja excluir este produto da lista?')
            print('Id:', produto['id'])
            print('Nome:', produto['nome'])
            print('Descrição:', produto['desc'])
            print('Valor:', produto['valor'])
            print('Quantidade:', produto['qnt'])
            print('Nota Fiscal:', produto['notaF'])
            print('Ativo:', produto['ativo'])
            escolha = input('S (sim) ou N (não): ').strip().upper()

            if escolha == 'S' or escolha == '':
                listall.remove(produto)
                print('Produto excluído com sucesso.')
        else:
            return

        repeat = input('Deseja excluir mais algum produto? (S/N): ').strip().upper()
