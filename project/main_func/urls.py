from django.urls import path
from . import views

app_name = 'main_func'
urlpatterns = [
    path('test_create/', views.judge_create_view, name='test_create'),
    #path('test_create_senior/', views.CreateSeniorEntryView.as_view(), name='test_create_senior'),
    path('test_create_company/', views.CreateJobEntryView.as_view(), name='test_create_company'),
    path('test_error/', views.Error.as_view(), name='test_error'),

    path('test_list/', views.judge_list_view, name='test_list'),
    path('test_list_company/', views.ListCompanyView.as_view(), name='test_list_company'),
    path('test_list_senior/', views.ListSeniorView.as_view(), name='test_list_senior'),
]