from django.urls import path
from . import views

app_name = 'main_func'
urlpatterns = [
    path('offering/company', views.search_company, name='company_page'),
    # create
    path('test_create/', views.judge_create_view, name='test_create'),
    #path('test_create_senior/', views.CreateSeniorEntryView.as_view(), name='test_create_senior'),
    path('test_create_company/', views.CreateJobEntryView.as_view(), name='test_create_company'),
    path('test_error/', views.Error.as_view(), name='test_error'),
    # read list
    path('test_list/', views.judge_list_view, name='test_list'),
    path('test_list_company/', views.SeniorListView.as_view(), name='test_list_company'),
    path('test_list_senior/', views.JobListView.as_view(), name='test_list_senior'),
    path('test_list_companlist/', views.CompanyListView.as_view(), name='company_list'),
    # read detail
    path('test_list/company/<int:pk>/detail', views.DetailSeniorView.as_view(), name='detail_senior'),
    path('test_list/senior/<int:pk>/detail', views.DetailJobView.as_view(), name='detail_job'),
    path('test_list/company/<int:pk>/mypage/', views.DetailCompanyView.as_view(), name='company_my_page'),
    path('last_page/', views.search_senior_for_2, name='last_page'),
    # update
    path('test_update/', views.judge_update_view, name='test_update'),
    path('test_serach_senior/', views.search_senior, name='test_search_senior'),
    path('serch_company/', views.search_company_for_update, name="search_company_update"),
    path('test_update_company/<int:pk>/', views.UpdateCompanyView.as_view(), name='update_company'),
    path('test_update_senior/<int:pk>/', views.UpdateSeniorView.as_view(), name='update_senior'),
    path('serch_senior/', views.search_seior_for_update, name='search_senior_update'),

    #gpt
    path('test_gpt/', views.display_model_data, name='test_gpt'),
    path('test_run_gpt/', views.run_gpt, name='test_run_gpt'),
    
    #問題起きたら原因ここかも
    path('create/', views.CreateSeniorEntryView.as_view(), name='test_create'),
    #path('offering/company/<uuid:company_uid>/', views.company_page, name='company_page'),  # 新しいパスを追加

]