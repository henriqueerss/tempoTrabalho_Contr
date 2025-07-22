tc = int(input("Digite quanto tempo você tem de trabalho na sua empresa: \n"))

salario = float(input("Digite seu salário: \n"))

if tc < 3:
    aumento = salario * 0.05
else:
    aumento = salario * 0.10

nSalario = salario + aumento
print(f"\nO seu salario foi de {salario:.2f} para {nSalario:.2f} com o aumento de {aumento:.2f}.\n")