from django.urls import path

import task_manager.status.views

urlpatterns = [

    path('',
         task_manager.status.views.StatusListView.as_view(),
         name='status_list'),
    path('create/',
         task_manager.status.views.StatusCreateView.as_view(),
         name='status_create'),
    path('<int:pk>/update/',
         task_manager.status.views.StatusUpdateView.as_view(),
         name='status_update'),
    path('<int:pk>/delete/',
         task_manager.status.views.StatusDeleteView.as_view(),
         name='status_delete'),
]