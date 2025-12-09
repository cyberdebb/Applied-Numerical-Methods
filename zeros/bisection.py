import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**2 - 3

def f2(x):
    return x**3 - 10

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

def bisection(f, a, b, epsilon):
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    
    count = 0

    while True:
        count += 1

        x_ns = (a + b) / 2.0

        f_a = f(a)
        f_b = f(b)
        f_ns = f(x_ns)
        
        # Calcula os produtos f(a) * f(x_ns) e f(b) * f(x_ns)
        fa_fns = f_a * f_ns
        fb_fns = f_b * f_ns
        
        print(f"Iteracao {count}: a = {a:.5f}, b = {b:.5f}, x_ns = {x_ns:.5f}, "
              f"f(x_ns) = {f_ns:.5f}, f(a) = {f_a:.5f}, f(b) = {f_b:.5f}, "
              f"f(a)*f(x_ns) = {fa_fns:.5f}, f(b)*f(x_ns) = {fb_fns:.5f}, E = {abs((b - a) / 2.0):.5f}")

        if abs((b - a) / 2.0) < epsilon:
            return x_ns
        
        # Decide qual lado substituir
        if f_ns == 0:
          return x_ns
        elif fa_fns < 0:
          b = x_ns
        else:
          a = x_ns
    
def plot(f, x_min, x_max, title="Grafico da Funcao"):
    # Plota uma função 'func' no intervalo [x_min, x_max].
    x = np.linspace(x_min, x_max, 400)
    
    # Calcula os valores de y usando a função f(x)
    y = f(x)
    
    # Plota a função
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x) = x^2 - 3')
    
    # Adiciona linhas de grade
    plt.grid(True)
    
    # Adiciona títulos e legendas
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    # Adiciona uma linha horizontal em y=0 para indicar o eixo x
    plt.axhline(0, color='black', linewidth=0.8)
    
    # Adiciona uma linha vertical em x=0 para indicar o eixo y
    plt.axvline(0, color='black', linewidth=0.8)
    
    # Mostra o gráfico
    plt.legend()
    plt.show()


print("\nFuncao f(x) = x^2 - 3")
# Encontrando o intervalo inicial [a, b]
interval = find_initial_interval(f1, 50, -50)

if interval is not None:
    a, b = interval
    raiz = bisection(f1, a, b, 0.01)
    print(f"\nA raiz aproximada encontrada e: {raiz:.5f}")
    plot(f1, x_min=-2, x_max=5, title="Grafico de f(x) = x^2 - 3") # Chamando a função de plotagem para a função f(x)


print("\nFuncao f(x) = x^3 - 10")
# Encontrando o intervalo inicial [a, b]
interval = find_initial_interval(f2, 50, -50)
 
if interval is not None:
    a, b = interval
    raiz = bisection(f2, a, b, 0.05)
    print(f"\nA raiz aproximada encontrada e: {raiz:.5f}")
    plot(f2, x_min=-2, x_max=5, title="Grafico de f(x) = x^3 - 10") # Chamando a função de plotagem para a função f(x)

