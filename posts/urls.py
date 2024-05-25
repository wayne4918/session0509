from django.urls import path
from .views import PostAPIView, PostListAPIView, CommentAPIView, PostAPI_FBV, PostListCreateMixin, PostListCreateGeneric

app_name = 'posts'

urlpatterns = [
    path('post/', PostAPIView.as_view(), name='post'),
    path('list/', PostListAPIView.as_view(), name='list'),
    path('comment/', CommentAPIView.as_view(), name='comment'),
    path('post_fbv/', PostAPI_FBV, name='post_fbv'),
    path('post_mixin/', PostListCreateMixin.as_view(), name='post_mixin'),
    path('post_generic/', PostListCreateGeneric.as_view(), name='post_generic'),
]
