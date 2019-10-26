import xlrd as xlrd

from matchingBackend.Enums.Bundeslaender import StringToBUNDESLAND
from matchingBackend.Enums.Einsatzbereiche import StringToEINSATZBEREICH
from matchingBackend.Enums.ProgrammSchwerpunkt import StringToPROGRAMMSCHWERPUNKT
from matchingBackend.Model.Fellow import Fellow, fellowToJSON
from matchingBackend.Model.School import School, SchoolToJSON

filenameFellows = "C:/Users/Raphael Kunz/Downloads/Fellowliste.xlsx"
filenameSchools = "C:/Users/Raphael Kunz/Downloads/Schulliste.xlsx"

def loadDataFromXLSX():
    fellowBook = xlrd.open_workbook(filenameFellows, encoding_override="utf-8")
    schoolBook = xlrd.open_workbook(filenameSchools, encoding_override="utf-8")

    schoolSheet = schoolBook.sheet_by_index(0)
    fellowSheet = fellowBook.sheet_by_index(0)

    for i in range(1, fellowSheet.nrows):
        fellow = Fellow()

        fellow.titel = fellowSheet.cell(i, 1).value
        fellow.accountName = fellowSheet.cell(i, 2).value
        fellow.Stadt = fellowSheet.cell(i, 3).value
        fellow.Bundesland = StringToBUNDESLAND(fellowSheet.cell(i, 4).value)
        fellow.Land = fellowSheet.cell(i, 5).value
        fellow.Bundesland1Wahl = StringToBUNDESLAND(fellowSheet.cell(i, 6).value)
        fellow.Bundesland2Wahl = StringToBUNDESLAND(fellowSheet.cell(i, 7).value)
        fellow.Bundesland3Wahl = StringToBUNDESLAND(fellowSheet.cell(i, 8).value)

        fellow.schwerpuntke = [StringToPROGRAMMSCHWERPUNKT(item) for item in fellowSheet.cell(i, 10).value.split(';')]
        fellow.einsatzBereiche = [StringToEINSATZBEREICH(item) for item in fellowSheet.cell(i, 9).value.split(';')]

        print(fellowToJSON(fellow))

    for i in range(1,schoolSheet.nrows):
        school = School()

        school.Priority = int(schoolSheet.cell(i, 0).value)
        school.Stadt = schoolSheet.cell(i, 4).value
        school.Bundesland = StringToBUNDESLAND(schoolSheet.cell(i, 5).value)
        school.Einsatzbereich = [StringToEINSATZBEREICH(item) for item in schoolSheet.cell(i, 6).value.split(';')]
        school.Schwerpunkt = [StringToPROGRAMMSCHWERPUNKT(item) for item in schoolSheet.cell(i, 7).value.split(';')]

        print(SchoolToJSON(school))


if __name__ == '__main__':
    loadDataFromXLSX()
