import os
import pandas as pd
import plotext as plt  
from constants import num_layout_equals

def quick_analysis():
    """
    Analiza un CSV y genera un resumen completo con gráficos en terminal usando plotext.
    """

    while True:
        try:
            os.system("clear")
            print("=" * num_layout_equals)
            print("📊  Marea Chatbot STEM — Sección Análisis de CSV con gráficos")
            print("=" * num_layout_equals)

            ruta = input("Introduce la ruta del archivo CSV (o 'salir' para volver al menú): ").strip()
            if ruta.lower() == "salir":
                break

            if not os.path.exists(ruta):
                print("❌ Archivo no encontrado. Verifica la ruta.")
                input("Presiona Enter para continuar...")
                continue

            # Leer CSV
            df = pd.read_csv(ruta)

            # Información general
            print("\n=== Información general del CSV ===")
            print(f"Filas    : {df.shape[0]}")
            print(f"Columnas : {df.shape[1]}")
            print(f"Nombres de columnas: {list(df.columns)}\n")

            # Mostrar primeras filas
            print("=== Primeras filas del CSV ===")
            print(df.head(5).to_string(index=False))  # Muestra 5 primeras filas sin índice
            print("\n")

            # Tipos de datos y valores faltantes
            print("=== Tipos de datos y valores faltantes ===")
            for col in df.columns:
                tipo = str(df[col].dtype)
                faltantes = df[col].isna().sum()
                print(f"{col:20} | Tipo: {tipo:10} | Valores faltantes: {faltantes}")


            # Estadísticas de columnas numéricas
            num_cols = df.select_dtypes(include='number').columns
            if len(num_cols) > 0:
                print("\n=== Estadísticas de columnas numéricas ===")
                print(df[num_cols].describe().transpose())

                graphic_answer = input("Deseas graficar el histograma de los datos introducidos ? (Yes/No): ")

                # Graficar histogramas para cada columna numérica
                for col in num_cols:
                    plt.clf()
                    plt.hist(df[col].dropna(), bins=10, color="white")
                    plt.title(f"Histograma: {col}")
                    plt.canvas_color("black")
                    plt.clear_color()
                    plt.show()
                    plt.sleep(0.5)  # Pequeña pausa entre gráficos

                
            else:
                print("\nNo se detectaron columnas numéricas para graficar.")

            input("\nPresiona Enter para continuar...")

        except Exception as e:
            print(f"❌ Error al procesar el CSV: {e}")
            input("Presiona Enter para continuar...")
