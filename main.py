from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

question_bank = []
for item in question_data:
  # question_bank.append(Question(item['text'], item['answer']))
  question_bank.append(Question(item['question'], item['correct_answer']))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()
  quiz.check_answer()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
