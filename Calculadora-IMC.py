def calcular_imc():
    print("Bem-vindo à Calculadora de IMC!")
    print("O IMC (Índice de Massa Corporal) é uma medida usada para avaliar se você está dentro de um peso saudável.")

    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros (exemplo: 1.75): "))

        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos.")
            return

        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif 18.5 <= imc < 24.9:
            print("Classificação: Peso normal")
        elif 25 <= imc < 29.9:
            print("Classificação: Sobrepeso")
        elif 30 <= imc < 34.9:
            print("Classificação: Obesidade Grau 1")
        elif 35 <= imc < 39.9:
            print("Classificação: Obesidade Grau 2")
        else:
            print("Classificação: Obesidade Grau 3 (obesidade mórbida)")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")

if __name__ == "__main__":
    calcular_imc()
