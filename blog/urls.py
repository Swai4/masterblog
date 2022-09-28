from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from .apiviews import PostList, PostDetail, CreateComment, CreatePost, UserCreate, LoginAPIView
from rest_framework.authtoken import views as tokenviews
from rest_framework_simplejwt.views import TokenRefreshView
from knox import views as knox_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about/', views.about, name='blog-about'),
    path('search/', views.search, name='search'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('postapi/', PostList.as_view(), name="postapi_list"),
    path('postapi/<int:pk>/', PostDetail.as_view(), name="postapi_detail"),
    path('commentapi/', CreateComment.as_view(), name="createcommentapi"),
    path('newpostapi/', CreatePost.as_view(), name="newapipost"),
    path('createuserapi/', UserCreate.as_view(), name="create_new_userapi"),
    path('api/login/', LoginAPIView.as_view(), name='loginviaapi'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logoutviaapi'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api-token/', tokenviews.obtain_auth_token, name='token_generate'),
]