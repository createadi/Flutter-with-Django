from .models import Demo
from .serializers import DemoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def DemoList(request):

  if(request.method=='GET'):
    queryset = Demo.objects.first()
    serializer_class = DemoSerializer(queryset, many=False)
    return Response (serializer_class.data)
