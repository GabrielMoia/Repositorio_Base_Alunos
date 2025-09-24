notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print("Média:", media)
if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")