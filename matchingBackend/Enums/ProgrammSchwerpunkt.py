from enum import Enum


class PROGRAMMSCHWERPUNKT(Enum):
    All = 0
    EinsatzInDerSekundarStufe1 = 1
    EinsatzInDerSekundarStufe2 = 2
    EchteTeilhabe = 3
    NeuePerspektiven = 4
    StarkeBasis = 5


def StringToENUM(string):
    stringLower = string.lower()
    if "starke basis" in stringLower:
        return PROGRAMMSCHWERPUNKT.StarkeBasis
    elif "echte teilhabe" in stringLower:
        return PROGRAMMSCHWERPUNKT.EchteTeilhabe
    elif "neue perspektiven" in stringLower:
        return PROGRAMMSCHWERPUNKT.NeuePerspektiven
    else:
        return PROGRAMMSCHWERPUNKT.All

def SchwerpunkteToString(item):
    if item is PROGRAMMSCHWERPUNKT.StarkeBasis:
        return "Starke Basis"
    elif item is PROGRAMMSCHWERPUNKT.EchteTeilhabe:
        return "Echte Teilhabe"
    elif item is PROGRAMMSCHWERPUNKT.NeuePerspektiven:
        return "Neue Perspektiven"
    else:
        return "Keine Präferenzen"