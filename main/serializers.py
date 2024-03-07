from rest_framework import serializers

from .models import Subject

from Authentication.serializer import UserSerializer


class SubjectSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()

    def get_student(self, subject):
        serializer = UserSerializer(subject.student)
        return serializer.data

    class Meta:
        model = Subject
        fields = "__all__"
