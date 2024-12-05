from question_model import Question


class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list #here we will insert question_bank as q_list at main file
    self.score = 0

  def still_has_questions(self):
    if self.question_number < len(self.question_list):
      return True
    else:
      return False

  def next_question(self):
    self.current_question = self.question_list[self.question_number]
    self.question_number += 1
    self.qa = input(f"Q{self.question_number}. {self.current_question.text} (True/False)?: ").title()

  def check_answer(self):
    if self.qa == self.current_question.answer:
      print("You got it right")
      self.score += 1
    else:
      print("You got it wrong")
    print(f"The correct answer was: {self.current_question.answer}")
    print(f"Your current score is: {self.score}/{self.question_number}.")
    print("\n")
    
    
    


