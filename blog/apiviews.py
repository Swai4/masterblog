from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer, UsererSerializer
from django.contrib.auth import authenticate
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import render, redirect
from threading import Timer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CreateComment(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)

class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = (permissions.AllowAny,)
    serializer_class = UsererSerializer

    def redirect_to(self, request):
        return redirect('/postapi')        

    def post(self, request):
        #serializer = AuthTokenSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #user = serializer.validated_data['username']
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        #password = serializer.validated_data['password']
        
        if user:
            try:
                token = Token.objects.get(user_id=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            login(request, user)
            #return Response({"token": user.auth_token.key})
            #t = Timer(10.0, self.redirect_to)
            #t.start()
            return Response({"token": user.auth_token.key})

        
        elif username == '' or password == '':
            return Response({"detail": "Authentication credentials were not provided."})

        else:
            return Response({"error": "Wrong Credentials"})

