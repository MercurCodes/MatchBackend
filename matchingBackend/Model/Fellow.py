from matchingBackend.Enums.Bundeslaender import BUNDESLAND, BundeslandToString
from matchingBackend.Enums.Einsatzbereiche import EinsatzBereichToString
from matchingBackend.Enums.ProgrammSchwerpunkt import SchwerpunkteToString


class Fellow():
    rating = 0
    comment = ""
    titel = ""
    accountName = ""
    Stadt = ""
    Bundesland = ""
    Land = ""

    Bundesland1Wahl = BUNDESLAND.All
    Bundesland2Wahl = BUNDESLAND.All
    Bundesland3Wahl = BUNDESLAND.All
    einsatzBereiche = []
    schwerpuntke = []


def fellowToJSON(fellow):
    fellowJson = {}

    fellowJson["rating"] = fellow.rating
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
