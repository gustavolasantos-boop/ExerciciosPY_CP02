cp1=float(input("digite a nota do checkpoint 1 "))
cp2=float(input("digite a nota do checkpoint 2 "))
cp3=float(input("digite a nota do checkpoint 3 "))
sp1=float(input("digite a nota do sprint 1 "))
sp2=float(input("digite a nota do sprint 2 "))
gs=float(input("digite a nota do global solution "))
menor = cp1
if cp2 < menor:
    menor = cp2
if cp3 < menor:
    menor = cp3
media = (cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4
media_peso = media * 0.4 + gs * 0.6
print("média do semestre ", media,)
print("média do semestre com peso ", media_peso)
