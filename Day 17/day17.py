from day17_question_model import Question
from day17_data import question_data
from day17_quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text= question_text, q_answer= question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

