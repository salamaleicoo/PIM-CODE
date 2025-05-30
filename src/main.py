import os 
import functions
import time

import functions

opc: int | None = None
listall = []

while opc != 0: 
    os.system('cls')
    print('''         
----------MENU PRINCIPAL----------
1- Cadastrar Ativos
2- Alterar
3- Excluir
4- Consultar
5- Gerar Relatório
0- Sair
----------------------------------''')

    try: 
        opc = int(input('Escolha uma opção: '))

        if opc > 6:
            print('Erro! Opção inexistente.')
            input('Pressione Enter para continuar')
            continue

        if opc == 0:
            os.system('cls')
            print('-------------')
            print('  Saindo...  ')
            print('-------------')
            time.sleep(1)
            break

        if opc == 1:
            functions.cadastrar(listall)

        if opc == 2:
            functions.alterar(listall)

        if opc == 3:
            functions.excluir(listall)

        if opc == 4:
            functions.consultar(listall)

        if opc == 5:
            functions.listar(listall)

    except ValueError:
        print('Somente números podem ser inseridos.') 
        input('Pressione Enter para continuar')
        continue
