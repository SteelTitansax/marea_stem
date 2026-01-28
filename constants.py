import os
from pathlib import Path

# Input and output dirs
# ----------------------
home = Path.home()

INPUT_DIR = Path(f"{home}/marea_stem/chatbot_input")
OUTPUT_DIR = Path(f"{home}/marea_stem/chatbot_output")
DATA_DIR = Path(f"{home}/Data")

# Get terminal width 
# ---------------------
terminal_width = os.get_terminal_size().columns

# Adjust the number of "=" to the terminal width
# -----------------------------------------------
num_layout_equals = terminal_width

# Config 
# ---------------------

DB_PATH = "./data.db"

G = 6.67430e-11 # Constante de gravitación universal

k = 8.9875517923e9  # Constante de Coulomb (N·m²/C²)

R = 8.314  # J/mol/K
