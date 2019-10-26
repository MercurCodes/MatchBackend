import json
from django.http import HttpResponse

from matchingBackend import getLoadedData, SchoolToJSON
from matchingBackend.Enums.Bundeslaender import BundeslandToString


def getSchoolList():
    loadedData = getLoadedData()
    return list(loadedData['schools'])

def getSchoolJSONPost(request):
    return HttpResponse(json.dumps(getSchoolJSON(request["login"])), content_type="application/json")

def getSchool(schoolId):
    for school in getSchoolList():
        print(school.id + " " + schoolId + " " + str(schoolId is not school.login))
        if schoolId not in school.id :
            continue
        return school


def getSchoolJSON(schoolId):
        school = getSchool(schoolId)
        if school is None:
            return {}
        schoolJSON = {}

        schoolJSON["priority"] = school.Priority
        schoolJSON["id"] = school.id
        schoolJSON["login"] = school.login
        schoolJSON["stadt"] = school.Stadt
        schoolJSON["bundesland"] = BundeslandToString(school.Bundesland)

        return schoolJSON

def getSchoolListJSON(request):
    jsonDump = []
    for school in getSchoolList():
        schoolJSON = {}

        schoolJSON["priority"] = school.Priority
        schoolJSON["id"] = school.id
        schoolJSON["login"] = school.login
        schoolJSON["stadt"] = school.Stadt
        schoolJSON["bundesland"] = BundeslandToString(school.Bundesland)

        jsonDump.append(schoolJSON)

    return HttpResponse(json.dumps({"schools" : jsonDump}), content_type="application/json")


def getSchoolJSONREST(request):
    school_id = json.loads(request.body)['id']
    print(json.loads(request.body)['id'])
    school = getSchool(school_id)
    response_data = SchoolToJSON(school)
    print( response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")
