import time

# Função Cadastrar com retorno de erros de quantidade de caracteres. Definindo máximo de caracteres.
def cadastrar(listall):
    print('----------CADASTRAR ATIVO----------')
    try:
        id_ativo = f"{len(listall) + 1:03d}"
        desc = input('Insira uma descrição: ').strip()
        if not desc:
            print('Erro! Descrição não pode estar vazia!')
        elif len(desc) > 300:
            print('Erro! Descrição excede 300 caracteres!')
            print('-------------------------------------')
            input('Pressione Enter para continuar...')
            return
        
        valor = float(input('Digite o valor(ex 3500.00): '))
        if valor <= 0:
            print('Erro! Valor deve ser maior que zero(0)!')
            print('---------------------------------------')
            input('Pressione Enter para continuar...')
            return
        
        quant = int(input('Digite a quantidade: '))
        # if quant <= 0:
        #     print('Erro! Quantidade deve ser maior que zero(0)!')
        # elif len(quant) > 1000:
        #     print('Erro! Quantidade maior que 1000!')
        #     print('--------------------------------------------')
        #     input('Pressione Enter para continuar...')
        #     return

        nota_fiscal = input('Digite o número da Nota Fiscal(NF): ').strip()
        if len(nota_fiscal) > 44:
            print('Erro! Nota Fiscal excede 44 caracteres!')

        ativo = {
            'id': id_ativo,
            'desc': desc,
            'valor': valor,
            'qnt': quant,
            'notaF': nota_fiscal,
            'ativo': True
        }

        listall.append(ativo)
        print(f'Ativo cadastrado com Id: {id_ativo}')
        input('Pressione Enter para continuar...')

    
    except ValueError:
        print('Erro! Valor ou Quantidade devem ser numeros válidos!')
        input('Pressione Enter para continuar...')
        return

# Função listar com parâmetros de decisão
def listar(listall):
    print('----------LISTA DE ATIVOS----------')
    
    for item in listall:
        print('Id:', item['id'])
        print('Descrição:', item['desc'])
        print('Valor:', item['valor'])
        print('Quantidade:', item['qnt'])
        print('Nota Fiscal:', item['notaF'])
        print('Ativo:', item['ativo'])
        print('-----------------------------------')

    input("Pressione Enter para continuar...")