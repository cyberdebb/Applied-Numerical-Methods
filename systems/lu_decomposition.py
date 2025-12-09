import numpy as np

# Configurar o numpy para suprimir notação científica para números pequenos
np.set_printoptions(suppress=True, precision=2)

# Cria matriz personalizada
def criarMatriz():
    print("\nDefinindo a matriz A de AX=B")

    while True:
        linhas = int(input("Digite um número válido de linhas e colunas da matriz:\n"))
        if linhas >= 2:
            break
        else:
            print("Valor inválido!")

    # Cria uma matriz A
    A = np.zeros((linhas, linhas), dtype=float)

    for i in range(linhas):
        for j in range(linhas):
            A[i][j] = float(input(f"Digite o valor de A[{i}][{j}]: "))

    # Cria o vetor b
    b = np.zeros(linhas, dtype=float)

    print("\nDefinindo o vetor b de AX=b")
    for i in range(linhas):
        b[i] = float(input(f"Digite o valor de b[{i}]: "))

    return A, b


# Função para decompor uma matriz A em duas matrizes L (inferior) e U (superior)
def lu_decomposition(A):
    n = A.shape[0]
    U = A.copy().astype(float)
    L = np.eye(n)

    # Iterando por cada coluna que será o pivô
    for coluna_pivo in range(n):
        if U[coluna_pivo, coluna_pivo] == 0:
            raise ValueError("Elemento pivô zero encontrado. Reordenamento necessário.")
        
        print(f"\nPivô na posição ({coluna_pivo}, {coluna_pivo}) é {U[coluna_pivo, coluna_pivo]:.2f}")

        # Para cada linha abaixo do pivô, fazemos a eliminação
        for linha_atual in range(coluna_pivo + 1, n):
            multiplicador = U[linha_atual, coluna_pivo] / U[coluna_pivo, coluna_pivo]
            U[linha_atual] = U[linha_atual] - multiplicador * U[coluna_pivo]
            L[linha_atual, coluna_pivo] = multiplicador
        
        print(f"\nApós a eliminação da linha {linha_atual} usando a linha {coluna_pivo}:")
        print("Matriz U:")
        print(U)
        print("Matriz L:")
        print(L)

    return L, U


# Função para resolver um sistema triangular inferior L * y = b
def resolver_triangular_inferior(L, b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=float)

    print("\nResolvendo o sistema L * y = b")
    print("Matriz L:")
    print(L)
    print("Vetor b:")
    print(b)

    # Para cada linha de L, calculamos o valor correspondente de y
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]

        print(f"y[{i}] calculado: {y[i]:.2f}")

    return y


# Função para resolver um sistema triangular superior U * x = y
def resolver_triangular_superior(U, y):
    n = U.shape[0]
    x = np.zeros_like(y, dtype=float)

    print("\nResolvendo o sistema U * x = y")
    print("Matriz U:")
    print(U)
    print("Vetor y:")
    print(y)

    # Resolvendo de baixo para cima (começando da última linha)
    for i in reversed(range(n)):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

        print(f"x[{i}] calculado: {x[i]:.2f}")

    return x


# Função principal para resolver um sistema linear A * x = b usando LU
def resolver_sistema(A, b):
    print("\n=== Iniciando resolução do sistema ===")
    L, U = lu_decomposition(A)

    print("\nMatriz L final:")
    print(L)
    print("\nMatriz U final:")
    print(U)

    y = resolver_triangular_inferior(L, b)
    x = resolver_triangular_superior(U, y)

    print("\nSolução final (vetor x):")
    print(x)

    return x


# Para criar a matriz personalizada
# linhas, a, b = criarMatriz()

# A = np.array([[1, 1, 2],
#               [2, -1, -1],
#               [1, -1, -1]], dtype=float)

# b = np.array([4, 0, -1], dtype=float)


A = np.array([[3, 2, 4],
              [1, 1, 2],
              [4, 3, 2]], dtype=float)

b = np.array([1, 2, 3], dtype=float)


print("\nMatriz A:")
print(A)

print("\nVetor b:")
print(b)

resolver_sistema(A, b)