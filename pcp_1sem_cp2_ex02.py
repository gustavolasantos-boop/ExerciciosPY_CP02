valor1 = int(input("Digite um numero:\n"))
valor2 = int(input("Digite um numero:\n"))
valor3 = int(input("Digite um numero:\n"))

valores = [valor1,valor2,valor3]

valores.sort(reverse=True)

A = valores[0]
B = valores[1]
C = valores[2]

print(f"O valor de A é: {A}")
print(f"O valor de B é: {B}")
print(f"O valor de C é: {C}")

if A >= B+C:
    print("NÃO FORMA TRIÂNGULO")
elif A == B == C:
    print("TRIÂNGULO EQUILÁTERO")
elif A == B or A == C or B == C:
    print("TRIÂNGULO ISÓSCELES")

if A >= B+C:
    print()
elif  A^2 == B^2 + C^2:
    print("TRIÂNGULO RETÂNGULO")
elif A^2 > B^2 + C^2:
    print("TRIÂNGULO OBTUSÂNGULO")
elif A^2 < B^2 + C^2:
    print("TRIÂNGULO ACUTÂNGULO")

