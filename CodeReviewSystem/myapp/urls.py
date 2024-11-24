from django.urls import path
from myapp.views import start_task,show_start_task

urlpatterns = [
    path('api/task/',start_task),
    path('api/task/<task_id>/',show_start_task),
]