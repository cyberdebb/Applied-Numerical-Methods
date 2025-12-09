import numpy as np

# Encontra o pivô de maior valor
def encontraPivoInicial(A):
    linhaInicial, colunaInicial = 0, 0
    linhaPivo = max(
        range(linhaInicial, len(A)),  # Aqui percorremos as linhas a partir de linha_inicial
        key=lambda i: abs(A[i][colunaInicial])  # Procuramos o maior valor absoluto na coluna j
    )

    # Troca de linha inicial com a linha que contém o pivô de maior valor
    A[[linhaInicial, linhaPivo]] = A[[linhaPivo, linhaInicial]]
    return A

# Zera todos os elementos abaixo do pivô
def elementoPivo(A, linhaPivo, colunaPivo):
    index = 1
    while linhaPivo + index < len(A):
        if A[linhaPivo + index][colunaPivo] != 0:
            m = A[linhaPivo + index][colunaPivo] / A[linhaPivo][colunaPivo]

            linhaAlterada = m * A[linhaPivo]
            linhaAbaixo = A[linhaPivo + index]
            linhaResultado = linhaAbaixo - linhaAlterada
            A[linhaPivo + index] = linhaResultado

        index += 1

    return A

# Cria matriz personalizada
def criarMatriz():
    print("\nDefinindo a matriz A de AX=B")

    while True:
        linhas = int(input("Digite um número válido de linhas e colunas da matriz:\n"))
        if linhas >= 2:
            break
        else:
            print("Valor inválido!")

    # Cria uma matriz a
    a = np.zeros((linhas, linhas), dtype=float)

    for i in range(linhas):
        for j in range(linhas):
            a[i][j] = float(input(f"Digite o valor de a[{i}][{j}]: "))

    # Cria a matriz b
    b = np.zeros(linhas, dtype=float)

    print("\nDefinindo a matriz B de AX=B")
    for i in range(linhas):
        b[i] = float(input(f"Digite o valor de b[{i}]: "))

    return linhas, a, b

# Utiliza o Método da Eliminação Gaussiana para resolver o sistema
def gaussian_elimination(linhas, A, b):
    # Criar a matriz estendida [A | B]
    matrizEstendida = np.hstack((A, b.reshape(-1, 1)))
    print("\nA matriz estendida [A | B] é:")
    print(matrizEstendida)

    matrizEstendida = encontraPivoInicial(matrizEstendida)
    linhaPivo, colunaPivo = 0, 0

    print("\nMatriz alterada com o maior pivô na posição 1")
    print(matrizEstendida)

    print("\nResolvendo:")
    while linhaPivo < linhas - 1:  # Percorre até a última linha
        matrizEstendida = elementoPivo(matrizEstendida, linhaPivo, colunaPivo)
        linhaPivo += 1
        colunaPivo += 1 
        print(matrizEstendida)
        print()

    print("Matriz triangular superior encontrada!")

    # Substituição retroativa para resolver o sistema triangular
    x = np.zeros(linhas, dtype=float)
    for i in range(linhas-1, -1, -1):  # Começa da última linha até a primeira
        soma = 0
        for j in range(i+1, linhas):  # Somar os termos que já foram resolvidos
            soma += matrizEstendida[i][j] * x[j]
        x[i] = (matrizEstendida[i][-1] - soma) / matrizEstendida[i][i]

    return x


print("\nResolvendo um sistema com o método de Eliminação Gaussiana")

# Para criar a matriz personalizada
# linhas, a, b = criarMatriz()

A = np.array([[0.25, 0.5, 1],
              [0.09, 0.3, 1],
              [0.01, 0.1, 1]])

b = np.array([0.25, 0.49, 0.81])

linhas = len(A)

print("\nMatriz A:")
print(A)

print("\nMatriz B:")
print(b)

# Exibir o sistema AX = B de forma simbólica
print("\nSistema linear na forma AX = B:")
x_simbolica = np.array([f"x{i+1}" for i in range(linhas)])
for i in range(linhas):
    linha = " + ".join([f"{A[i][j]}*{x_simbolica[j]}" for j in range(linhas)])  # Criar a equação para cada linha
    print(f"{linha} = {b[i]}")  # Exibir a equação completa da linha

x = gaussian_elimination(linhas, A, b)

print("\nResultado do vetor X:")
x = np.round(x, 2)
print(x)
