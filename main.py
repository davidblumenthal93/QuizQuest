#from quiz_game import Question, Quiz, new_gam
from high_score import get_high_score, save_high_score
from characters import Character
from levels import Level, MusicLevel, MoviesLevel,new_game
from questions import Question, q_list1, q_list2

#high_score = get_high_score()




def menu_screen():

    print("                          Main Menu                          ")
    print(" *********|              1.New Game                |********* ")
    print(" *********|2. High Score      |3. Quit            |********* ")
    option = input("Choose an option: ")
    if option == "1":
        new_game()
    elif option == "2":
        high_score = get_high_score()
        if input("Return to main menu, y or n\n") == "y":
            menu_screen()
        elif input == "n":
            exit()
    elif option == "3":
        exit()


def play_again():
    option = input("Do you wish to play again \n 1.Yes or 2.No:")
    option = option.lower()
    if option == "yes":
        menu_screen()
    else:
        exit


menu_screen()
play_again()
