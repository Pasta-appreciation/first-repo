from django.shortcuts import render,redirect
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.template.response import TemplateResponse
from django.template.loader import get_template
from django.contrib.auth import login


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)


class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'



def judge_is_senior(request):
    print(request.user)
    print(request.user.is_senior)

    # UIの観点から、Trueの場合を募集側にしたので、ここで逆転させる
    if request.user.is_senior:
        request.user.is_senior = False
        print(request.user.is_senior)

    else:
        request.user.is_senior = True
        print(request.user.is_senior)

    if request.user.is_senior:

        return redirect('main_func:test_list_senior')
        #return TemplateResponse.__init__(request=request, template=get_template('list_view_senior.html'), context=None, content_type=None, status=None, charset=None, using=None)
    else:
        return render(request, 'list_view_offering.html')
        #return TemplateResponse.__init__(request=request, template=get_template('list_view_offering.html'), context=None, content_type=None, status=None, charset=None, using=None)

class SeniorHomeView(TemplateView):
    template_name = 'list_view_senior.html'

class OfferingHomeView(TemplateView):
    template_name = 'list_view_offering.html'

def redirect_to_senior_view(request):
    return redirect('main_func:test_list_senior')