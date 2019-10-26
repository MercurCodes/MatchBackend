from matchingBackend.Enums.Bundeslaender import BUNDESLAND, BundeslandToString
from matchingBackend.Enums.Einsatzbereiche import EinsatzBereichToString
from matchingBackend.Enums.ProgrammSchwerpunkt import SchwerpunkteToString


class Fellow():
    rating = 0
    distance_rating = 0
    comment = ""
    titel = ""
    name = ""
    accountName = ""
    Stadt = ""
    Bundesland = ""
    Land = ""

    Bundesland1Wahl = BUNDESLAND.All
    Bundesland2Wahl = BUNDESLAND.All
    Bundesland3Wahl = BUNDESLAND.All
    einsatzBereiche = []
    schwerpuntke = []

    def deepCopy(self):
        fellow_copy = Fellow()
        fellow_copy.comment = self.comment
        fellow_copy.titel = self.titel
        fellow_copy.name = self.name
        fellow_copy.Stadt = self.Stadt
        fellow_copy.Bundesland = self.Bundesland

        fellow_copy.Bundesland1Wahl = self.Bundesland1Wahl
        fellow_copy.Bundesland2Wahl = self.Bundesland2Wahl
        fellow_copy.Bundesland3Wahl = self.Bundesland3Wahl

        fellow_copy.einsatzBereiche = [item for item in self.einsatzBereiche]
        fellow_copy.schwerpuntke = [item for item in self.schwerpuntke]

        return fellow_copy


def fellowToJSON(fellow):
    fellowJson = {}

    fellowJson["rating"] = fellow.rating
    fellowJson["distance_rating"] = fellow.distance_rating
    fellowJson["comment"] = fellow.comment
    fellowJson["titel"] = fellow.titel
    fellowJson["accountName"] = fellow.accountName
    fellowJson["Stadt"] = fellow.Stadt
    fellowJson["Bundesland"] = BundeslandToString(fellow.Bundesland)
    fellowJson["Land"] = fellow.Land
    fellowJson["Bundesland1Wahl"] = BundeslandToString(fellow.Bundesland1Wahl)
    fellowJson["Bundesland2Wahl"] = BundeslandToString(fellow.Bundesland2Wahl)
    fellowJson["Bundesland3Wahl"] = BundeslandToString(fellow.Bundesland3Wahl)
    fellowJson["einsatzBereiche"] = [EinsatzBereichToString(item) for item in fellow.einsatzBereiche ]
    fellowJson["schwerpuntke"] = [SchwerpunkteToString(item) for item in fellow.schwerpuntke ]

    return fellowJson
