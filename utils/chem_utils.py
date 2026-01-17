# chempy_rdkit_terminal.py
from chempy import *
import periodictable
from chempy.util.periodic import symbols
from rdkit import Chem
import pubchempy as pcp
import requests

def get_use_and_manufacturing(cid):
    """
    Obtiene la sección 'Use and Manufacturing' de un compuesto de PubChem usando la API PUG-View.
    """
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error al obtener datos:", response.status_code)
        return None
    
    data = response.json()
    
    # Buscar la sección "Use and Manufacturing"
    use_section = None
    for section in data.get("Record", {}).get("Section", []):
        if section.get("TOCHeading") == "Use and Manufacturing":
            use_section = section
            break
    
    if not use_section:
        print("No se encontró la sección 'Use and Manufacturing'.")
        return None
    
    # Extraer subsecciones y texto
    extracted = {}
    for subsection in use_section.get("Section", []):
        heading = subsection.get("TOCHeading")
        # Algunos tienen múltiples textos en 'Information'
        texts = []
        for info in subsection.get("Information", []):
            if "Value" in info and "StringWithMarkup" in info["Value"]:
                for item in info["Value"]["StringWithMarkup"]:
                    texts.append(item.get("String"))
        extracted[heading] = texts
    
    return extracted



    

def molecules_description(formula):

    # =========================
    # Propiedades con ChemPy
    # =========================
    substance = Substance.from_formula(formula)

    print("\n=== Propiedades Químicas ===\n")
    print(f"Fórmula: {formula}")
    print("Composición elemental (números atómicos):", substance.composition)

    print("Composición legible:")
    for Z, quantity in substance.composition.items():
        print(f"  {symbols[Z-1]}: {quantity}")  # Z-1 corrige índice

    mass = round(substance.molar_mass(), 3)
    print(f"Masa molar: {mass} g/mol")

    num_atoms = sum(substance.composition.values())
    print(f"Número total de átomos: {num_atoms}")
    
    print("\n=== Propiedades avanzadas ===\n")
    
    extended_substance = pcp.get_compounds(substance.name,'name')
    extended_substance_info = extended_substance[0]
   
    
    # Extended information

    print("CID:", extended_substance_info.cid)
    print("Nombre IUPAC:", extended_substance_info.iupac_name)
    print("Fórmula molecular:", extended_substance_info.molecular_formula)

    # Identifiers

    print("InChI:", extended_substance_info.inchi)
    print("SMILES:", extended_substance_info.smiles)

    print("\n=======Substance Usage=========\n")

    usage_data = get_use_and_manufacturing(extended_substance_info.cid)
    
    if usage_data:
        for section, texts in usage_data.items():
            print(f"\n=== {section} ===\n")
            for text in texts:
                print("-", text)

def element_info(symbol):
    """
    Imprime información completa de un elemento químico usando periodictable.
    """
    symbol = symbol.capitalize()  # Asegura que la primera letra sea mayúscula

    try:
        element = periodictable.elements.symbol(symbol)

        extended_element = pcp.get_compounds(element.name,'name')
        extended_element_info = extended_element[0]
        



    except KeyError:
        print(f"❌ Símbolo químico '{symbol}' no válido")
        return
    
    # Basic information
    
    print("\n=== Información completa del elemento químico ===\n")
    print(f"Símbolo químico        : {element.symbol}")
    print(f"Número atómico         : {element.number}")
    print(f"Nombre                 : {element.name}")
    print(f"Masa atómica (u)       : {element.mass}")
    print(f"Densidad (g/cm³)       : {getattr(element, 'density', 'No disponible')}")
    
    # Extended information

    print("CID:", extended_element_info.cid)
    print("Nombre IUPAC:", extended_element_info.iupac_name)
    print("Fórmula molecular:", extended_element_info.molecular_formula)
    
    # Identifiers

    print("InChI:", extended_element_info.inchi)
    print("SMILES:", extended_element_info.smiles)

    print("\n=============== Element Usage =================\n")

    usage_data = get_use_and_manufacturing(extended_element_info.cid)
    
    if usage_data:
        for section, texts in usage_data.items():
            print(f"\n=== {section} ===\n")
            for text in texts:
                print("-", text)


def analize_reaction(react1,react2,product1,product2):

    if react1 == '' or react2 == '':
        reactive = react1 + react2
        reaction = balance_stoichiometry({reactive},{product1,product2})
    elif product1 == '' or product2 == '':
        product = product1 + product2 
        reaction = balance_stoichiometry({react1,react2},{product})
    else :
        reaction = balance_stoichiometry({react1,react2},{product1,product2})
    
    reaction_converted = Reaction(*reaction)
    reaction_keys = reaction_converted.keys()
    reaction_order = reaction_converted.order()

    print(f"Reaction described : {reaction_converted.string()}")
    print(f"Reaction keys : {reaction_keys}")
    print(f"Reaction order : {reaction_order}")
    
