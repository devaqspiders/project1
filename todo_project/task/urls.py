from django.urls import path
from task import views

urlpatterns = [
    path('api/v1/task/',views.TaskView.as_view()),
]