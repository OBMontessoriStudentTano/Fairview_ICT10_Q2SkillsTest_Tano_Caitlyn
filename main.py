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

elements = {**Solids, **Liquids, **Gases}
states = {
        **dict.fromkeys(Solids, "Solid"),
        **dict.fromkeys(Liquids, "Liquid"),
        **dict.fromkeys(Gases, "Gas"),
}

def enter(event):
    symbol = document.querySelector("#text1").value.strip()

    name, number, mass = elements.get(symbol, ("Element is not found", state = states.get(symbol, "-")))

     document.querySelector("#details").innerHTML = f"""
         <h2>Element Details</h2>
         <b>Symbol:</b> {symbol or "-"}<br>
         <b>Element:</b> {name}<br>
         <b>Atomic Number:</b> {number}<br>
         <b>Atomic Mass:</b> {mass}<br>
         <b>Physical State:</b> {state}<br>
     """





    