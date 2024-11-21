from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)'
            ,'Is similiar to a traditional DJango view'
            ,'Gives you the most control over your application logic'
            , 'Is mapped manuallt to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})