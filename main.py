from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

banco_perguntas = []

for perguntas in question_data:
    pergunta = perguntas["question"]
    resposta = perguntas["correct_answer"]
    nova_pergunta = Question(pergunta, resposta)
    banco_perguntas.append(nova_pergunta)

quiz = QuizBrain(banco_perguntas)

while quiz.ainda_tem_perguntas():
    quiz.proxima_pergunta()

print("Você completou o Quiz!")
print(f"Sua pontuação foi de: {quiz.pontos}/{quiz.pergunta_numero}")