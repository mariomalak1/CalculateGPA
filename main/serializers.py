from rest_framework import serializers

from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    # student = serializers.SerializerMethodField()

    # def get_student(self, data):
    #     return "mario"

    # def create_subject(self, data_):
    #     self.validated_data["student"] = data_.get("student")
    #     return self.save()

    class Meta:
        model = Subject
        fields = "__all__"
