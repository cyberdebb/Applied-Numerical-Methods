import numpy as np

n = 10 # número de iterações
b = 1
a = 0


def f(x):
    return np.e ** x 

def calcula_f_total(n, b, a):
    f_total = 0
    h = (b - a) / n
    x_val = a

    for i in range(n + 1):
        # regra de simpson
        if i == 0 or i == n:
            func = f(x_val)
        elif i % 2 != 0:
            func = 4 * f(x_val)
        elif i % 2 == 0:
            func = 2 * f(x_val)
    
        f_total += func
        x_val += h

    return f_total, h

def calcula_S(h, f_total):
    return (h/3) * f_total
    


f_total, h = calcula_f_total(n, b, a)
S = calcula_S(h, f_total)
print(f"{S:.4f}")