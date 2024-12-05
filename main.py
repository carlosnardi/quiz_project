from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

question_bank = []
for item in question_data:
  question_bank.append(Question(item['text'], item['answer']))

# print(question_bank[0].text)
# print(question_bank[0].answer)

# number_of_questions = 0
# while number_of_questions < len(question_bank): #pensando ainda

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()
  quiz.check_answer()

# number_of_questions += 1 #no fim do while