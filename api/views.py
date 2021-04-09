from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer, PostSerializer
from .models import Task, Post


# 新規でユーザーを作成するためのview
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


# ブログの投稿データの一覧を取得するためのview
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


# 特定の投稿のidに基づいて、一つのブログのデータを取得するためのview
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


# タスクの一覧を取得するview
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


# 特定のidに基づいて、特定のタスクを取得するview
class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


# タスクの新規作成、更新、削除をするためのview
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
