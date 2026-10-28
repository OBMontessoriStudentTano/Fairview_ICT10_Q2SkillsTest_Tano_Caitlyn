from pyscript import document, display

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

elements = {**Solids, **Liquids, **Gases}
states = {
        **dict.fromkeys(Solids, "Solid"),
        **dict.fromkeys(Liquids, "Liquid"),
        **dict.fromkeys(Gases, "Gas"),
}

def enter(event):

    element_symbol = document.querySelector("#text1").value.strip()
    element_symbol = element_symbol.capitalize()

    name, number, mass = elements.get(
        
        element_symbol, ("Element not found", "-", "-")
    )

    state = {
        **dict.fromkeys(Solids, "Solid"),
        **dict.fromkeys(Liquids, "Liquid"),
        **dict.fromkeys(Gases, "Gas"),
    }

    state = states.get(element_symbol, "-")

    document.querySelector("#details").innerHTML = f"""
<h2>Element Details</h2>
<p>Symbol:<span class="symbol">{element_symbol or "-"}</span></p>
<p>Element:<span class="element-name">{name}</span></p>
<p>Atomic Number:<span class="atomic-number">{number}</span></p>
<p>Atomic Mass:<span class="atomic-mass">{mass}</p>
<p>Physical State:<span class="physical-state">{state}</span></p>
"""





    