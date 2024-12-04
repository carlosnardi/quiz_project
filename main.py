import question_model

import data

import quiz_brain


from data import question_data
from question_model import Question

question_bank = []
for item in question_data:
  question_bank.append(Question(item['text'], item['answer']))

print(question_bank[0].text)
print(question_bank[0].answer)
