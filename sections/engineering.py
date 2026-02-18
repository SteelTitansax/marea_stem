# Marea Chatbot STEM v1.0.0 (Engineering chatbot section)
# ---------------------------------------------------------------------------------------------------------------------------
# Purpose : Engineering tools section (RAG Engineering Knowledge)
# ---------------------------------------------------------------------------------------------------------------------------
# Author : Manuel Portero Leiva
# ---------------------------------------------------------------------------------------------------------------------------

import warnings
warnings.filterwarnings("ignore", message="pkg_resources is deprecated as an API")

import os
from constants import *
from utils.engineering_utils import *
import plotext as plt

# ------------------------
# Main Code Section
# ------------------------

def engineering_section():

    while True:

        try:

            # ❌ Clean screen
            os.system("clear")

            print("=" * num_layout_equals)
            print("👩💻  Marea Chatbot STEM — Sección Ingeniería")
            print("=" * num_layout_equals)
            print("🛠️  Bienvenido a la sección de ingeniería.")
            print("=" * num_layout_equals)
            print("Selecciona tu acción:")
            print("=" * num_layout_equals)
            print("=" * num_layout_equals)
            print("📘  Opción 0: RAG Perry's Chemical Handbook")
            print("📐  Opción 1: RAG Normativa UNE")
            print("📗  Opción 2: Optimización de equipos")
            print("🚪  Opción 3: Salir")
            print("=" * num_layout_equals)

            answer = input("👉  ¿Qué deseas hacer? (selecciona una opción): ")

            match answer:

                # 📘 Perry Handbook
                case "0":
                    try:

                        print("📄 Introduce la carpeta con los PDFs:")
                        folder = engineering_enciclopedia_path

                        # Load all PDFs
                        all_chunks = []
                        for file in os.listdir(folder):
                            if file.lower().endswith(".pdf"):
                                print(f"🔄 Cargando {file}...")
                                pdf_chunks = load_pdf_text(os.path.join(folder, file))
                                all_chunks.extend(pdf_chunks)

                        print("🧠 Cargando modelo de embeddings...")
                        model = SentenceTransformer(EMBED_MODEL)

                        print("📦 Construyendo índice vectorial...")
                        index, embeddings, metadatas = build_index(all_chunks, model)

                        os.system("clear")

                        while True:
                            print("\n❓ Escribe tu consulta técnica (o 'salir'):")
                            query = input(">> ")

                            if query.lower() == "salir":
                                print("👋 Finalizando.")
                                break

                            results = search(query, model, index, all_chunks, k=5)
                            print("\n📚 Fragmentos más relevantes:")
                            for i, (text, metadata) in enumerate(results, 1):
                                print(f"\n--- Resultado {i} ---")
                                print(f"📄 PDF: {metadata['pdf_name']}, Página: {metadata['page']}")
                                print(text[:500])
                        

                    except Exception as e:
                        print(f"❌ Error en RAG Perry: {e}")

                # 📐 Normativa UNE
                case "1":
                    try:
                        print("📄 Introduce la carpeta con los PDFs:")
                        folder = normative_path

                        # Load all PDFs
                        all_chunks = []
                        for file in os.listdir(folder):
                            if file.lower().endswith(".pdf"):
                                print(f"🔄 Cargando {file}...")
                                pdf_chunks = load_pdf_text(os.path.join(folder, file))
                                all_chunks.extend(pdf_chunks)

                        print("🧠 Cargando modelo de embeddings...")
                        model = SentenceTransformer(EMBED_MODEL)

                        print("📦 Construyendo índice vectorial...")
                        index, embeddings, metadatas = build_index(all_chunks, model)

                        os.system("clear")

                        while True:
                            print("\n❓ Escribe tu consulta técnica (o 'salir'):")
                            query = input(">> ")

                            if query.lower() == "salir":
                                print("👋 Finalizando.")
                                break

                            results = search(query, model, index, all_chunks, k=5)
                            print("\n📚 Fragmentos más relevantes:")
                            for i, (text, metadata) in enumerate(results, 1):
                                print(f"\n--- Resultado {i} ---")
                                print(f"📄 PDF: {metadata['pdf_name']}, Página: {metadata['page']}")
                                print(text[:500])

                    except Exception as e:
                        print(f"❌ Error en RAG UNE: {e}")


                # 📗 Optimización
                # -------------------------------------------------
                case "2":
                    try:
                        while True:

                            run_heat_exchanger()
                            answer = input("¿Quieres ejecutar la simulación del intercambiador? (Yes/No): ").strip().lower()

                            if answer.lower() == "yes" or answer.lower() == "y" :
                               break
                    
                    except Exception as e:
                        print(f"❌ Error en RAG Optimización: {e}")

                # 👋 Exit
                # -------------------------------------------------
                case "3":
                    print("Saliendo de sección ingeniería 🛠️")
                    break

                case _:
                    print("❌ No has seleccionado ninguna opción válida.")

            # 👋 Exit Dialog
            option_break = input("¿Deseas salir del programa? (Yes/No): ")

            if option_break.lower() in ["y", "yes"]:
                print("Saliendo de sección ingeniería 🛠️")
                break

        except Exception as e:
            print(f"❌ Error de selección: {e}")
