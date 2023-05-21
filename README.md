# QuizQuest
Trivia Quiz Game
This is a Python code that implements a trivia quiz game. The game has two categories, Movies and Music, and allows the player to select their character class from three options: Warrior, Mage, and Ranger.

Technologies Used
The code is written in Python and uses the following modules:

random: for shuffling the questions in each category
questions: a module containing two lists of dictionaries, each representing a category of questions
high_score: a module that reads and writes the current high score to a file
Classes
The code defines three classes:

Character
This class represents a player's character in the game and has the following attributes:

name: the character's name
character_class: the character's class (Warrior, Mage, or Ranger)
health: the character's health points
attack: the character's attack points
defence: the character's defence points
Question
This class represents a trivia question and has the following attributes:

question: the text of the question
answer: the correct answer to the question
Quiz
This class represents a quiz and has the following attributes:

question_number: the number of the current question
score: the player's score
question_list: the list of questions for the current category
And the following methods:

next_question(): displays the next question and checks the player's answer
remaining_questions(): returns True if there are more questions to ask
check_answer(): checks the player's answer and updates their score
Functions
The code defines two functions:

new_game()
This function initializes a new game and allows the player to select their character class and the category of questions. It then creates a Quiz object and starts asking questions until all questions have been asked. Finally, it displays the player's score and checks if it's a new high score.

main()
This function calls new_game() to start a new game.

How to Use
To use this code, you can simply run the main() function. The code will ask you to select your character class and the category of questions. Once you've completed the quiz, the code will display your score and whether you've achieved a new high score.