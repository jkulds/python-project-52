from django.urls import path

from task_manager.user.views import UserListView, UserCreateView, \
    UserUpdateView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update', UserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),
]