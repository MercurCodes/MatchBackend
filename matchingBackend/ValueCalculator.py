from django.http import HttpResponse
import json

from matchingBackend.Model.Fellow import fellowToJSON


def calculateValuesRanking():
    response_data = {}
    school = ""
    user_list = getTopMatchesRanking(school)

    response_data['user1'] = fellowToJSON(user_list[1])
    response_data['user2'] = fellowToJSON(user_list[2])
    response_data['user3'] = fellowToJSON(user_list[3])
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def calculateValuesDistance():
    response_data = {}
    school = ""
    user_list = getTopMatchesDistance(school)

    response_data['user1'] = fellowToJSON(user_list[1])
    response_data['user2'] = fellowToJSON(user_list[2])
    response_data['user3'] = fellowToJSON(user_list[3])
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getTopMatchesRanking(school):
    return sortAfterRanking(schoolMatrix[school])

def getTopMatchesDistance(school):
    return sortAfterDistance(schoolMatrix[school])

def sortAfterRanking(listOfFellows):
    return listOfFellows.sort(key= lambda x:x.rating)

def sortAfterDistance(listOfFellows):
    return listOfFellows.sort(key= lambda x:x.distance)