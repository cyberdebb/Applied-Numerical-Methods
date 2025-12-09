import numpy as np

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

def converge(A):
    for i in range(len(A)):
        soma = 0
        for j in range(len(A)):
            if i != j:
                soma += abs(A[i][j])
                
        if abs(A[i][i]) < soma:  # Critério de convergência
            return False
    
    return True 

def escolher_valores(A):
    resp = input("Deseja inserir valores para os x? (S)im ou (N)ão?").strip().upper()

    if resp == "S":
        x = []
        for i in range(len(A)):
            valor = float(input(f"Digite o valor de x[{i}]: "))
            x.append(valor)
    else:
        x = [0] * len(A)
    
    return x

def resolver_sistema(A, b, epsilon):
    print("\nResolução pelo método Gauss-Seidel:")
    count = 0

    if not converge(A):
        print("Matriz pode não convergir!")
        return
    
    # x_ant = escolher_valores(A)
    x_ant = [0] * len(A)
    x_novo = [0] * len(A)

    while True:
        count += 1
        for i in range(len(A)):
            soma = 0
            for j in range(len(A)):
                if i != j:
                    soma += A[i][j] * x_novo[j]

            x_novo[i] = (b[i] - soma) / A[i][i]  # Atualiza x_novo[i]

        print(f"\nInteração {count}:")
        x_formatado = [f"{v:.3f}" for v in x_novo]
        print(x_formatado)

        # Verifica a condição de convergência
        if max(abs(x_novo[i] - x_ant[i]) for i in range(len(A))) < epsilon:
            break

        x_ant = x_novo.copy()



# Exemplo de uso
A = np.array([[10, 1, 1],
              [2, 8, -4],
              [1, 5, 9]], dtype=float)

b = np.array([12, 6, 15], dtype=float)
epsilon = 0.02

print("\nMatriz A:")
print(A)

print("\nVetor b:")
print(b)

resolver_sistema(A, b, epsilon)
