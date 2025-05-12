def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

def main():
    print("=== Mini Conversor de Temperaturas ===")
    print("Unidades disponíveis: Celsius (C), Fahrenheit (F), Kelvin (K)")

    temp = input("Digite o valor da temperatura (ex: 36.6): ")
    unidade_origem = input("Digite a unidade de origem (C, F, K): ").strip().upper()
    unidade_destino = input("Digite a unidade para converter (C, F, K): ").strip().upper()

    try:
        temp = float(temp)
    except ValueError:
        print("Valor inválido para temperatura.")
        return

    if unidade_origem == unidade_destino:
        print(f"Temperatura convertida: {temp:.2f} {unidade_destino}")
        return

    if unidade_origem == 'C':
        if unidade_destino == 'F':
            resultado = celsius_to_fahrenheit(temp)
        elif unidade_destino == 'K':
            resultado = celsius_to_kelvin(temp)
        else:
            print("Unidade de destino inválida.")
            return

    elif unidade_origem == 'F':
        if unidade_destino == 'C':
            resultado = fahrenheit_to_celsius(temp)
        elif unidade_destino == 'K':
            resultado = fahrenheit_to_kelvin(temp)
        else:
            print("Unidade de destino inválida.")
            return

    elif unidade_origem == 'K':
        if unidade_destino == 'C':
            resultado = kelvin_to_celsius(temp)
        elif unidade_destino == 'F':
            resultado = kelvin_to_fahrenheit(temp)
        else:
            print("Unidade de destino inválida.")
            return
    else:
        print("Unidade de origem inválida.")
        return

    print(f"{temp:.2f} {unidade_origem} equivalem a {resultado:.2f} {unidade_destino}")

if __name__ == "__main__":
    main()
