from django.urls import path
from . import views

app_name = 'main_func'
urlpatterns = [
    path('create/', views.CreateSeniorEntryView.as_view(), name='test_create'),
    path('test_list_senior/', views.JobListView.as_view(), name='test_list_senior'),
]