cod_estado = int(input("Digite o código de estado de origem dom caminhão (1 a 5): "))
peso = float(input("Digite o peso da carga do caminhão em toneladas: "))
cod_carga = int(input("Digite o código da carga (10 a 40): "))

peso_kg = peso * 1000
print(f"Peso da carga convertido em quilos: {peso_kg:.2f} KG")

preco_carga = float
if 10 <= cod_carga <= 20:
    preco_carga = peso_kg * 100
    print(f"Preço da carga: R${preco_carga:.2f}")
elif 20 < cod_carga <= 30:
    preco_carga = peso_kg * 250
    print(f"Preço da carga: R${preco_carga:.2f}")
else:
    preco_carga = peso_kg * 340
    print(f"Preço da carga: R${preco_carga:.2f}")

imposto = float
if cod_estado == 1:
    imposto = preco_carga * 0.35
    print(f"Imposto: R${imposto:.2f}")
if cod_estado == 2:
    imposto = preco_carga * 0.25
    print(f"Imposto: R${imposto:.2f}")
if cod_estado == 3:
    imposto = preco_carga * 0.15
    print(f"Imposto: R${imposto:.2f}")
if cod_estado == 4:
    imposto = preco_carga * 0.05
if cod_estado == 5:
    imposto = preco_carga
    print(f"Imposto: R${imposto:.2f}")

total = preco_carga + imposto
print(f"Total: R${total:.2f}")