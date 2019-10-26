from enum import Enum


class PROGRAMMSCHWERPUNKT(Enum):
    All = 0
    EinsatzInDerSekundarStufe1 = 1
    EinsatzInDerSekundarStufe2 = 2
    EchteTeilhabe = 3
    NeuePerspektiven = 4
    StarkeBasis = 5


def StringToPROGRAMMSCHWERPUNKT(string):
    stringLower = string.lower()
    if "starke basis" in stringLower:
        return PROGRAMMSCHWERPUNKT.StarkeBasis
    elif "echte teilhabe" in stringLower:
        return PROGRAMMSCHWERPUNKT.EchteTeilhabe
    elif "neue perspektiven" in stringLower:
        return PROGRAMMSCHWERPUNKT.NeuePerspektiven
    elif "sicherer " in stringLower:
        return PROGRAMMSCHWERPUNKT.EinsatzInDerSekundarStufe1
    else:
        return PROGRAMMSCHWERPUNKT.All

def SchwerpunkteToString(item):
    if item is PROGRAMMSCHWERPUNKT.StarkeBasis:
        return "Starke Basis"
    elif item is PROGRAMMSCHWERPUNKT.EchteTeilhabe:
        return "Echte Teilhabe"
    elif item is PROGRAMMSCHWERPUNKT.NeuePerspektiven:
        return "Neue Perspektiven"
    elif item is PROGRAMMSCHWERPUNKT.EinsatzInDerSekundarStufe1:
        return "Sicherer Uebergang in die Sekundarstufe I"
    else:
        return "Keine Präferenzen"