class Question:
  def __init__(self, text, answer):
    self.text = text
    self.answer = answer
  def response(self):
    response = input("true or false: ")
    if self.answer == response:
      print("You are right")
    else: 
      print("You are wrong")

q1 = Question("Verde é uma cor?","true")

print(q1.text)
q1.response()



