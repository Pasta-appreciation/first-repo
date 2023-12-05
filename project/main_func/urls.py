from django.urls import path
from . import views

app_name = 'main_func'
urlpatterns = [
    path('create/', views.CreateSeniorEntryView.as_view(), name='test_create'),
]