from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class EndPointDWH(APIView):
    """..."""
    def get(self, request, format=None):
        table = request.GET['table']
        result = {
            'message' : 'ok',
            'nombre de ligne' : 320,
            'nom de table' : table
            }

        return Response(result)

# def endpoint(request):
#     return render(request, 'api/index.html')
