from matchingBackend.Enums import Bundeslaender
from matchingBackend.Enums.Bundeslaender import BundeslandToString
from matchingBackend.Enums.Einsatzbereiche import EinsatzBereichToString
from matchingBackend.Enums.ProgrammSchwerpunkt import PROGRAMMSCHWERPUNKT

distance_score_factor = 0.5
schwerpunkt_score_factor = 0.25
einsatzbereichs_score_factor = 0.25

class School():

    Priority = 0

    Stadt = ""
    Bundesland = Bundeslaender.BUNDESLAND.All
    Einsatzbereich = []
    Schwerpunkt = PROGRAMMSCHWERPUNKT.All

    def generateMatchingFellow(self, fellow):
        distance_score = fellow.distance_rating
        schwerpunkt_score = self.calculateSchwerpunktScore(fellow) # generate a schwerpunkt matching score
        einsatzbereichs_score = self.calculateEinsatzBereichScore(fellow) #generate a einsatzsbereichs score
        matched_fellow = fellow.deepCopy()
        matched_fellow.rating = distance_score * distance_score_factor \
                                + schwerpunkt_score * schwerpunkt_score_factor \
                                + einsatzbereichs_score * einsatzbereichs_score_factor
        return matched_fellow

    def calculateEinsatzBereichScore(self, fellow):
        maxMatch = len(self.Einsatzbereich)
        matchPoints = len(list(set(self.Einsatzbereich).intersection(fellow.einsatzBereiche)))
        return (matchPoints / maxMatch) * 100


    def calculateSchwerpunktScore(self, fellow):
        if self.Schwerpunkt in fellow.schwerpuntke or PROGRAMMSCHWERPUNKT.All in fellow.schwerpuntke :
            return 100
        else:
            return 0

def SchoolToJSON(school):
    JSONdata = {}
    JSONdata["Prioritaet"] = school.Priority
    JSONdata["stadt"] = school.Stadt
    JSONdata["Bundesland"] = BundeslandToString(school.Bundesland)
    JSONdata["Einsatzbereich"] = [EinsatzBereichToString(item) for item in school.Einsatzbereich]
    JSONdata["Schwerpunkt"] = EinsatzBereichToString(school.Schwerpunkt)
    return JSONdata

