import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**2 + x - 6

def f2(x):
    return 3*x - np.cos(x)

def find_initial_interval(f, start, end):
    x_values = range(start, end - 1, -1)

    for i in range(len(x_values) - 1):
        a = x_values[i]
        b = x_values[i + 1]

        if f(a) * f(b) < 0:
            print("Valor de a = " + str(a) + "\nValor de b = " + str(b) + "\n")
            return a, b
        elif f(a) * f(b) == 0:
            if f(a) == 0:
                print("Raiz = " + str(a))
            else:
                print("Raiz = " + str(b))
            
            return a, b
            
    raise ValueError("Nao foi encontrado um intervalo")

def secant(f, a, b, epsilon, max_iterations):
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    
    count = 0
    x_ant = a
    x_nov = b

    while count < max_iterations:
        count += 1

        f_x_ant = f(x_ant)
        f_x_nov = f(x_nov)

        if f_x_ant == 0:
            return x_ant
        elif f_x_nov == 0:
            return x_nov
        elif np.isclose(f_x_ant, f_x_nov):  # Evitando divisão por zero
            return x_nov
        
        x_prox = x_nov - (f_x_nov * (x_ant - x_nov)) / (f_x_ant - f_x_nov)

        print(f"Iteracao {count}: x(i-1) = {x_ant:.5f}, x(i) = {x_nov:.5f}, f(x(i-1)) = {f_x_ant:.5f}, f(x(i)) = {f_x_nov:.5f}, x(i+1) = {x_prox:.5f}, E = {abs(x_prox - x_nov):.5f}")

        # Verificação do critério de parada
        if abs(x_prox - x_nov) < epsilon:
            return x_prox

        x_ant = x_nov
        x_nov = x_prox
    
    raise ValueError("O método da Secante não convergiu em {max_iterations} iteracoes")

def plot(f, x_min, x_max, title="Grafico da Funcao"):
    x = np.linspace(x_min, x_max, 400)
    y = f(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=title)
    plt.grid(True)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.legend()
    plt.show()


print("\nFuncao f(x) = x^2 + x - 6")
# interval = find_initial_interval(f1, 50, -50)
interval = 1.5, 1.7

if interval is not None:
    a, b = interval
    raiz = secant(f1, a, b, 0.01, 100)
    print(f"\nA raiz aproximada encontrada é: {raiz:.5f}")
    plot(f1, x_min=-2, x_max=5, title="Grafico de f(x) = x^2 + x - 6")


print("\nFuncao f(x) = 3x - cos(x)")
# interval = find_initial_interval(f1, 50, -50)
interval = 0, 0.5

if interval is not None:
    a, b = interval
    raiz = secant(f2, a, b, 0.0001, 100)
    print(f"\nA raiz aproximada encontrada é: {raiz:.5f}")
    plot(f1, x_min=-2, x_max=5, title="Grafico de f(x) = 3x - cos(x)")