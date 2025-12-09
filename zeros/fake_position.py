import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**3 - 9*x +3

def f2(x):
    return x**4 - 26*x**2 + 24*x + 21

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

def fake_position(f, a, b, epsilon):    
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    
    count = 0

    while True:
        count += 1

        x_ns = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        f_a = f(a)
        f_b = f(b)
        f_ns = f(x_ns)
        
        print(f"Iteracao {count}: a = {a:.5f}, b = {b:.5f}, x_ns = {x_ns:.5f}, "
              f"f(x_ns) = {f_ns:.5f}, f(a) = {f_a:.5f}, f(b) = {f_b:.5f}, E = {abs(f(x_ns)):.5f}")

        if abs(f(x_ns)) < epsilon:
            return x_ns
        
        # Decide qual lado substituir
        if f_ns == 0:
            return x_ns
        elif f_a * f_ns < 0:
            b = x_ns
        else:
            a = x_ns
    
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


print("\nFuncao f(x) = x^3 - 9x + 3")
interval = find_initial_interval(f1, 50, -50)

if interval is not None:
    a, b = interval
    raiz = fake_position(f1, a, b, 0.001)
    print(f"\nA raiz aproximada encontrada é: {raiz:.5f}")
    plot(f1, x_min=-2, x_max=5, title="Grafico de f(x) = x^3 - 9x + 3")


print("\nFuncao f(x) = x^4 - 26x^2 + 24x + 21")
interval = find_initial_interval(f2, 50, -50)

if interval is not None:
    a, b = interval
    raiz = fake_position(f2, a, b, 0.01)
    print(f"\nA raiz aproximada encontrada é: {raiz:.5f}")
    plot(f2, x_min=-10, x_max=10, title="Grafico de f(x) = x^4 - 26x^2 + 24x + 21")