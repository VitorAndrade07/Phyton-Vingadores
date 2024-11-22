class Vingadores:

    lista_de_vingadores = []

    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_de_forca):
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_de_forca = nivel_de_forca
        Vingadores.lista_de_vingadores.append(self)
    
    @classmethod
    def listar_vingadores(cls):
        print(f'{"Nome do Heroi".ljust(3)} | {"Nome Real".ljust(3)} | {"Categoria".ljust(3)} | {"Poderes".ljust(3)} | {"Poder Principal".ljust(3)} | {"Fraqueza".ljust(3)} | {"Nível de força".ljust(3)}')
        for vingador in cls.lista_de_vingadores:
            print(f"{str(vingador.nome_heroi).ljust(3)} | {str(vingador.nome_real).ljust(3)} | {str(vingador.categoria).ljust(3)} | {str(vingador.poderes).ljust(3)} | {str(vingador.poder_principal).ljust(3)} | {str(vingador.fraquezas).ljust(3)} | {str(vingador.nivel_de_forca).ljust(3)}")
   
    def __str__(self):
        return f'{"Nome do Heroi".ljust(3)} | {"Nome Real".ljust(3)} | {"Categoria".ljust(3)} | {"Poderes".ljust(3)} | {"Poder Principal".ljust(3)} | {"Fraqueza".ljust(3)} | {"Nível de Força".ljust(3)} \n{str(self.nome_heroi).ljust(3)} | {str(self.nome_real).ljust(3)} | {str(self.categoria).ljust(3)} | {str(self.poderes).ljust(3)} | {str(self.poder_principal).ljust(3)} | {str(self.fraquezas).ljust(3)} | {str(self.nivel_de_forca).ljust(3)}'


capitao_america = Vingadores('Capitão América', 'Steve Rogers', 'Humano', 'Super força', 'Super força', 'Nenhum Notável', 'Alto')

Vingadores.listar_vingadores()

print()
print(capitao_america)