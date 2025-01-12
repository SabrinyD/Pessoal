import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (1 a 50, tentativas ilimitadas)")
    print("2 - Médio (1 a 100, máximo de 10 tentativas)")
    print("3 - Difícil (1 a 200, máximo de 5 tentativas)")

    while True:
        try:
            nivel = int(input("Digite o número do nível (1, 2 ou 3): "))
            if nivel == 1:
                limite = 50
                max_tentativas = None
                break
            elif nivel == 2:
                limite = 100
                max_tentativas = 10
                break
            elif nivel == 3:
                limite = 200
                max_tentativas = 5
                break
            else:
                print("Escolha um nível válido (1, 2 ou 3).")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    numero_secreto = random.randint(1, limite)
    tentativas = 0
    acertou = False

    print(f"Eu pensei em um número entre 1 e {limite}. Tente adivinhar!")

    while not acertou:
        if max_tentativas and tentativas >= max_tentativas:
            print(f"Você excedeu o número máximo de {max_tentativas} tentativas. O número era {numero_secreto}.")
            break

        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1

            if chute < 1 or chute > limite:
                print(f"Por favor, digite um número entre 1 e {limite}.")
            elif chute < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif chute > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                acertou = True
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    jogo_adivinhacao()
