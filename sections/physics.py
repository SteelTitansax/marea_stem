import os
import math
from utils.physics_utils import *
from constants import num_layout_equals,G, k
def physics_section():

    while True:

        try:
            # ❌ Limpiar pantalla
            os.system("clear")

            print("=" * num_layout_equals)
            print("👩💻  Marea Chatbot STEM — Sección Física Clásica")
            print("=" * num_layout_equals)
            print("⚛️  Bienvenido a la sección de física clásica.")
            print("=" * num_layout_equals)
            print("Selecciona tu acción:")
            print("=" * num_layout_equals)
            print("🎯  Opción 0: Cinemática")
            print("⚙️   Opción 1: Dinámica")
            print("🌍  Opción 2: Gravedad clásica")
            print("⚡  Opción 3: Electromagnetismo")
            print("🚪  Opción 4: Salir")
            print("=" * num_layout_equals)

            answer = input("👉  ¿Qué deseas hacer? (selecciona una opción): ")

            match answer:

                # 🎯 CINEMÁTICA
                case "0":
                    try:
                        print("⚙️ Calculando cinemática ...")

                        # Entrada de datos
                        v0 = float(input("Velocidad inicial (m/s): "))
                        a = float(input("Aceleración (m/s²): "))
                        t = float(input("Tiempo (s): "))

                        kinematics(v0,a,t)

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # ⚙️ DINÁMICA
                case "1":
                    try:
                        print("⚙️ Calculando dinámica ...")
                        m = float(input("Masa del objeto (kg): "))
                        F = float(input("Fuerza aplicada (N): "))

                        dynamics(F,m)
                        
                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # 🌍 GRAVEDAD CLÁSICA
                case "2":
                    try:
                        print("⚙️ Calculando gravedad clásica ...")
                        m1 = float(input("Masa del primer objeto (kg): "))
                        m2 = float(input("Masa del segundo objeto (kg): "))
                        r = float(input("Distancia entre objetos (m): "))
                        
                        classic_gravity(G,m1,m2,r)
                        

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # ⚡ ELECTROMAGNETISMO
                case "3":
                    try:
                        print("⚙️ Calculando fuerza eléctrica ...")
                        
                        q1 = float(input("Carga 1 (C): "))
                        q2 = float(input("Carga 2 (C): "))
                        r = float(input("Distancia entre cargas (m): "))

                        coulomb(k,q1,q2,r)
                        

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # 🚪 Salir
                case "4":
                    print("Saliendo de sección física ⚛️")
                    break

                # ❌ Opción no válida
                case _:
                    print("❌ No has seleccionado ninguna opción válida.")

            # 👋 Preguntar si quiere salir del programa
            option_break = input("Deseas salir del programa ? (Yes/No): ")
            if option_break.lower() in ["y", "yes"]:
                print("Saliendo de sección física ⚛️")
                break

        except Exception as e:
            print(f"❌ Error de selección: {e}")
