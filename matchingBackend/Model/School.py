from matchingBackend.Enums import Bundeslaender
from matchingBackend.Enums.Bundeslaender import BundeslandToString
from matchingBackend.Enums.Einsatzbereiche import EinsatzBereichToString
from matchingBackend.Enums.ProgrammSchwerpunkt import PROGRAMMSCHWERPUNKT


class School():

    Priority = 0

    Stadt = ""
    Bundesland = Bundeslaender.BUNDESLAND.All
    Einsatzbereich = []
    Schwerpunkt = PROGRAMMSCHWERPUNKT.All

def SchoolToJSON(school):
    JSONdata = {}
    JSONdata["Prioritaet"] = school.Priority
    JSONdata["stadt"] = school.Stadt
    JSONdata["Bundesland"] = BundeslandToString(school.Bundesland)
    JSONdata["Einsatzbereich"] = [EinsatzBereichToString(item) for item in school.Einsatzbereich]
    JSONdata["Schwerpunkt"] = EinsatzBereichToString(school.Schwerpunkt)
    return JSONdata

