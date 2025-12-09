n = 6 # número de iterações
b = 3.6
a = 3.0


def f(x):
    return 1 / x 

def calcula_f_total(n, b, a):
    f_total = 0
    h = (b - a) / n

    x_ant = a
    x_nov = x_ant

    for _ in range(n):
        x_nov = x_ant + h

        # regra dos trapézios
        valor_f_ant = f(x_ant)
        valor_f_nov = f(x_nov)

        valor_f = (valor_f_ant + valor_f_nov) / 2 

        f_total += valor_f
        x_ant = x_nov
    
    return f_total, h

def calcula_R(h, f_total):
    return h * f_total
    


f_total, h = calcula_f_total(n, b, a)
R = calcula_R(h, f_total)
print(f"{R:.4f}")