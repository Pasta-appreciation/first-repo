from django.urls import path
from . import views

app_name = 'main_func'
urlpatterns = [
    path('create/', views.CreateSeniorEntryView.as_view(), name='test_create'),
    path('offering/company/company', views.Company_view.as_view(), name='company_page'),  # 新しいパスを追加
]