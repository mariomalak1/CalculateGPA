from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.views import CustomAuthentication
from .models import Subject
from .serializers import SubjectSerializer
# Create your views here.

@api_view(["GET", "POST"])
def registerSubjects(request):
    token_ = CustomAuthentication.get_token_or_none(request)
    if not token_:
        return Response({"error": "you must authorized"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        subjects = Subject.objects.filter(student_id=token_.user_id).all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            sub = serializer.create_subject(serializer.validated_data)
            return Response(sub, )





@api_view(["GET"])
def getStatistics(request):
    pass

