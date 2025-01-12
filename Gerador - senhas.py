import random
import string

def gerar_senha():
    print("Seja bem-vindo(a) ao Gerador de Senhas Aleatórias!")

    try:
        tamanho = int(input("Digite o tamanho da senha que você deseja (mínimo 6 caracteres): "))
        if tamanho < 6:
            print("O tamanho mínimo da senha é 6 caracteres. Tente novamente.")
            return

        incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
        incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
        incluir_caracteres_especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

        caracteres = string.ascii_lowercase  

        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_caracteres_especiais:
            caracteres += string.punctuation

        if not caracteres:
            print("Você precisa selecionar pelo menos um tipo de caractere. Tente novamente.")
            return

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        print(f"Sua senha gerada é: {senha}")

    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos para o tamanho.")

if __name__ == "__main__":
    gerar_senha()
