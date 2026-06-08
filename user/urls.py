from django.urls import path
from user import views

urlpatterns = [
    path('api/v1/user/',views.UserView.as_view()),
]