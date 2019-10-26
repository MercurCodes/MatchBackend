from random import randint

from django.http import HttpResponse
import json

from matchingBackend import getLoadedData
from matchingBackend.Enums.Bundeslaender import BUNDESLAND
from matchingBackend.InformationManagement import getSchool
from matchingBackend.Model.Fellow import fellowToJSON

school_matrix = {}

def initCalculation():
    global school_matrix
    loadedData = getLoadedData()
    school_matrix = {}
    school_data = loadedData["schools"]
    fellow_data = loadedData["fellows"]

    for school in school_data:
        sub_list = []

        for fellow in fellow_data:
            if not isFellowInteressting(school, fellow):
                continue
            sub_list.append(school.generateMatchingFellow(fellow))
        school_matrix[school] = sub_list

def isFellowInteressting(school, fellow):
    if fellow.Bundesland1Wahl is school.Bundesland or fellow.Bundesland1Wahl is BUNDESLAND.All:
        fellow.distance_rating = randint(85, 99)
        return True
    elif fellow.Bundesland2Wahl is school.Bundesland or fellow.Bundesland2Wahl is BUNDESLAND.All:
        fellow.distance_rating = randint(65,84)
        return True
    elif fellow.Bundesland3Wahl is school.Bundesland or fellow.Bundesland3Wahl is BUNDESLAND.All:
        fellow.distance_rating = randint(30,64)
        return True
    else:
        return False

def calculateValuesRanking(request):
    response_data = {}
    school_id = json.loads(request.body)['id']
    print(json.loads(request.body)['id'])
    school = getSchool(school_id)
    user_list = getTopMatchesRanking(school)
    print(user_list)
    response_data['user1'] = fellowToJSON(user_list[1])
    response_data['user2'] = fellowToJSON(user_list[2])
    response_data['user3'] = fellowToJSON(user_list[3])
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def calculateValuesDistance(request):
    response_data = {}
    school_id = json.loads(request.body)['id']
    print(json.loads(request.body)['id'])
    school = getSchool(school_id)
    print(school)
    user_list = getTopMatchesDistance(school)

    response_data['user1'] = fellowToJSON(user_list[1])
    response_data['user2'] = fellowToJSON(user_list[2])
    response_data['user3'] = fellowToJSON(user_list[3])
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getTopMatchesRanking(school):
    initCalculation()
    return sortAfterRanking(school_matrix[school])

def getTopMatchesDistance(school):
    initCalculation()
    return sortAfterDistance(school_matrix[school])

def sortAfterRanking(listOfFellows):
    listOfFellows.sort(key= lambda x:x.rating, reverse=True)
    return listOfFellows

def sortAfterDistance(listOfFellows):
    listOfFellows.sort(key= lambda x:x.distance_rating, reverse=True)
    return listOfFellows


if __name__ == '__main__':
    initCalculation()
    print(school_matrix)