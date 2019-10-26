from enum import Enum


class BUNDESLAND(Enum):
    All = 0
    BadenWuerttemberg = 1
    Bayern = 2
    Berlin = 3
    Brandenburg = 4
    Bremen = 5
    Hamburg = 6
    Hessen = 7
    MecklenburgVorpommern = 8
    Niedersachsen = 9
    NordrheinWestfalen = 10
    RheinlandPfalz = 11
    Saarland = 12
    Sachsen = 13
    SachsenAnhalt = 14
    SchleswigHolstein = 15
    Thueringen = 16

def StringToBUNDESLAND(string):
    stringLower = string.lower()
    if "baden" in stringLower:
        return BUNDESLAND.BadenWuerttemberg
    elif "bayern" in stringLower:
        return BUNDESLAND.Bayern
    elif "berlin" in stringLower:
        return BUNDESLAND.Berlin
    elif "brandenburg" in stringLower:
        return BUNDESLAND.Brandenburg
    elif "bremen" in stringLower:
        return BUNDESLAND.Bremen
    elif "hamburg" in stringLower:
        return BUNDESLAND.Hamburg
    elif "hessen" in stringLower:
        return BUNDESLAND.Hessen
    elif "mecklenburg" in stringLower:
        return BUNDESLAND.MecklenburgVorpommern
    elif "nieder" in stringLower:
        return BUNDESLAND.Niedersachsen
    elif "nord" in stringLower:
        return BUNDESLAND.NordrheinWestfalen
    elif "rheinland" in stringLower:
        return BUNDESLAND.RheinlandPfalz
    elif "saarland" in stringLower:
        return BUNDESLAND.Saarland
    elif "sachsen-" in stringLower:
        return BUNDESLAND.Sachsen
    elif "sachsen" in stringLower:
        return BUNDESLAND.SachsenAnhalt
    elif "schleswig" in stringLower:
        return BUNDESLAND.SchleswigHolstein
    elif "thueringen" in stringLower:
        return BUNDESLAND.Thueringen
    else:
        return BUNDESLAND.All

def BundeslandToString(item):
        if item is BUNDESLAND.BadenWuerttemberg:
            return "Baden-Wuerttemberg"
        elif item is BUNDESLAND.Bayern:
            return "Bayern"
        elif item is BUNDESLAND.Berlin:
            return "Berlin"
        elif item is BUNDESLAND.Brandenburg:
            return "Brandenburg"
        elif item is BUNDESLAND.Bremen:
            return
        elif item is BUNDESLAND.Hamburg:
            return "Hamburg"
        elif item is BUNDESLAND.Hessen:
            return "Hessen"
        elif item is BUNDESLAND.MecklenburgVorpommern:
            return "Mecklenburg-Vorpommern"
        elif item is BUNDESLAND.Niedersachsen:
            return "Niedersachsen"
        elif item is BUNDESLAND.NordrheinWestfalen:
            return "Nordrhein-Westfalen"
        elif item is BUNDESLAND.RheinlandPfalz:
            return "Rheinland-Pfalz"
        elif item is BUNDESLAND.Saarland:
            return "Saarland"
        elif item is BUNDESLAND.Sachsen:
            return "Sachsen"
        elif item is BUNDESLAND.SachsenAnhalt:
            return "Sachsen-Anhalt"
        elif item is BUNDESLAND.SchleswigHolstein:
            return "Schleswig Holstein"
        elif item is BUNDESLAND.Thueringen:
            return "Thueringen"
        else:
            return "Keine Praeferenz"


