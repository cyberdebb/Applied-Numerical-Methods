import sympy as sp
import numpy as np

# Configurações de impressão do numpy
np.set_printoptions(suppress=True, precision=2)


def calcular_vetor(M, valor_x, valor_y):
    # Substituindo x e y na matriz
    M_valores = M.subs({x: valor_x, y: valor_y})
    M_valores_floats = np.array(M_valores.tolist(), dtype=float)

    return M_valores, M_valores_floats


def calcular_s(J, F):
    # Multiplica F por -1
    neg_F = -F
    # Resolve o sistema J * s = -F para s
    s = J.LUsolve(neg_F)
    return s


def resolver_sistema(F, J, X, epsilon, tau):
    print("\n\nResolução pelo método Newton:")
    count = 0 

    while True:
        count+=1

        valor_x = X[0]
        valor_y = X[1]

        print(f"\nIteração {count}")
        print(f"Matriz com x={valor_x:.2f} e y={valor_y:.2f}:")

        J_vetor, J_vetor_floats = calcular_vetor(J, valor_x, valor_y)
        F_vetor, F_vetor_floats = calcular_vetor(F, valor_x, valor_y)

        print("Vetor J:")
        for row in J_vetor_floats:
            print(" ".join(f"{val:8.3f}" for val in row))

        print("\nVetor F:")
        for row in F_vetor_floats:
            print(" ".join(f"{val:8.3f}" for val in row))
        
        s = calcular_s(J_vetor, F_vetor)

        # Calcula o novo vetor X
        X_novo = X + np.array(s).astype(np.float64).flatten()  # Converte s para numpy array e flattens para somar
        F_vetor_novo, F_vetor_novo_floats = calcular_vetor(F, X_novo[0], X_novo[1])

        # Critério de parada
        if (np.linalg.norm(X_novo - X) < epsilon) and \
           (abs(F_vetor_novo[0]) < tau) and (abs(F_vetor_novo[1]) < tau):
            break

        # Atualiza X
        X = X_novo

    print("\nSolução encontrada:")
    print(X)


# Definindo as variáveis simbólicas
x, y = sp.symbols('x y')

# Definindo as matrizes e variáveis
F = sp.Matrix([[x + y - 3],
               [x**2 + y**2 - 9]])
J = F.jacobian([x, y])

X = np.array([1, 5], dtype=float)

epsilon = 0.01
tau = 0.01

# Printando as matrizes
print("\nMatriz F:")
sp.pprint(F)

print("\nMatriz Jacobiana de F:")
sp.pprint(J)

print("\nVetor X inicial:")
print(X)

# Resolvendo sistema
resolver_sistema(F, J, X, epsilon, tau)
