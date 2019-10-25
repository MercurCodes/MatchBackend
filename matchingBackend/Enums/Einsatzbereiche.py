from enum import Enum


class EINSATZBEREICH(Enum):
    All = 0
    Sport = 1
    Kreativ = 2
    Interkulturell = 3
    Musik = 4
    Natur = 5
    Digitales = 6

def StringToEINSATZBEREICH(string):
    stringLower = string.lower()
    if "sport" in stringLower:
        return EINSATZBEREICH.Sport
    elif "kreativ" in stringLower:
        return EINSATZBEREICH.Kreativ
    elif "natur" in stringLower:
        return EINSATZBEREICH.Natur
    elif "musik" in stringLower:
        return EINSATZBEREICH.Musik
    elif "digitales" in stringLower:
        return EINSATZBEREICH.Digitales
    elif "inter" in stringLower:
        return EINSATZBEREICH.Interkulturell
    else:
        return EINSATZBEREICH.All

def EinsatzBereichToString(einsatzbereich):
    if einsatzbereich is EINSATZBEREICH.Sport:
        return "Sport"
    elif einsatzbereich is EINSATZBEREICH.Kreativ:
        return "Kreativ"
    elif einsatzbereich is EINSATZBEREICH.Natur:
        return "Natur"
    elif einsatzbereich is EINSATZBEREICH.Interkulturell:
        return "Interkulturell"
    elif einsatzbereich is EINSATZBEREICH.Musik:
        return "Musik"
    elif einsatzbereich is EINSATZBEREICH.Digitales:
        return "Digitales"
    else:
        return "Keine Praeferenzen"