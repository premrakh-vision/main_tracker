from rest_framework import serializers
from .models import ScreenShot, User , EventOff
from datetime import datetime
class ScreenShotSerializer(serializers.ModelSerializer):
    class Meta:
        model=ScreenShot
        fields='__all__'
        

class UserSerializer(serializers.ModelSerializer):
       class Meta:
           model=User
           fields='__all__'
           
           
class EventOffSerializer(serializers.ModelSerializer):
    break_time=serializers.SerializerMethodField()
    class Meta:
        model=EventOff
        fields=['user','pre_off_time','post_off_time','break_time']

    def get_break_time(self,obj):
        start_time = datetime.strptime(str(obj.pre_off_time).split('.')[0].split('+')[0],"%Y-%m-%d %H:%M:%S") 
        end_time = datetime.strptime(str(obj.post_off_time).split('.')[0].split('+')[0],"%Y-%m-%d %H:%M:%S") 
        break_time = end_time - start_time
        seconds = break_time.seconds
        minute= break_time.total_seconds() // 60 
        hour= minute //60
        return f"{hour}hr:{minute}min:{seconds}sec"

       
class EventOffCreateSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    class Meta:
        model=EventOff
        fields=['user','pre_off_time','post_off_time']
              
    def create(self, validated_data):
        user_obj=User.objects.get(host=validated_data['user'])
        validated_data['user']=user_obj
        event_obj=EventOff.objects.create(**validated_data)
        return event_obj
        