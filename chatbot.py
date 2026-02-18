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
from constants import *
from sections.mathematics import *
from sections.chemistry import *
from sections.physics import *
from sections.data_analysis import *
from sections.engineering import *

# ------------------------
# Main Code Section
# ------------------------

if __name__ == "__main__":


    while True :

        try:
        
            # ❌ Clean screen
            # ----------------

            os.system("clear")
        

            print("=" * num_layout_equals)
            print("👩💻  Marea Chatbot STEM —  Release v1.0.0   (Autor: Manuel Portero Leiva)")
            print("=" * num_layout_equals)
            print("🌊 Hola, soy Marea (STEM Version), tu asistente virtual.")
            print("=" * num_layout_equals)
            print("Selecciona tu sección:")
            print("=" * num_layout_equals)
            print("=" * num_layout_equals)
            print("🧮  Opción 0: Matemáticas")      
            print("🧪  Opción 1: Química")          
            print("🔬  Opción 2: Física")           
            print("🛠️   Opción 3: Ingeniería")       
            print("📈  Opción 4: Análisis de datos")
            print("🚪  Opción 5: Salir")            

            print("=" * num_layout_equals)

            answer = input("👉  ¿Qué deseas hacer? (selecciona una opción): ")

            match answer:

                # ⚙️  Math section
                # ----------------------

                case "0":

                    try:
                        print("⚙️ Entrando en sección matemáticas")
                        mathematics_section()
                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # 📜 Chemistry section
                # ----------------------

                case "1":
                    try:
                        print("📜 Entrando en sección química")
                        chemistry_section()
                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # ⚙️  Physics section
                # -------------------------------------------------

                case "2":
                    try:
                        print("⚙️ Entrando en sección física")
                        physics_section()

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # 🛠️   Engineering section
                # -------------------------------------------------

                case "3":
                    try:
                        print("🛠️  Entrando en sección ingenieria")
                        engineering_section()

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")


                # 📊  Data analytics
                # -------------------------------------------------
                
                case "4":
                    try:
                        print("🧰 Entrando en la sección de análisis de datos")
                        quick_analysis()

                    except Exception as e:
                        print(f"❌ Error al realizar la acción : {e}")

                # 👋 Program Exit
                # -----------------------------------
                
                case "5":

                    print("Espero haberte ayudado 👋")
                    break
                    break # the first break, breaks the match case , the second break the while

                case _:

                    print("❌ No has seleccionado ninguna opción válida.")


            # 👋 Exit Dialog
            # -----------------------------------

            option_break = input("Deseas salir del programa ? (Yes/No): ")

            if option_break.lower() == "y" or option_break.lower() == "yes":
                print("Espero haberte ayudado 👋")
                break
                break # the first break, breaks the match case , the second break the while

        except Exception as e:
            print(f"❌ Error de seleccion: {e}")    
