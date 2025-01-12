def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def conversor_temperatura():
    print("Seja bem-vindo(a) ao Conversor de Temperatura!")
    print("Escolha a conversão desejada:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("3 - Fahrenheit para Celsius")
    print("4 - Fahrenheit para Kelvin")
    print("5 - Kelvin para Celsius")
    print("6 - Kelvin para Fahrenheit")

    try:
        opcao = int(input("Digite o número da conversão desejada: "))
        if opcao < 1 or opcao > 6:
            print("Opção inválida. Escolha um número entre 1 e 6.")
            return

        valor = float(input("Digite o valor da temperatura: "))

        if opcao == 1:
            resultado = celsius_para_fahrenheit(valor)
            print(f"{valor}°C equivalem a {resultado:.2f}°F")
        elif opcao == 2:
            resultado = celsius_para_kelvin(valor)
            print(f"{valor}°C equivalem a {resultado:.2f} K")
        elif opcao == 3:
            resultado = fahrenheit_para_celsius(valor)
            print(f"{valor}°F equivalem a {resultado:.2f}°C")
        elif opcao == 4:
            resultado = fahrenheit_para_kelvin(valor)
            print(f"{valor}°F equivalem a {resultado:.2f} K")
        elif opcao == 5:
            resultado = kelvin_para_celsius(valor)
            print(f"{valor} K equivalem a {resultado:.2f}°C")
        elif opcao == 6:
            resultado = kelvin_para_fahrenheit(valor)
            print(f"{valor} K equivalem a {resultado:.2f}°F")

    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos.")

if __name__ == "__main__":
    conversor_temperatura()
