from ServiceLayer import util
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import exceptions

class Scores(APIView):
    '''
    http post method that expose the _calculateScore function
    '''
    def post(self, request,format=None):
        try:
            if not "scores" in request.data:
                raise exceptions.ParseError("please provide scores parameter")
                
            scores = [abs(int(i)) for i in request.data.get("scores",[])] 
            max_count, min_count = self._calculateScore(scores)
            return Response({"max":str(max_count), "min":str(min_count)}, status=status.HTTP_200_OK) 
        except Exception as err:
            util.raiseParentExceptionIfApply(err,exceptions.APIException)
            return Response({"error":str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    '''
    return an integer array containing the numbers of times the scores were broken
    '''
    def _calculateScore(self,scores:"List of values ex [1,2,3,4,5]")->"dict with max and min keys":
        tmpmin = tmpmax = scores[0]
        min_count = max_count = 0
        for i in scores[1:]:
            if i > tmpmax:
                max_count += 1
                tmpmax = i
            if i < tmpmin:
                min_count += 1
                tmpmin = i
        return (max_count, min_count)