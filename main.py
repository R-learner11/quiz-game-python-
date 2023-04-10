from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# creating a question bank

question_bank = []
for question in question_data:
    new_question = Question(question['text'],question['answer'])
    question_bank.append(new_question)


quiz1 = QuizBrain(question_bank)

while quiz1.still_has_questions():
    quiz1.next_question()
    # quiz1.check_answer()

quiz1.final_score()
# we can also get the values as
print("You've completed the quiz.")
print(f"Your final score is: {self.score}/{self.question_no}")



