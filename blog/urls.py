from django.urls import path
from .views import IndexView, PostDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, DisLikeView, AddCommentView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('post/edit/<int:pk>/', EditPostView.as_view(), name = 'update_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name = 'delete_post'),
    path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
    path("category/<str:cats>/", CategoryView, name = 'category'),
    path("category-list/", CategoryListView, name = 'category_list'),
    path("like/<int:pk>/", LikeView, name = 'like_post'),
    path("dislike/<int:pk>/", DisLikeView, name = 'dislike_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name = 'add_comment'),
]

