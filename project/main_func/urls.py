from django.urls import path
from . import views

app_name = 'main_func'
urlpatterns = [
    path('create/', views.CreateSeniorEntryView.as_view(), name='test_create'),
    path('offering/company', views.CompanyMyView.as_view(), name='company_page'),
    #path('offering/company/<int:company_id>/', views.company_page, name='company_page'),  # 新しいパスを追加
]