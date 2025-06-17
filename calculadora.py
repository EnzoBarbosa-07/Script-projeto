Numero_1 = 0
Numero_2 = 0

print("Olá, bem vindo!\n\nVamos começar a calcular! \n\nPara isso, preciso que você me informe os dois números a serem calculados e o tipo de operação entre eles. Vamos lá?\n")

operação = input("Por favor, informe qual tipo de operação você deseja usar:\n + para adição\n - para subtração\n * para multiplicação\n / para divisão\n\n")
print("Ok, a operação escolhida é", operação, "\n")

Numero_1 = int (input ("Digite o primeiro número: "))
print("O primeiro número é:", Numero_1)

print("\n\nPerfeito!\nAgora insira o segundo valor!")

Numero_2 = int (input ("Digite o segundo número: "))
print("O segundo número é:", Numero_2, "\n\n")


if operação == '+':
  print(Numero_1, "+", Numero_2, "= ")
  print("O resultado é", Numero_1 + Numero_2)

elif operação == '-':
  print(Numero_1, "-", Numero_2, "= ")
  print("O resultado é", Numero_1 - Numero_2)

elif operação == '*':
  print(Numero_1, "*", Numero_2, "= ")
  print("O resultado é", Numero_1 * Numero_2)

elif operação == '/':
  print(Numero_1, "/", Numero_2, "= ")
  print("O resultado é", Numero_1 / Numero_2)

else:
  print("Tipo de operação inválida, tente novamente.")
