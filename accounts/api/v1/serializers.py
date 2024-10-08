from django.contrib.auth.models import User
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']