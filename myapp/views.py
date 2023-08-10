from django.shortcuts import render
from .models import ScreenShot, User
from .serializer import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
import datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import OuterRef, Subquery
# Create your views here.

class ScreenShotView(ViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    
    def create(self,request):
        serializer_data=ScreenShotSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({'msg':'done'},status=status.HTTP_200_OK)
        return Response(serializer_data.errors,status=status.HTTP_404_NOT_FOUND)

    def retrieve(self,request,pk):
        try:
            user_obj=User.objects.get(username=pk)
            ss_obj=ScreenShot.objects.filter(host=user_obj.host)
            if len(ss_obj)==0:
                return Response({'msg':'Not Found !!!'}, status=status.HTTP_404_NOT_FOUND)
            serializer_data=ScreenShotSerializer(ss_obj,many=True)
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        except:
            return Response({'msg':'Not Found !!!'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk):
        try:
            if pk.isnumeric():
                ss_obj=ScreenShot.objects.get(id=pk)
                ss_obj.delete()
                return Response({'msg':'ScreenShot Deleted!!'},status=status.HTTP_202_ACCEPTED )
            user_obj=User.objects.get(username=pk)
            ss_obj=ScreenShot.objects.filter(host=user_obj.host)
            ss_obj.delete()
            return Response({'msg':'ScreenShots Deleted!!'},status=status.HTTP_202_ACCEPTED )
        except:
            return Response({'msg':'Not Found !!!'}, status=status.HTTP_404_NOT_FOUND)


class UserView(ViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]   
    def create(self,request):
        serializer_data=UserSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            d1=dict(serializer_data.data)
            # d1['start_time']=d1['start_time'].split('.')[0].replace('T',' ')
            # d1['end_time']=d1['end_time'].split('.')[0].replace('T',' ')
            d1['start_time']=d1['start_time'].split('.')[0].replace('T',' ')
            d1['end_time']=d1['end_time'].split('.')[0].replace('T',' ')
            print('create_data',d1)
            return Response(d1,status=status.HTTP_200_OK)
        return Response(serializer_data.errors)
       

    def list(self,request):
        try:
            user_obj=User.objects.get(host=request.query_params.get('host'))
            serializer_data=UserSerializer(user_obj)
            d1=dict(serializer_data.data)
            # d1['start_time']=d1['start_time'].split('+')[0].split('.')[0].replace('T',' ')
            # d1['end_time']=d1['end_time'].split('+')[0].split('.')[0].replace('T',' ')
            d1['start_time']=d1['start_time'].split('.')[0].replace('T',' ')
            if (str(d1['start_time']).__contains__("+05:30")):
                d1['start_time']=d1['start_time'].replace("+05:30","")
                
            d1['end_time']=d1['end_time'].split('.')[0].replace('T',' ')
            if (str(d1['end_time']).__contains__("+05:30")):
                d1['end_time']=d1['end_time'].replace("+05:30","")
                
            # print("list data",d1)
            
            return Response(d1,status=status.HTTP_200_OK)
        except:
            return Response({'msg':'Not Found !!!'},status=status.HTTP_404_NOT_FOUND)


class EventOffView(ViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def create(self,request):
        
        d1=EventOffCreateSerializer(data=request.data)
        if d1.is_valid():
            d1.save()
            return Response(d1.data,status=status.HTTP_200_OK)
        return Response(d1.errors,status=status.HTTP_400_BAD_REQUEST)
      
    def list(self,request):
        user_obj=EventOff.objects.filter(user__host=request.query_params.get('host'))
        d1=EventOffSerializer(user_obj,many=True)
        return Response(d1.data)
        

def view_screen(request):
    if request.method=='POST':
        name_query= User.objects.filter(username=request.POST['username'].lower())        
        if(len(name_query) != 0):
            if request.POST.get('date'):
                screen_data=ScreenShot.objects.filter(host=name_query[0].host,created_at__date=request.POST['date']).annotate(
            username = Subquery(User.objects.filter(host=OuterRef('host')).values('username')[:1])
        )                                                     
            else:
                screen_data=ScreenShot.objects.filter(host=name_query[0].host).annotate(
            username = Subquery(User.objects.filter(host=OuterRef('host')).values('username')[:1])
        )                                                      
            return render(request,'index.html', {'data':screen_data,"username":name_query[0].username,})
        
        screen_data=ScreenShot.objects.none()
        return render(request,'index.html', {'data':screen_data})
    else: 
        screen_data=ScreenShot.objects.all().annotate(
            username = Subquery(User.objects.filter(host=OuterRef('host')).values('username')[:1])
        )                                      
        return render(request,'index.html', {'data':screen_data})
    

