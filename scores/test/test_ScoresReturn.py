import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.conf import settings
from django.urls.exceptions import NoReverseMatch

class test_Score(APITestCase):
    '''
    verify "score" url name exists
    '''
    def test_existScoreRoute(self):
        d = reverse("score")
        self.assertIsNotNone(d)
    
    '''
    verify that the post method is working
    '''
    def test_APIScores(self):
        data = {'scores' :[10,5]}
        d = reverse("score")
        response = self.client.post(f"{settings.TESTHOSTPORT}{d}",data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    '''
    verify result 1
    '''
    def test_APIScoresResult_1(self):
        data = {'scores' :[10,5,20,20,4,5,2,25,1]}
        d = reverse("score")
        response = self.client.post(f"{settings.TESTHOSTPORT}{d}",data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(int(response.data["max"]),2)
        self.assertEqual(int(response.data["min"]),4)

    '''
    verify result 2
    '''
    def test_APIScoresResult_2(self):
        data = {'scores' :[171645, 4199460, 1792941, 7634143, 5126340, 8930592, 3440006, 6437607, 3736481, 3236750, 5410071, 17094, 8636427, 5856681, 4534760, 666362, 511247, 2277874, 4070151, 7072691, 9130059, 8311177, 6651100, 8537755, 3390569, 516039, 93759, 3338879, 8624243, 6066083, 345618, 4511761, 1714620, 3593758, 7118005, 4981262, 1786085, 4050835, 8557577, 9057470, 9879447, 997843, 696642, 2333744, 8548635, 7996240, 5448625, 167471, 4597637, 2964368, 9444031, 8296411, 1670774, 4683653, 5152188, 239202]}
        d = reverse("score")
        response = self.client.post(f"{settings.TESTHOSTPORT}{d}",data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(int(response.data["max"]),5)
        self.assertEqual(int(response.data["min"]),1)

    '''
    verify result when negatives values are provided since it is impossible to have negative punctuation
    these values will be converted to positives
    '''
    def test_APIScoresValidateNegative(self):
        data = {'scores' :[10,-5,20,20,-4,5,2,25,1]}
        d = reverse("score")
        response = self.client.post(f"{settings.TESTHOSTPORT}{d}",data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(int(response.data["max"]),2)
        self.assertEqual(int(response.data["min"]),4)        

    '''
    verify response status 400 when scores parameter is not provided
    '''
    def test_APIScoresParameterNotProvided(self):
        data = {'scoresssss' :[10,-5,20,20,-4,5,2,25,1]}
        d = reverse("score")
        response = self.client.post(f"{settings.TESTHOSTPORT}{d}",data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
       

    '''
    verify when the scores parameter has invalid values
    '''
    def test_APIScoresInvalidList(self):
        data = {'scores' :[10,"five",20,20,"four",5,2,25,1]}
        d = reverse("score")
        response = self.client.post(f"{settings.TESTHOSTPORT}{d}",data,format='json')
        existkey = "error" in response.data
        self.assertEqual(existkey,True)
        self.assertEqual(response.status_code,status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    '''
    verify that get,put and delete methods does not exist
    '''
    def test_APIScoresInvalidMethods(self):
        data = {'scores' :[10,5,20,20,4,5,2,25,1]}
        d = reverse("score")
        responseGet = self.client.get(f"{settings.TESTHOSTPORT}{d}")
        responsePut = self.client.put(f"{settings.TESTHOSTPORT}{d}",data,format='json')
        responseDelete = self.client.delete(f"{settings.TESTHOSTPORT}{d}")

        self.assertEqual(responseGet.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(responsePut.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(responseDelete.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)









