# posts > views.py
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .models import Post
from .serializers import *

class PostAPIView(APIView):
    def post(self, request):
        serializer = PostBaseSerializer(data = request.data)
        if serializer.is_valid():
            if serializer.validated_data['bad_post'] == True:
                return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response({"message": "post success"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostAPIView2(APIView):
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            print(serializer.validated_data)
            
            if serializer.initial_data['bad_post'] == True:
                return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                print(serializer.data)
                return Response({"message": "post success"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        posts = Post.objects.all()
        serializer = GETallSerializer(posts, many=True)
        return Response(serializer.data)    



# PostAPI_FBV 추가
@api_view(['POST'])
def PostAPI_FBV(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.initial_data['bad_post'] == True:
            return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({"message": "post success"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListCreateMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.initial_data['bad_post'] == True:
            return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request)
    
class PostListCreateGeneric(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.initial_data['bad_post'] == True:
            return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request)
    
class PostListCreateGeneric(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.initial_data['bad_post'] == True:
            return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request)
    
    
class CommentAPIView(APIView):

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)