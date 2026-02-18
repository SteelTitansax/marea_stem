import os 
import plotext as plt
import math
import numpy as np
import sympy as sym

# Definir la función
def func_point_solve(x,function_str):
    y = eval(
                function_str,
                {"__builtins__": None},   # for security
                {"x": x, "math": math}
            )
    return y

def function_solver(origin_point, final_point, function_str, step=100):
    x_vals = np.linspace(origin_point, final_point, step)
    
    y_vals = []
    for x in x_vals:
        try:
            y = eval(
                function_str,
                {"__builtins__": None},   # for security
                {"x": x, "math": math}
            )
            y_vals.append(y)
        except Exception:
            y_vals.append(None)

    plt.clf()
    plt.plot(x_vals, y_vals, label=function_str, color="white")
    plt.canvas_color("black")
    plt.clear_color()
    plt.show()
    
    point_solve_answer = input("Deseas resolver la ecuación para un punto especifico? (Yes/No): ") 

    if point_solve_answer.lower() == "y" or point_solve_answer.lower() == "yes" : 
        while True:
            x_solve = int(input("Introduzca punto a resolver: "))
            y_solve = func_point_solve(x_solve,function_str)
            print(f"Para la funcion {function_str} en el punto x {x_solve} , y es {y_solve}")
            
            solver_continue_answer = input("Deseas salir y dejar de resolver la funcion para otros puntos? (Yes/No): ")

            if solver_continue_answer.lower() == "y" or solver_continue_answer.lower() == "yes":
               break 

def system_function_solver(origin_point, final_point, function_str_1, function_str_2, step=100):
    x_vals = np.linspace(origin_point, final_point, step)
    
    y_vals_1 = []
    y_vals_2 = []

    for x in x_vals:
        try:
            y_1 = eval(
                function_str_1,
                {"__builtins__": None},   # for security
                {"x": x, "math": math}
            )
            y_vals_1.append(y_1)
            y_2 = eval(
                function_str_2,
                {"__builtins__": None},   # for security
                {"x": x, "math": math}
            )
            y_vals_2.append(y_2)
        except Exception:
            y_vals_1.append(None)
            y_vals_2.append(None)
    
    plt.clf()
    plt.plot(x_vals, y_vals_1, label=function_str_1, color="white")
    plt.plot(x_vals, y_vals_2, label=function_str_2, color="yellow")
    plt.canvas_color("black")
    plt.clear_color()
    plt.show()

    x,y = sym.symbols('x y')
    first = sym.sympify(function_str_1)
    second = sym.sympify(function_str_2)
    try:
        system_eq_answer = sym.solve([first, second], (x, y))
        print(f"📌 El resultado para el sistema de ecuaciones es: {system_eq_answer}")
    except Exception as e:
        print("❌ No se pudo resolver simbólicamente:", e)

def derivative_solver(function_str):
    x = sym.symbols('x')
    function = sym.sympify(function_str)
    derivative = sym.diff(function,x)
    print(f"La derivada de {function_str} es {derivative}")
    graphic_answer = input("Deseas graficar la funcion? (Yes/No): ")
    if graphic_answer.lower() == "y" or graphic_answer.lower() == "yes" : 
        x_vals = np.linspace(-100, 100, 100)
        y_vals = []
        for x in x_vals:
            try:
                y = eval(
                    str(derivative),
                    {"__builtins__": None},   # for security
                    {"x": x, "math": math}
                )
                y_vals.append(y)
            except Exception:
                y_vals.append(None)

        plt.clf()
        plt.plot(x_vals, y_vals, label=derivative, color="white")
        plt.canvas_color("black")
        plt.clear_color()
        plt.show()


def integral_solver(function_str):
    x = sym.symbols('x')
    function = sym.sympify(function_str)
    derivative = sym.integrate(function,x)
    print(f"La integral de {function_str} es {derivative}")
    graphic_answer = input("Deseas graficar la funcion? (Yes/No): ")
    if graphic_answer.lower() == "y" or graphic_answer.lower() == "yes" : 
        x_vals = np.linspace(-100, 100, 100)
        y_vals = []
        for x in x_vals:
            try:
                y = eval(
                    str(derivative),
                    {"__builtins__": None},   # for security
                    {"x": x, "math": math}
                )
                y_vals.append(y)
            except Exception:
                y_vals.append(None)
        
        plt.clf()
        plt.plot(x_vals, y_vals, label=derivative, color="white")
        plt.canvas_color("black")
        plt.clear_color()
        plt.show()

def permutations(n, r):
    """
    Calcula el número de permutaciones de n elementos tomados de r en r.
    
    Parámetros:
        n (int): Número total de elementos
        r (int): Número de elementos a elegir en cada permutación
        
    Retorna:
        int: Número de permutaciones posibles
    """
    if r > n or n < 0 or r < 0:
        print(f"Los datos introducidos {n} y {r} no tienen sentido")
    print(f"El numero de permutaciones es {math.factorial(n) // math.factorial(n - r)}")

def combinations(n, r):
    """
    Calcula el número de combinaciones de n elementos tomados de r en r.

    Parámetros:
        n (int): Número total de elementos
        r (int): Número de elementos a elegir en cada combinación

    Retorna:
        int: Número de combinaciones posibles
    """
    if r > n or n < 0 or r < 0:
        print("❌ Error: valores inválidos (r no puede ser mayor que n ni negativos)")
        return 0

    result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    print(f"🔢 El número de combinaciones de {n} elementos tomados de {r} en {r} es: {result}")



def read_matrix(rows, cols, name):
    print(f"\nIntroduce la matriz {name} (fila por fila, separando con espacios):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Fila {i+1}: ").split()))
                if len(row) != cols:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print(f"⚠️ Debes introducir exactamente {cols} números.")
    return np.array(matrix)


def read_vector(n, name):
    print(f"\nIntroduce el vector {name} ({n} valores):")
    while True:
        try:
            vector = list(map(float, input().split()))
            if len(vector) != n:
                raise ValueError
            return np.array(vector)
        except ValueError:
            print(f"⚠️ Debes introducir exactamente {n} números.")


def solve_system(A, b):
    Ab = np.hstack((A, b.reshape(-1, 1)))

    rank_A = np.linalg.matrix_rank(A)
    rank_Ab = np.linalg.matrix_rank(Ab)
    n = A.shape[1]

    print("\n--- RESULTADOS ---")
    print(f"Rango(A)  = {rank_A}")
    print(f"Rango(A*) = {rank_Ab}")
    print(f"Número de incógnitas = {n}\n")

    if rank_A < rank_Ab:
        print("❌ Sistema incompatible (no tiene solución).")

    elif rank_A == rank_Ab == n:
        solution = np.linalg.solve(A, b)
        print("✅ Sistema compatible determinado (solución única):")
        for i, x in enumerate(solution, start=1):
            print(f"x{i} = {x}")

    else:
        print("🔁 Sistema compatible indeterminado (infinitas soluciones).")



