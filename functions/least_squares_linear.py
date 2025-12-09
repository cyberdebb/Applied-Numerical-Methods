dados = [
    [1, 1],
    [2, 4],
    [3, 8]
]

Sx = 0
Sy = 0
Sxx = 0
Sxy = 0

for d in dados:
    Sx += d[0]
    Sy += d[1]
    Sxx += d[0] ** 2
    Sxy += d[0] * d[1]

n = len(dados)
m = (n*Sxy - Sy*Sx) / (n*Sxx - Sx*Sx)
b = (Sxx*Sy - Sxy*Sx) / (n*Sxx - Sx*Sx)

print(f"aproximação linear: y = {m:.3f}x + {b:.3f}")