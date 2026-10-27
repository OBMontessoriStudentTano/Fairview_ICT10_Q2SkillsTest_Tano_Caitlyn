from pyscript import document

Solids = {
    "C": ("Carbon", 6, "12.011 u"),
    "P": ("Phosphorus", 15, "30.974 u"),
    "S": ("Sulfur", 16, "32.06 u"),
    "Se": ("Selenium", 34, "78.96 u"),
    "I": ("Iodine", 53, "126.904 u"),
}

Liquids = {
    "Br": ("Bromine", 35, "79.904 u"),
}

Gases = {
    "H": ("Hydrogen", 1, "1.008 u"),
    "He": ("Helium", 2, "4.00 u"),
    "N": ("Nitrogen", 7, "14.007 u"),
    "O": ("Oxygen", 8, "15.999 u"),
    "F": ("Fluorine", 9, "18.998 u"),
    "Ne": ("Neon", 10, "20.180 u"),
    "Cl": ("Chlorine", 17, "35.45 u"),
    "Ar": ("Argon", 18, "39.948 u"),
    "Kr": ("Krypton", 36, "83.798 u"),
    "Xe": ("Xenon", 54, "131.29 u"),
    "Rn": ("Radon", 86, "222 u"),
}

elements = {}
elements.update(Solids)
elements.update(Liquids)
elements.update(Gases)

def enter(event):


    
    # Get the element symbol
    element_symbol = document.querySelector("#text1").value.strip()
    element_symbol = element_symbol.capitalize()

    result = elements.get(element_symbol, ("Element not found", "-", "-")    
    )

    name, atomic_number, atomic_mass = result

    state = {
        **dict.fromkeys(Solids, "Solid"),
        **dict.fromkeys(Liquids, "Liquid"),
        **dict.fromkeys(Gases, "Gas"),
    }.get(element_symbol, "-")

     document.querySelector("#details").innerHTML = f"""
         <h2>Element Details</h2>
         <b>Symbol:</b> {element_symbol or "-"}<br>
         <b>Element:</b> {name}<br>
         <b>Atomic Number:</b> {atomic_number}<br>
         <b>Atomic Mass:</b> {atomic_mass}<br>
         <b>Physical State:</b> {state}<br>
     """





    