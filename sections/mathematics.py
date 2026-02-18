# Marea Chatbot STEM v1.0.0 (STEM chatbot) 
# ---------------------------------------------------------------------------------------------------------------------------
# Purpose : Multipurpose chatbot combining Maths, Physics, Chemistry and data analytics actions
# ---------------------------------------------------------------------------------------------------------------------------
# Author : Manuel Portero Leiva 
# ---------------------------------------------------------------------------------------------------------------------------


import warnings
# We write this code here to filter every warning
# ---------------------------------------------------------------------------------------------------------------------------
warnings.filterwarnings("ignore", message="pkg_resources is deprecated as an API")
# ---------------------------------------------------------------------------------------------------------------------------

import os
from constants import num_layout_equals
from utils.math_utils import *
# ------------------------
# Main Code Section
# ------------------------

def mathematics_section():


    while True :

        try:
        
            # ❌ Clean screen
            # ----------------

            os.system("clear")
        

            print("=" * num_layout_equals)
            print("👩💻  Marea Chatbot STEM —  Seccion matemáticas")
            print("=" * num_layout_equals)
            print("📐 Bienvenido a la sección matemáticas.")
            print("=" * num_layout_equals)
            print("Selecciona tu acción:")
            print("=" * num_layout_equals)
            print("=" * num_layout_equals)
            print("📊  Opción 0: Graficar función / Resolver función en un punto")
            print("📉  Opción 1: Derivadas de una función")
            print("∫   Opción 2: Integral de una función")
            print("📟  Opción 3: Logaritmo o exponencial de un número")
            print("🧩  Opción 4: Resolución de sistemas de ecuaciones")
            print("🧮  Opción 5: Resolución de sistemas matriciales")
            print("📐  Opción 6: Trigonometría")
            print("🔀  Opción 7: Permutaciones")
            print("🎯  Opción 8: Combinaciones")
            print("🚪  Opción 9: Salir")

            print("=" * num_layout_equals)


            answer = input("👉  ¿Qué deseas hacer? (selecciona una opción): ")


            match answer:

                # 📈  Function solver
                # -------------------------------------------------

                case "0":
                    try:
                        print("⚙️ Graficando solver...")
                        origin_point = input("Introduce un punto inicial (integer): ")
                        origin_point = int(origin_point)
                        final_point = input("Introduce un punto final (integer): ")
                        final_point = int(final_point)
                        function = input("Introduce ecuacion en formato x (Ej: x**2 + 3*x - 5): ")
                        function_solver(origin_point,final_point,function)

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # 📐 Derivative functions section
                # -------------------------------------------------

                case "1":
                    try:
                        print("📐 Entrando en sección derivadas")
                        function = input("Introduce ecuacion en formato x (Ej: x**2 + 3*x - 5): ")
                        derivative_solver(function)

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # ∫  Integral functions section
                # -------------------------------------------------

                case "2":
                    try:
                        print("∫  Entrando en sección integrales")
                        function = input("Introduce ecuacion en formato x (Ej: x**2 + 3*x - 5): ")
                        integral_solver(function)

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # 🔢 Log / Exp functions section
                # -------------------------------------------------
                
                case "3":
                    try:
                        print("∫  Entrando en sección integrales")
                        log_answer = input("logaritmo o exponencial (Log == 0 / Neperian Exp == 1): ").strip()
                        number = input("introduzca numero para realizar operacion: ").strip()
                        if log_answer == "0":
                            result_log = round(math.log(float(number),10),4)
                            print(f"El logaritmo de {number} es {str(result_log)}")
                        else:
                            result_exp = round(math.e**float(number),4)
                            print(f"La exponencial de {number} es {str(result_exp)}")

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")
                
                # 🧮  System ecuations
                # -------------------------------------------------

                case "4":
                    try:
                        print("⚙️ Graficando solver...")
                        origin_point = input("Introduce un punto inicial (integer): ")
                        origin_point = int(origin_point)
                        final_point = input("Introduce un punto final (integer): ")
                        final_point = int(final_point)
                        function1 = input("Introduce la primera ecuación en formato x (Ej: x**2 + 3*x - 5): ")
                        function2 = input("Introduce la segunda ecuación en formato x (Ej: x**2 + 3*x - 5): ")
                        system_function_solver(origin_point,final_point,function1,function2)

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                case "5":

                # 📐  Matrix solver ecuation
                # -------------------------------------------------

                        print("Resolucion de sistemas de ecuaciónes linesales\n")

                        m = int(input("Número de ecuaciones: "))
                        n = int(input("Número de incógnitas: "))

                        A = read_matrix(m, n, "A")
                        b = read_vector(m, "b")

                        solve_system(A, b)


                # 📐  Trigonometric ecuations
                # -------------------------------------------------

                case "6":
                    try:
                        print("⚙️ Realizando calculos trigonometricos")
                        cateto_contiguo = int(input("Introduce longitud de cateto 1: "))
                        cateto_opuesto = int(input("Introduce longitud de cateto 2: "))
                        hipotenusa = int(input("Introduce longitud de hipotenusa: "))

                        seno = cateto_opuesto / hipotenusa 
                        coseno = cateto_contiguo / hipotenusa
                        tangente = cateto_opuesto / cateto_contiguo 

                        print(f"Cateto opuesto : {cateto_opuesto}")
                        print(f"Cateto contiguo : {cateto_contiguo}")
                        print(f"Hipotenusa : {hipotenusa}")

                        print(f"Seno : {seno}")
                        print(f"Coseno : {coseno}")
                        print(f"Tangente : {tangente}")

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                case "7":
                    try:
                        n = int(input("Introduce el número total de elementos: "))
                        r = int(input("Introduce el número de elementos a elegir en cada permutación: "))

                        permutations(n, r)

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                case "8":
                    try:
                        n = int(input("Introduce el número total de elementos: "))
                        r = int(input("Introduce el número de elementos a elegir en cada combinacion: "))

                        combinations(n, r)
                        
                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")


                # 👋 Program Exit
                # -----------------------------------
                
                case "9":

                    print("Saliendo de seccion matemáticas 📐")
                    break
                    break # the first break, breaks the match case , the second break the while

                case _:

                    print("❌ No has seleccionado ninguna opción válida.")


            # 👋 Exit Dialog
            # -----------------------------------

            option_break = input("Deseas salir del programa ? (Yes/No): ")

            if option_break.lower() == "y" or option_break.lower() == "yes":
                print("Saliendo de seccion matemáticas 📐")
                break
                break # the first break, breaks the match case , the second break the while

        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    
