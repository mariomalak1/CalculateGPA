from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login as django_login
from .models import Student
# from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["username", "password", "last_name", "first_name", "email"]

    def validate_username(self, username):
        user = Student.objects.filter(username=username).first()
        if user:
            raise serializers.ValidationError("this username is already taken")
        return username


    def create_user(self):
        user_ = self.save()
        user_.set_password(self.data.get("password"))
        user_.save()
        return user_

class StudnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["username", "Gpa"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)

    def validate(self, data):
        user = Student.objects.filter(username=data.get("username")).first()
        if not user:
            raise serializers.ValidationError("Username Not Found")
        return data

    def create_token(self, data, request):
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if not user:
            return {"error": "password not valid"}
        django_login(request, user=user)
        token = Token.objects.filter(user=user).first()
        if not token:
            token = Token.objects.create(user=user)
        return {"token": str(token)}
