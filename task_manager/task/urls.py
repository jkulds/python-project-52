from django.urls import path

from task_manager.task.views import TaskModelListView, TaskModelDetailView, \
    TaskModelCreateView, TaskModelUpdateView, TaskModelDeleteView

urlpatterns = [
    path('', TaskModelListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskModelDetailView.as_view(), name='task_detail'),
    path('create/', TaskModelCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskModelUpdateView.as_view(),
         name='task_update'),
    path('<int:pk>/delete/', TaskModelDeleteView.as_view(),
         name='task_delete'),
]