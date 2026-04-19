nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
renda = float(input("Informe sua renda mensal: "))
emprestimo = float(input("Informe o valor que deseja retirar de emprestimo: "))
parcelas = int(input("Número de parcelas que deseja: "))

def pode_aprovar(idade, renda, emprestimo):
    return idade >= 18 and emprestimo < 20*renda

if parcelas < 3 or parcelas > 24:
    print("Número de parcelas inválido, deve ser entre 3 e 24")
else:
    if not pode_aprovar(idade, renda, emprestimo):
        print("Empréstimo negado!")
    else:
        def taxa(parcelas):
            if parcelas < 7:
                return 0.05
            elif parcelas < 13:
                return 0.08
            else:
                return 0.1