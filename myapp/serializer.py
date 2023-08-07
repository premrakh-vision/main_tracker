from rest_framework import serializers
from .models import ScreenShot, User

class ScreenShotSerializer(serializers.ModelSerializer):
    class Meta:
        model=ScreenShot
        fields='__all__'
        

class UserSerializer(serializers.ModelSerializer):
       class Meta:
           model=User
           fields='__all__'