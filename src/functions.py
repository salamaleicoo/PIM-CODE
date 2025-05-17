def cadastrar(listall):
    print('----------CADASTRAR ATIVO----------')
    try:
        id_ativo = f"{len(listall) + 1:03d}"
        desc = input('Insira uma descrição: ').strip()
        if not desc:
            print('Erro! Descrição não pode estar vazia!')
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
        if quant <= 0:
            print('Erro! Quantidade deve ser maior que zero(0)!')
            print('--------------------------------------------')
            input('Pressione Enter para continuar...')
            return

        nota_fiscal = input('Digite o número da Nota Fiscal(NF): ').strip()
        
        ativo = {
            'Id': id_ativo,
            'Descrição': desc,
            'Valor': valor,
            'Quantidade': quant,
            'Nota Fiscal': nota_fiscal,
            'Ativo': True
        }

        listall.append(ativo)
        print(f'Ativo cadastrado com Id: {id_ativo}')
    
    except ValueError:
        print('Erro! Valor ou Quantidade devem ser numeros válidos!')
        input('Pressione Enter para continuar...')
        return
    