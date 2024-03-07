from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from django.http.response import Http404

from Authentication.views import UserAuthentication
from Authentication.serializer import UserSerializer
from Authentication.models import Student

from .models import Subject
from .serializers import SubjectSerializer

from project.utilis import defualtResponse, getDataFromPaginator


# Create your views here.

class SubjectView(APIView):
    def post(self, request):
        token_ = UserAuthentication.get_token_or_none(request)
        if not token_:
            return Response({"error": "you must authorized"}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data.copy()
        data["student"] = token_.user_id
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            subject = serializer.save()
            serializer = SubjectSerializer(subject)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # get all subjects
    def get(self, request):
        token_ = UserAuthentication.get_token_or_none(request)
        if not token_:
            return Response({"error": "you must authorized"}, status=status.HTTP_401_UNAUTHORIZED)

        subjects = Subject.objects.filter(student_id=token_.user_id).all()
        allData = getDataFromPaginator(request, subjects)
        return defualtResponse(allData, SubjectSerializer)

    # get specific subject
    @staticmethod
    @api_view(["GET"])
    def getSpecificSubject(request, ref):
        token_ = UserAuthentication.get_token_or_none(request)
        if not token_:
            return Response({"error": "you must authorized"}, status=status.HTTP_401_UNAUTHORIZED)

        subject = self.get_object(ref)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, ref):
        try:
            return Subject.objects.get(ref=ref)
        except:
            raise Http404

    def patch(self, request, ref):
        token_ = UserAuthentication.get_token_or_none(request)
        if not token_:
            return Response({"error": "you must authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        subject = self.get_object(ref)
        data = request.data.copy()
        data["student"] = token_.user_id
        print(subject)
        serializer = SubjectSerializer(data=data, instance=subject, partial=True)
        if serializer.is_valid():
            subject = serializer.save()
            serializer = SubjectSerializer(subject)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ref):
        token_ = UserAuthentication.get_token_or_none(request)
        if not token_:
            return Response({"error": "you must authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        subject = self.get_object(ref)
        try:
            subject.delete()
        except:
            return Response({"error":"error while deleting subject"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def getStatistics(request):
    token_ = CustomAuthentication.get_token_or_none(request)
    if not token_:
        return Response({"error": "you must authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    student = Student.objects.get(id=token_.user_id)
    student.calculate_Gpa()
    serializer = StudnetSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def calculateGpa(request):
    token_ = UserAuthentication.get_token_or_none(request)
    if not token_:
        return Response({"error": "you must authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    student = Student.objects.get(id=token_.user_id)
    # calculate gpa and save it
    student.calculate_Gpa()
    serializer = UserSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)