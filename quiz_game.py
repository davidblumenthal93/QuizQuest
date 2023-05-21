import random
from questions import Question, q_list1, q_list2
from high_score import get_high_score, save_high_score
from characters import Character
from levels import Level, MusicLevel, MoviesLevel




class Quiz:
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
            print("Correct")
        else:
            print("")
            self.player.take_damage(10)
        print(f"Wrong Answer", "you take {damage} damage. You have {health} health remaining.")



