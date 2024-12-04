# Estrutura de Decisão (if, elif, else)
nota = 85

if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
else:
    print("Nota: D")

# Estrutura de Repetição
# FOR
frutas = ["maça", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

# WHILE
contador = 1

while contador <= 5:
    print("Convidados:", contador)
    contador += 1

# Comandos de Controle de Fluxo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# BREAK
for numero in numeros:
    if numero == 7:
        print("Número 7 encontrado! Interromper o loop")
        break
    print(numero)

# CONTINUE
for numero in range(1, 10):
    if numero % 2 == 0:
        continue # Pular a iteração para números pares
    print("Número Ímpar:", numero)

# Função map()
# map(função, iterável)
valores_iniciais = [1000, 1500, 2000, 3000]
print("Valores iniciais:", valores_iniciais)

# calcular_juro = lambda valor: valor * 1.02

valores_com_juro = list(map(lambda valor: valor * 1.02, valores_iniciais))
print("Valores com juro de 2% aplicados:", valores_com_juro)