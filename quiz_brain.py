class QuizBrain:
    def __init__(self, lista_perguntas):
        self.pergunta_numero = 0
        self.lista_perguntas = lista_perguntas
        self.pontos = 0

    def ainda_tem_perguntas(self):
        """Verifica se ainda tem perguntas na lista."""
        return self.pergunta_numero < len(self.lista_perguntas)

    def proxima_pergunta(self):
        """Chama a próxima pergunta da lista."""
        pergunta_atual = self.lista_perguntas[self.pergunta_numero]
        self.pergunta_numero += 1
        resposta_usuario = input(f"Pergunta {self.pergunta_numero}: {pergunta_atual.pergunta} (Verdadeiro/Falso) ")
        self.verifica_pergunta(resposta_usuario, pergunta_atual.resposta)

    def verifica_pergunta(self, resposta_usuario, resposta_certa):
        """Verifica se a resposta do usuário é a correta."""
        if resposta_usuario.lower() == resposta_certa.lower():
            print("Acertou!")
            self.pontos += 1
        else:
            print("Errou!")
            print(f"Resposta certa: {resposta_certa}")
        print(f"Sua pontuação é: {self.pontos}/{self.pergunta_numero}")
        print("\n")