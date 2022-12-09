#!/usr/bin/python3

"""
Autor: Rodrigo (Seth) de Freitas <rodcesar.freitas@gmail.com>
Contribuidor: Bruno (Guntz) Gasparetto <brunogasparetto@gmail.com>
Data: 13/01/2016
Versão: 0.0.2
Licença GPL/GPLv2
    Rules
	Tesoura corta papel
	Papel cobre pedra
	Pedra esmaga lagarto
	Lagarto envenena Spock
	Spock destrói tesoura
	Tesoura decapita lagarto
	Lagarto come papel
	Papel rejeita Spock
	Spock vaporiza pedra
	Pedra esmaga tesoura.
	Simples ;)
    
    News
        Data: 13/01/2013, Rodrigo de Freitas
        * Jogo baseado no seriado The Big Bang Theory, no qual o personagem Sheldon Cooper cria um
        jogo, baseado no famoso 'pedra, papel, tesoura', criando o 'pedra, papel, tesoura, lagarto, Spock'.
        Neste jogo o usuário tem cinco opções (pedra, papel, tesoura, lagarto e Spock), e tenta vencer a CPU, 
        de acordo com as regras vigentes (estou sem o rascunho original aqui, depois eu digito as regras).
	Data: 22/01/2016, Rodrigo de Freitas
	* O jogo realiza todas as funções "mínimas" necessárias. Se torna uma versão stable.


    Log
        Data: Não definida, Bruno Gasparetto
        * Bruno usou constantes no código, e o deixou mais limpo. Realmente, ficou muito bom
        Data: 13/01/2016, Rodrigo de Freitas
        * Como o jogo será em um arquivo só, ao invés de arquivos separados, resolvi colocar a documentação (log e news)
        aqui mesmo.
        Data: 17/01/2016, Rodrigo de Freitas
        * Regras do jogo colocadas na documentação, como prometido. ^_^
	Data: 22/01/2916, Rodrigo de Freitas
	* Término de estruturas de decisão - e consequentemente, término desta versão
    
"""

import random
 
CONST_EXIT = 0
CONST_ROCK = 1
CONST_PAPER = 2
CONST_SCISSORS = 3
CONST_LIZARD = 4
CONST_SPOCK = 5

def winner(user, cpu):
    #check if user or cpu win
    if user == 1 and cpu == 3 or user == 1 and cpu == 4 or user == 2 and cpu == 1 or user == 2 and cpu == 5 or user == 3 and cpu == 2 or user == 3 and cpu == 4 or user == 4 and cpu == 2 or user == 4 and cpu == 5 or user == 5 and cpu == 1 or user == 5 and cpu == 3:
        print('Você ganhou')
    elif user == 1 and cpu == 2 or user == 1 and cpu == 5 or user == 2 and cpu ==3 or user == 2 and cpu == 4 or user == 3 and cpu == 1 or user == 3 and cpu == 5 or user == 4 and cpu == 1 or user == 4 and cpu == 3 or user == 5 and cpu == 2 or user == 5 and cpu == 4:
        print('Você perdeu')


def whoWin(userChoice, cpuChoice):
    print('\n')
   
    if userChoice == cpuChoice:
        print('Empate')
   
    elif (userChoice == CONST_LIZARD and cpuChoice == CONST_SPOCK) or (cpuChoice == CONST_LIZARD and userChoice == CONST_SPOCK):
        print('Lagarto envenena Spock')
   
    elif (userChoice == CONST_LIZARD and cpuChoice == CONST_PAPER) or (cpuChoice == CONST_LIZARD and userChoice == CONST_PAPER):
        print('Lagarto come Papel')
   
    elif (userChoice == CONST_PAPER and cpuChoice == CONST_ROCK) or (cpuChoice == CONST_PAPER and userChoice == CONST_ROCK):
        print('Papel cobre Pedra')
   
    elif (userChoice == CONST_PAPER and cpuChoice == CONST_SPOCK) or (cpuChoice == CONST_PAPER and userChoice == CONST_SPOCK):
        print('Papel refuta Spock')
   
    elif (userChoice == CONST_ROCK and cpuChoice == CONST_SCISSORS) or (cpuChoice == CONST_ROCK and userChoice == CONST_SCISSORS):
        print('Pedra quebra Tesoura')
   
    elif (userChoice == CONST_ROCK and cpuChoice == CONST_LIZARD) or (cpuChoice == CONST_ROCK and userChoice == CONST_LIZARD):
        print('Pedra esmaga Lagarto')
   
    elif (userChoice == CONST_SPOCK and cpuChoice == CONST_SCISSORS) or (cpuChoice == CONST_SPOCK and userChoice == CONST_SCISSORS):
        print('Spock destrói Tesoura')
   
    elif (userChoice == CONST_SPOCK and cpuChoice == CONST_ROCK) or (cpuChoice == CONST_SPOCK and userChoice == CONST_ROCK):
        print('Spock vaporiza Pedra')
   
    elif (userChoice == CONST_SCISSORS and cpuChoice == CONST_PAPER) or (cpuChoice == CONST_SCISSORS and userChoice == CONST_PAPER):
        print('Tesoura corta Papel')
   
    elif (userChoice == CONST_SCISSORS and cpuChoice == CONST_LIZARD) or (cpuChoice == CONST_SCISSORS and userChoice == CONST_LIZARD):
        print('Tesoura decapita Lagarto')
   
    else:
        print('WTF???')
   
    winner(userChoice, cpuChoice)
 
 
def main():
    choices = 'Sair do Jogo', 'Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock'
 
    while True:
        print('\nPedra, Papel, Tesoura, Lagarto e Spock\n')
       
        for index, value in enumerate(choices):
            print('%d - %s' % (index, value))
 
        choice = int(input('\nEscolha entre os números do menu: '))
 
        if choice == CONST_EXIT:
            print('\nObrigado por jogar\n')
            quit()
 
        if choice < CONST_ROCK or choice > CONST_SPOCK:
            print('\nEscolha somente os números indicados no menu\n')
            continue
 
        cpu = random.randint(CONST_ROCK, CONST_SPOCK)
 
        print('\nVocê escolheu %s' % choices[choice])
        print('Computador escolheu %s' % choices[cpu])
 
        whoWin(choice, cpu)
 
 
if __name__ == '__main__':
    main()
