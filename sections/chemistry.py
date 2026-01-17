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
from utils.chem_utils import *
# ------------------------
# Main Code Section
# ------------------------

def chemistry_section():


    while True :

        try:
        
            # ❌ Clean screen
            # ----------------

            os.system("clear")
        

            print("=" * num_layout_equals)
            print("👩💻  Marea Chatbot STEM —  Seccion química")
            print("=" * num_layout_equals)
            print("⚗️  Bienvenido a la sección química.")
            print("=" * num_layout_equals)
            print("Selecciona tu acción:")
            print("=" * num_layout_equals)
            print("=" * num_layout_equals)
            print("🧪  Opción 0: Descripción de compuesto químico")
            print("🔬  Opción 1: Descripción de elemento químico")
            print("⚗️   Opción 2: Descripción de reacción química , obtención de datos termodinamicos de equilibrio")
            print("🚪  Opción 3: Salir")
            print("=" * num_layout_equals)


            answer = input("👉  ¿Qué deseas hacer? (selecciona una opción): ")


            match answer:

                # 🧪    Molecule query
                # -------------------------------------------------

                case "0":
                    try:
                        print("⚙️ Consultando molécula ...")
                        formula = input("Introduce formula del compuesto químico: ")
                        molecules_description(formula)
                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # 🔬    Element query
                # -------------------------------------------------

                case "1":
                    try:
                        print("⚙️ Consultando elemento ...")
                        simbolo = input("Introduce símbolo del elemento químico: ")
                        element_info(simbolo)
                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")
                
                # ⚗️    Reaction query
                # -------------------------------------------------

                case "2":
                    try:
                        print("⚙️ Consultando reaccion ...")
                        react1 = input("Introduce el simbolo de la primera molecula: ")
                        react2 = input("Introduce el simbolo de la segunda molecula: ")
                        product1 = input("Introduce el simbolo del primer producto: ")
                        product2 = input("Introduce el simbolo del segundo producto: ")

                        analize_reaction(react1,react2,product1,product2)

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")
                
                # 👋 Program Exit
                # -----------------------------------
                
                case "3":

                    print("Saliendo de seccion química ⚗️")
                    break
                    break # the first break, breaks the match case , the second break the while

                case _:

                    print("❌ No has seleccionado ninguna opción válida.")


            # 👋 Exit Dialog
            # -----------------------------------

            option_break = input("Deseas salir del programa ? (Yes/No): ")

            if option_break.lower() == "y" or option_break.lower() == "yes":
                print("Saliendo de seccion química ⚗️ ")
                break
                break # the first break, breaks the match case , the second break the while

        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    
