import random
from questions import q_list1, q_list2
from high_score import get_high_score, save_high_score


class Character:
    def __init__(self, name, character_class, health, attack, defence):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.attack = attack
        self.defence = defence

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

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
            print("Correct")
        else:
            print("")
        print(f"The correct answer was: {answer}")


q_bank1 = []
for q in q_list1:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    q_bank1.append(new_question)


q_bank2 = []
for q in q_list2:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    q_bank2.append(new_question)


def new_game():
    high_score = get_high_score
    current_score = 0
    
    class_choice = input("Please select a Class: 1.Warrior, 2.Mage, 3.Ranger")
    if class_choice == "1":
        character_class = "Warrior"
        health = 100
        attack = 20
        defence = 10
    elif class_choice == "2":
        character_class = "Mage"
        health = 100
        attack = 10
        defence = 5
    elif class_choice == "3":
        character_class = "Ranger"
        health = 100
        attack = 15
        defence = 7
    else:
        print("Invalid choice, defaulting to warrior.")
        character_class = "Warrior"
    user = input("Please enter your name: ")
    print("Welcome", user, "the", character_class)
    player = Character(user, character_class, health, attack, defence)
    print("          |------------Welcome to Trivia------------|          ")
    print(" *********|1. Movies            |2. Music           |********* ")
    print("          |-----------------------------------------|")
    option = input("Choose a category " + user + ":")
    if option == "1":
        print("You chose category 1: Movies")
        quiz = Quiz(q_bank1)
        random.shuffle(q_bank1)
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

    elif option == "2":
        print("You chose category 2: Music")
        quiz = Quiz(q_bank2)
        random.shuffle(q_bank2)
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

    while quiz.remaining_questions():
        quiz.next_question()

    print("You've completed the quiz")

    print(f"Your Final score was: {quiz.score}")
    if quiz.score > int(high_score):
        print("New high score!")
        save_high_score(quiz.score)
    else:
        print("Better luck next time.")
