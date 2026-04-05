nome = input("Seu nome: ")
peso = float(input ("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

print(f"\n=== Resultado para {nome} ===")
print(f"Peso:    {peso} kg")
print(f"Altura:  {altura} m")
print(f"IMC:     {imc: .2f}")
print(f"(Classificação virá na próxima aula!)")