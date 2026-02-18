import os
import numpy as np
import plotext as plt
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

# ==============================
# Base de datos de fluidos
# ==============================
fluids = {
    "Agua": {"Cp": 4180, "T_min": 273, "T_max": 373},
    "Aceite térmico": {"Cp": 2000, "T_min": 300, "T_max": 600},
    "Aire": {"Cp": 1005, "T_min": 250, "T_max": 800},
    "Etilenglicol": {"Cp": 2400, "T_min": 260, "T_max": 450}
}

# ==============================
# Función para seleccionar fluido
# ==============================
def pick_fluid(fluids, prompt):
    nombres = list(fluids.keys())
    print(prompt)
    for i, nombre in enumerate(nombres, 1):
        print(f"{i}. {nombre}")
    choice = int(input("> ")) - 1
    return nombres[choice], fluids[nombres[choice]]

# ==============================
# Simulación intercambiador de calor
# ==============================
def run_heat_exchanger():
    print("=== Simulador de Intercambiador de Calor ===\n")
    
    hot_name, hot = pick_fluid(fluids, "Selecciona fluido CALIENTE:")
    cold_name, cold = pick_fluid(fluids, "Selecciona fluido FRÍO:")

    m_hot = float(input("\nCaudal fluido caliente [kg/s]: "))
    m_cold = float(input("Caudal fluido frío [kg/s]: "))

    T_in_hot = float(input("Temperatura entrada caliente [K]: "))
    T_in_cold = float(input("Temperatura entrada fría [K]: "))

    Cp_hot = hot["Cp"]
    Cp_cold = cold["Cp"]

    T_out_hot_min = max(hot["T_min"], T_in_cold)
    T_out_hot_max = min(hot["T_max"], T_in_hot)
    T_out_hot_range = np.linspace(T_out_hot_min, T_out_hot_max, 100)

    Q_list = []
    T_out_cold_list = []

    for T_out_hot in T_out_hot_range:
        Q = m_hot * Cp_hot * (T_in_hot - T_out_hot)
        T_out_cold = T_in_cold + Q / (m_cold * Cp_cold)
        Q_list.append(Q)
        T_out_cold_list.append(T_out_cold)

    Q_list_kW = np.array(Q_list) / 1000

    print("\n=== Resultados ===")
    print(f"Fluido caliente: {hot_name}")
    print(f"Fluido frío: {cold_name}")
    print(f"Rango T salida caliente: {T_out_hot_min:.2f} – {T_out_hot_max:.2f} K")
    print(f"Calor máximo transferido: {max(Q_list_kW):.2f} kW")
    print(f"T salida fría máxima: {max(T_out_cold_list):.2f} K")

    plt.clear_data()
    plt.plot(T_out_hot_range, Q_list_kW)
    plt.xlabel("T salida fluido caliente [K]")
    plt.ylabel("Calor transferido Q [kW]")
    plt.title(f"Q vs T_out_hot | {hot_name} -> {cold_name}")
    plt.grid(True)
    plt.canvas_color("black")
    plt.clear_color()
    plt.show()
    print()
    plt.clear_data()
    plt.plot(T_out_hot_range, T_out_cold_list)
    plt.xlabel("T salida fluido caliente [K]")
    plt.ylabel("T salida fluido frío [K]")
    plt.title(f"T_out_cold vs T_out_hot | {hot_name} -> {cold_name}")
    plt.grid(True)
    plt.canvas_color("black")
    plt.clear_color()
    plt.show()


# =========================
# CONFIG
# =========================
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 500  # characters per chunk

# =========================
# PDF LOADER WITH METADATA
# =========================
def load_pdf_text(pdf_path: str):
    reader = PdfReader(pdf_path)
    chunks = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            start = 0
            while start < len(text):
                chunk_text = text[start:start+CHUNK_SIZE]
                metadata = {
                    "pdf_name": os.path.basename(pdf_path),
                    "page": page_number
                }
                chunks.append((chunk_text, metadata))
                start += CHUNK_SIZE
    return chunks

# =========================
# BUILD VECTOR INDEX
# =========================
def build_index(all_chunks, model):
    texts = [c[0] for c in all_chunks]
    metadatas = [c[1] for c in all_chunks]

    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index, embeddings, metadatas

# =========================
# RETRIEVAL
# =========================
def search(query, model, index, all_chunks, k=5):
    query_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, k)
    results = []
    for i in indices[0]:
        text, metadata = all_chunks[i]
        results.append((text, metadata))
    return results

