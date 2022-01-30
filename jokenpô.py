#library and modules
from random import randrange
from time import sleep
from os import system
#options to player
rock = 0
paper = 1
scissors = 2

match = 0

"""a variable to define the player option for none"""
player_option = None
bot_option = None

#the strings to show the result of the player choices 
win = "Você venceu!!!"
lose = "Você perdeu."
tie = "Empate."

def print_option (choice, possibility, who=str, options=str):
    if choice == possibility:
        print(f"{who}: {choice} ({options})\n")

#function for define a color to strings
def print_with_color (color=str, text=str):
    if color == "red":
        print(f"\033[1;31m{text}\033[m")
    elif color == "green":
        print(f"\033[1;32m{text}\033[m")
    elif color == "yellow":
        print(f"\033[1;33m{text}\033[m")
    

print("""                ===PEDRA PAPEL E TESOURA.===
                         Jokenpô
____________             -------

Pedra = 0 
Papel = 1
Tesoura = 2
____________""")

#looping of the program
while True:
    #choose of player
    player = int(input("Escolha sua opção: "))

    """generate a random number on a range between 0 and 2
     to simulate an option of the bot(machine)"""
    bot_number = randrange(0,2)
    
    print("""                    Jokenpô.
____________         -------
Pedra = 0 
Papel = 1
Tesoura = 2
____________""")

    """basic expression to make a increment in number of matchs. This
    expression is equivalent to match = match++ in other programming languages"""
    match = match + 1
    #Show the match number and a "decoration for the game."
    print(f"Round |{match}|\n")
    sleep(0.10)
    print("JO...")
    sleep(1)
    print("KEN...")
    sleep(1)
    print("PÔ!!!\n")
    sleep(1)

     
    #-------------the main part of the game-----------------
    #print player option
    print_option(player, rock, "Você", "Pedra")
    print_option(player, paper, "Você", "Papel")
    print_option(player, scissors, "Você", "Tesoura")

    #option "bot option"
    print_option(bot_number, rock, "Bot", "Pedra")
    print_option(bot_number, paper, "Bot", "Papel")
    print_option(bot_number, scissors, "Bot", "Tesoura")

    """The conditions of main part of the program
    (In this part, the colors of that function have been applied.)"""
    if player > 2 or player < 0:
        print_with_color("yellow", "Tente novamente.\n")
    elif bot_number == player:
        print_with_color("yellow", "Empate.\n")
    elif bot_number == 0 and player == scissors:
        print_with_color("red", f"{lose}\n")
    elif bot_number == 1 and player == rock:
        print_with_color("red", f"{lose}\n")
    elif bot_number == 2 and player == paper:
        print_with_color("red", f"{lose}\n")
    else:
        '''When the player wins, print some mensages,
        ask if he wants to leave, clear the terminal
        and break the code (end the program)'''
        print_with_color("green", "Você venceu!!!\n")
        print(f"Total de partidas jogadas: {match}\n")
        player = input("Você quer sair? (S/N) ")
        if player == "S" or player == "s":
            sleep(3)
            system("clear")
            break
        elif player == "N" or player == "n":
            match = 0
            system("clear")
            continue
        else:
            print("Ocorreu algum erro...\n")
            sleep(1)
            print("Tente novamente.\n")