from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.views import CustomAuthentication
from .models import Subject
from .serializers import SubjectSerializer
# Create your views here.


# get all subjects with same name pattern
def getAllRegisterSubjects(request):
    pass


@api_view(["GET"])
def getAllRegisterSubjects(request):
    token_ = CustomAuthentication.get_token_or_none(request)
    if not token_:
        return Response({"error": "you must authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
