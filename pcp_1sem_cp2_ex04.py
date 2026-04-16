#codigo da funcao de horas extras
def calcular_horas_extras(salario_base, horas):
    valor_hora_extra = salario_base * 0.015
    total = valor_hora_extra * horas
    return total

#codigo da funcao para descontos x faltas
def calcular_descontos_faltas(salario_base, faltas):
    desconto_por_falta = salario_base * 0.02
    total = desconto_por_falta * faltas
    return total

#codigo para funcao de bonus
def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == 's':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0

nome = input("Nome do funcionário: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Salário base: "))
horas_extras = float(input("Horas extras: "))
faltas = int(input("Faltas no mês: "))
recebeu_bonus = input("Recebeu bônus? (s/n): ")

total_horas_extras = calcular_horas_extras(salario_base, horas_extras)
total_descontos = calcular_descontos_faltas(salario_base, faltas)
bonus = calcular_bonus(cargo, recebeu_bonus)

salario_bruto = salario_base
total_acrescimos = total_horas_extras + bonus
salario_final = salario_bruto + total_acrescimos - total_descontos


print("--- RESUMO ---")
print("Funcionário:", nome)
print("Salário bruto:", salario_bruto)
print("Acréscimos:", total_acrescimos)
print("Descontos:", total_descontos)
print("Salário final:", salario_final)