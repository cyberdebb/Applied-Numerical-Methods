n = 10 # número de iterações
b = 1
a = 0


def f(x):
    return x / (1 + x**2)

def calcula_f_total(n, b, a):
    f_total = 0
    h = (b - a) / n

    x_ant = a
    x_nov = x_ant

    for _ in range(n):
        x_nov = x_ant + h

        # regra dos retângulos
        x_medio = (x_ant + x_nov) / 2
        valor_f = f(x_medio) 

        f_total += valor_f
        x_ant = x_nov
    
    return f_total, h

def calcula_R(h, f_total):
    return h * f_total
    


f_total, h = calcula_f_total(n, b, a)
R = calcula_R(h, f_total)
print(f"{R:.4f}")