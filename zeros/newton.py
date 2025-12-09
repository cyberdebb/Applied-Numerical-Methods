import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    # Verificar se x é simbólico (SymPy) ou numérico (NumPy)
    if isinstance(x, sp.Symbol):
        return 2 * x - sp.sin(x) - 4  # Usar sin de SymPy para cálculo simbólico
    else:
        return 2 * x - np.sin(x) - 4  # Usar sin de NumPy para cálculo numérico

def calculate_prime(f, order=1):
    # Definir x como uma variável simbólica
    x = sp.symbols('x')

    # Converter a função 'f' para uma expressão simbólica
    f_sympy = f(x)

    # Calcular a derivada simbolicamente (de acordo com a ordem)
    f_prime_sympy = sp.diff(f_sympy, x, order)

    # Converter a derivada para uma função numérica usando lambdify
    f_prime = sp.lambdify(x, f_prime_sympy, 'numpy')

    return f_prime

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

def find_best_extreme(f, f_prime2, a, b):
    x_values = np.linspace(a, b, 1000)  # Gera 1000 pontos entre a e b (pode ajustar o número de pontos)

    for x in x_values:
        if f(x) * f_prime2(x) > 0:
            return x
    raise ValueError("Nenhum extremo encontrado onde f(x) * f''(x) > 0")

def newton(f, f_prime, x_init, epsilon, max_iterations):
    if f(x_init) == 0:
        return x_init
    
    count = 0
    x_ant = x_init

    while count < max_iterations:
        count += 1

        f_x_ant = f(x_ant)
        f_prime_x_ant = f_prime(x_ant)

        x_nov = x_ant - (f_x_ant / f_prime_x_ant)

        print(f"Iteracao {count}: x(i) = {x_ant:.5f}, f(x(i)) = {f_x_ant:.5f}, f'(x(i)) = {f_prime_x_ant:.5f}, x(i+1) = {x_nov:.5f}, E = {abs(x_nov - x_ant):.5f}")

        # Verifica a condição de parada
        if abs(x_nov - x_ant) < epsilon:
            return x_nov
        
        x_ant = x_nov
    
    raise ValueError("O método de Newton não convergiu em {max_iterations} iteracoes")

def plot(f, x_min, x_max, title="Grafico da Funcao"):
    # Plota uma função 'func' no intervalo [x_min, x_max].
    x = np.linspace(x_min, x_max, 400)
    
    # Calcula os valores de y usando a função f(x)
    y = f(x)
    
    # Plota a função
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=title)
    
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


print("\nFuncao f(x) = 2x - sen(x) - 4")
interval = find_initial_interval(f1, 50, -50)

if interval is not None:
    a, b = interval
    f_prime = calculate_prime(f1)
    f_prime2 = calculate_prime(f1, order=2)
    
    x_init = find_best_extreme(f1, f_prime2, a, b)
    print(f"Melhor valor inicial encontrado: x = {x_init} com f(x)*f''(x) > 0")

    raiz = newton(f1, f_prime, x_init, 0.001, 100)
    print(f"\nA raiz aproximada encontrada e: {raiz:.5f}")
    plot(f1, x_min=-2, x_max=5, title="Grafico de f(x) = 2x - sen(x) - 4")
