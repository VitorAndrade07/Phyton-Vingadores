from vingadores import Interface
from vingadores import Vingador

def main():
    Vingador('Homem de Ferro', 'Tony Stark', 'Humano', ['Inteligência', 'Engenharia', 'Rico'], 'Armadura', ['Arrogância', 'Orgulho'], 2000)
    Vingador('Capitão América', 'Steve Rogers', 'Humano', ['Força', 'Habilidade em Combate', 'Liderança'], 'Escudo', ['Inexperiência no mundo moderno'], 8000)
    Vingador('Star-Lord', 'Peter Quill', 'Humano', ['Liderança', 'Habilidade em Combate', 'Inteligência'], 'Pistolas e Jetpack', ['Impulsividade'], 7500)
    Vingador('Hulk', 'Bruce Banner', 'Humano', ['Força sobre-humana', 'Regeneração', 'Durabilidade'], 'Força', ['Raiva', 'Controle mental'], 10000)
    Vingador('Homem-Aranha', 'Peter Parker', 'Humano', ['Força sobre-humana', 'Agilidade', 'Sentido Aranha'], 'Teias', ['Responsabilidade'], 6000)


    Interface().menu() 

if __name__ == "__main__":
    main()
