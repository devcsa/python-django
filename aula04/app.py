# Funções
def saudacao():
    print("Olá, bem-vindo a live de Python")
saudacao()

# Parâmentros e Argumentos
def saudacao(nome):
    print(f"Olá, {nome}")
saudacao("Cesar")

# Retorno de Valores
def soma(a, b):    
    return a + b
resultado = soma(5, 3)
print(f"Resultado: { resultado }")

# Parâmetro Padrão
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}")
saudacao()
saudacao("Cesar")

# Argumentos e Parâmentros Variáveis
def soma(*numeros):
    return sum(numeros)
resultado = soma(1, 2, 3, 4)
print(resultado)

def exibir_informacoes(**info):
    print(info)
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
exibir_informacoes(nome="Ana", idade=19)

# Função simples
def juro(x):
    return x * 1.03
print(juro(100))
# Funções lambda
juro = lambda x: x * 1.03
print(juro(100))