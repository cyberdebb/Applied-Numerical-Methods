import numpy as np

dados = [
    [0, 2.1],
    [1, 7.7],
    [2, 13.6],
    [3, 27.2],
    [4, 40.9],
    [5, 61.1]
]

Sx = 0
Sxx = 0
Sxxx = 0
Sxxxx = 0
Sy = 0
Sxy = 0
Sxxy = 0

# Caluculado somatórios
for d in dados:
    Sx += d[0] # x
    Sxx += d[0] ** 2 # x^2
    Sxxx += d[0] ** 3 # x^3
    Sxxxx += d[0] ** 4 # x^4

    Sy += d[1] # y
    Sxy += d[0] * d[1] # x*y
    Sxxy += (d[0] ** 2) * d[1] # x^2 * y

n = len(dados)

# Resolvendo o sistema
A = np.array([[n, Sx, Sxx], [Sx, Sxx, Sxxx], [Sxx, Sxxx, Sxxxx]]) # Coeficientes
B = np.array([Sy, Sxy, Sxxy]) # Termos independentes

solucao = np.linalg.solve(A, B)
a = solucao[0]
b = solucao[1]
c = solucao[2]

# Resultado
print("solução:", solucao)
print(f"aproximação quadrática: y = {a:.3f} + {b:.3f}x + {c:.3f}x^2")