from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for dict in question_data:
    question_bank.append(Question(dict["question"], dict["correct_answer"]))
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()