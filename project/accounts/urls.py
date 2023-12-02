from django.urls import path
from .views import SignUpView, judge_is_senior, SignUpSuccessView,SeniorHomeView, OfferingHomeView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup_success/', SignUpSuccessView.as_view(), name='signup_success'),

    path('login_success/', judge_is_senior, name='login_success'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),

    path('senior/', SeniorHomeView.as_view(), name='senior'),
    path('offering/', OfferingHomeView.as_view(), name='offering'),
]


