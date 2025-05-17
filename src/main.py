# Importações
import os 
import functions
import time

import functions

# Variaveis e Listas
opc: int | None = None
listall = []

while opc != 0: # Laço de repetição para entrada no menu principal
    os.system('cls')
    print('----------MENU PRINCIPAL----------')
    print('     ------------------------')
    print('''          1- Cadastrar
          2- Alterar
          3- Excluir
          4- Consultar
          5- Listar
          0- Sair''')
    print('     ------------------------')

    try: # Erros de entrada
        opc = int(input('Escolha uma opção: '))
        if opc == 0:
            os.system('cls')
            print('-------------')
            print('  Saindo...  ')
            print('-------------')
            time.sleep(3)
            break
        if opc < 0 or opc >5:
            print('Erro! Opção inexistente.')
            input('Pressione Enter para continuar')
            continue

        if opc == 1:
            functions.cadastrar(listall)

        if opc == 5:
            functions.listar(listall)

    except ValueError:
        print('Somente números podem ser inseridos.') 
        input('Pressione Enter para continuar')
        continue
