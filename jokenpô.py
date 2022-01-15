#library and modules
from random import randint
from time import sleep
#options to player
rock = 0
paper = 1
cut = 2
match = 0

print('''                ===PEDRA PAPEL E TESOURA.===
                         Jokenpô
____________             -------

Pedra = 0 
Papel = 1
Tesoura = 2
____________''')

#looping of the program
while True:
    #option of the player
    player = int(input('Escolha sua opção: '))
    
    print('''                    Jokenpô.
____________         -------
Pedra = 0 
Papel = 1
Tesoura = 2
____________''')
    #match
    match = match + 1
    print(f'Round |{match}|')
    sleep(2)
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!!!\n')
    sleep(1)
     
    #-------------the main part of the game-----------------
    #random number to simulate an option of the machine/bot
    option = randint(0,2)
    #print the bot option and the player option
    bot = print('Bot: ',option)
    print('Você: ',player)
    if player > 2:
        print('Tente novamente.')
    elif option == player:
        print('Empate.')
    elif option == 0 and player == cut:
        print('Você perdeu.')
    elif option == 1 and player == rock:
        print('Você perdeu.')
    elif option == 2 and player == paper:
        print('Você perdeu.')
    else:
      end = print('Você venceu!!!')
      break