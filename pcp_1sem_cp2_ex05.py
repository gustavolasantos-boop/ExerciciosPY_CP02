# Informações de entrada
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
renda = float(input("Informe sua renda mensal: "))
emprestimo = float(input("Informe o valor que deseja retirar de emprestimo: "))
parcelas = int(input("Número de parcelas que deseja (3 até 24): "))

# Funções
def pode_aprovar(idade, renda, emprestimo):
    return idade >= 18 and emprestimo < 20*renda

def taxa(parcelas):
    if parcelas < 7:
        return 0.05
    elif parcelas < 13:
        return 0.08
    else:
        return 0.1

def calc_parcelas(emprestimo, taxa, parcelas):
    PMT = emprestimo * ((taxa*(1+taxa)**parcelas) / ((1+taxa)**parcelas - 1))
    return PMT

def calc_total(calc_parcelas, parcelas):
    total = calc_parcelas(emprestimo, taxa(parcelas), parcelas) * parcelas
    return total

def calc_juros(calc_total, emprestimo):
    juros = calc_total - emprestimo
    return juros

# Informações de saida
if pode_aprovar(idade, renda, emprestimo) == 1:
    print("="*20)
    print(f"Cliente: {nome}")
    print(f"Valor do financiamento: R${emprestimo:.2f}")
    print(f"A taxa de juros é de {taxa(parcelas)*100:.0f}%")
    print(f"O valor de cada parcela é de: R${calc_parcelas(emprestimo, taxa(parcelas), parcelas):.2f}")
    print(f"O valor total pago é de R${calc_total(calc_parcelas, parcelas):.2f}")
    print(f"O juros pago é de R${calc_juros(calc_total(calc_parcelas, parcelas), emprestimo):.2f}")
    print("=" * 20)
else:
    print("=" * 20)
    print("Você deve ter mais de 18 anos, e o valor do emprestimo deve ser de no maximo de 20 vezes o valor da renda")
    print("=" * 20)