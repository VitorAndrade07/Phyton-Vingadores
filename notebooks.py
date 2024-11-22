from vingadores import Vingadores
import os

class Interface:

    @staticmethod
    def imprimir_titulo_app():
        print(''' 
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░████░░▄▀░░███░░▄▀░░█████████
█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░░░███░░░░░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀░░▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████████░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░░░▄▀▄▀▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█░░░░░░░░░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░███░░░░▄▀░░░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░██░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
              ''')

    @staticmethod
    def apresentar_menu_principal():
        os.system('cls')
        Interface.imprimir_titulo_app()
        print()
        print('Menu principal')
        print('1. Cadastrar um novo vingador')
        print('2. Listar todos os vingadores cadastrados')
        print('3. Detalhes de um vingador específico')
        print('4. Sair')
        print()
        Interface.ler_opcao_usuario()

    @staticmethod
    def imprimir_titulo_tela(titulo):
        os.system('cls')
        Interface.imprimir_titulo_app()
        print(f'{str(titulo).upper()}')
        print('*' * 20)
        print()

    @staticmethod
    def cadastrar_vingador():
        Interface.imprimir_titulo_tela('Cadastrando novo vingador')
        nome_heroi = input('Nome Heróico: ')
        nome_real = input('Nome Real: ')
        categoria = input('Categoria: ')
        poderes = input('Poderes: ')
        poder_principal = input('Poder Principal: ')
        fraquezas = input('Fraquezas: ')
        nivel_de_forca = input('Nível de Força: ')

        vingador = Vingadores(nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_de_forca)

        print(f'O vingador foi cadastrado: \n{vingador}')

    @staticmethod
    def listar_vingadores():
        Interface.imprimir_titulo_tela('Listando Vingadores')
        Vingadores.listar_vingadores()
    
    
    def limitar_texto(cls, texto):
        if len(texto) > 15:
            return texto[:15] + '...'
        return texto

    @staticmethod
    def mostrar_detalhes_vingador():
        Interface.imprimir_titulo_tela('Detalhes do Vingador')
        nome_heroi = input('Digite o nome do herói: ')
        vingador_encontrado = None
        for vingador in Vingadores.lista_de_vingadores:
            if vingador.nome_heroi.lower() == nome_heroi.lower():
                vingador_encontrado = vingador
                break
        if vingador_encontrado:
            print(f'Detalhes do Vingador {vingador_encontrado.nome_heroi}:')
            print(vingador_encontrado)
        else:
            print('Vingador não encontrado.')

    @staticmethod
    def ler_opcao_usuario():
        try:
            opcao = int(input('Digite sua opção: '))
            if opcao == 1:
                Interface.cadastrar_vingador()
            elif opcao == 2:
                Interface.listar_vingadores()
            elif opcao == 3:
                Interface.mostrar_detalhes_vingador()
            elif opcao == 4:
                print('Encerrando o programa')
                exit()
            else:
                print('Digite uma opção válida!')
        except ValueError:
            print('Você deve digitar um número inteiro.')

        Interface.voltar_ao_menu_principal()

    @staticmethod
    def voltar_ao_menu_principal():
        input('Digite qualquer tecla para voltar ao menu')
        os.system('cls')
        Interface.apresentar_menu_principal()