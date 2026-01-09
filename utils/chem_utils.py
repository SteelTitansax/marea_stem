# chempy_rdkit_terminal.py
from chempy import *
import periodictable
from chempy.util.periodic import symbols
from rdkit import Chem


def molecules_description(formula):

    # =========================
    # Propiedades con ChemPy
    # =========================
    sustancia = Substance.from_formula(formula)

    print("=== Propiedades Químicas ===")
    print(f"Fórmula: {formula}")
    print("Composición elemental (números atómicos):", sustancia.composition)

    print("\nComposición legible:")
    for Z, cantidad in sustancia.composition.items():
        print(f"  {symbols[Z-1]}: {cantidad}")  # Z-1 corrige índice

    masa = round(sustancia.molar_mass(), 3)
    print(f"\nMasa molar: {masa} g/mol")

    num_atomos = sum(sustancia.composition.values())
    print(f"Número total de átomos: {num_atomos}")

    # =========================
    # Estructura molecular en texto con RDKit
    # =========================
    # Diccionario SMILES para moléculas conocidas
    smiles_dict = {
        "C2H6O": "CCO",
        "CH4": "C",
        "H2O": "O",
        "CO2": "O=C=O",
        "C6H6": "c1ccccc1"
    }

    smiles = smiles_dict.get(formula)

    if smiles is None:
        print("\nNo se encontró SMILES para la fórmula. Solo se muestran propiedades.")
    else:
        mol = Chem.MolFromSmiles(smiles)
        
        print("\n=== Estructura Molecular (texto) ===")
        print(f"SMILES: {Chem.MolToSmiles(mol)}")
        
        print("\nÁtomos:")
        for atom in mol.GetAtoms():
            print(f"Índice {atom.GetIdx():2d} → {atom.GetSymbol()}, "
                f"valencia={atom.GetTotalValence()}, "
                f"Hs={atom.GetTotalNumHs()}")
        
        print("\nEnlaces:")
        for bond in mol.GetBonds():
            a1 = bond.GetBeginAtom().GetSymbol()
            a2 = bond.GetEndAtom().GetSymbol()
            print(f"{a1} - {a2}  tipo={bond.GetBondType()}")

def getElementAttribute(Z, attr):
    return getattr(periodic, attr, {}).get(Z, "No disponible")

def element_info(symbol):
    """
    Imprime información completa de un elemento químico usando periodictable.
    """

    symbol = symbol.capitalize()  # Asegura que la primera letra sea mayúscula

    try:
        element = periodictable.elements.symbol(symbol)
    except KeyError:
        print(f"❌ Símbolo químico '{symbol}' no válido")
        return

    print("\n=== Información completa del elemento químico ===")
    print(f"Símbolo químico        : {element.symbol}")
    print(f"Número atómico         : {element.number}")
    print(f"Nombre                 : {element.name}")
    print(f"Masa atómica (u)       : {element.mass}")
    print(f"Densidad (g/cm³)       : {getattr(element, 'density', 'No disponible')}")
    