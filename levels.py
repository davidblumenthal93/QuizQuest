from characters import Character
from questions import Question, q_list1, q_list2
from high_score import get_high_score

import random

def new_game():
        high_score = get_high_score
        current_score = 0
    
        my_character = Character()
        my_character.select_class(input)
        user = input("Please enter your name: ")
        print("Welcome", user, "the", my_character.character_class, my_character.health, my_character.art)
        print("You come upon two doors, on each door is a symbol,on the left is a music note, on the right is a movie reel")
        print(" *********|1. Movies           |2. Music           |********* ")
        print("          |-----------------------------------------|")
        option = input("Choose a door " + user + ":")
        if option == "1":
            level = MoviesLevel()
        elif option == "2":
            level = MusicLevel()
        if level.remaining_questions():
            level.next_question()
        elif level.player.health <= 0:
            print("You have died, your score was", level.score)
            print("The high score is", high_score)

class Level:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.player = Character()


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Question {self.question_number}: {current_question.question}")
        self.check_answer(user_answer, current_question.answer)

    def remaining_questions(self):
        return self.question_number < len(self.question_list)
        

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print("Correct, You attack the Demon, he takes 10 damage")
        else:
            print("")
            self.player.take_damage(10)
            print(f"Wrong Answer, you take 10 damage. You have {self.player.health} health remaining.")

    

        


class MoviesLevel(Level):
    def __init__(self):
        q_bank = []
        for q in q_list1:
            question_text = q["question"]
            question_answer = q["answer"]
            next_question = Question(question_text, question_answer)
            q_bank.append(next_question)
        random.shuffle(q_bank)
        super().__init__(q_bank)
        print(""" 
_______________________________
|_______________^_______________|
|                               |
|    ____   _________   ____    |
|   /  / | | Movies  | | \  \   |
|   \__\_| |_________| |_/__/   |
|                               |
|                               |
'-------------------------------'
      """)
        print("You have entered a a land filled with old video tapes and movie reels, a creature appears, it has a cameraa for a head and a VHS tape for a body, it is the VHS Demon, he attacks you, you must answer his questions to defeat him")


class MusicLevel(Level):
    def __init__(self):
        q_bank = []
        for q in q_list2:
            question_text = q["question"]
            question_answer = q["answer"]
            new_question = Question(question_text, question_answer)
            q_bank.append(new_question)
        random.shuffle(q_bank)
        super().__init__(q_bank)
        print("""

.------------------------.
|\\////////               |
| \/  __ _ Music_ __     |
|    /  \|\.....|/  \    |
|    \__/|/_____|\__/    |                                                
| A                      |                                                
|    ________________    |                                                
|___/_._o________o_._\___| 
        """)