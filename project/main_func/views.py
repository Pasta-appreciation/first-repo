from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Senior, Company, Job, Matching

# Create your views here.
# create############################################################################################################
def judge_create_view(request):
    if request.user.is_senior: 
        # return CreateCompanyEntryView.as_view()
        return redirect('main_func:test_create_company')
    else:
        # return CreateSeniorEntryView.as_view()
        return redirect('main_func:test_error')


class CreateSeniorEntryView(LoginRequiredMixin,CreateView):
    template_name = 'model_create.html'
    model = Senior
    fields = ['name', 'age', 'address','description']
    success_url = reverse_lazy('model_test')


    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.senior_id = self.request.user
        entry.save()
        return super().form_valid(form)
    

class CreateCompanyEntryView(LoginRequiredMixin,CreateView):
    template_name = 'model_create.html'
    model = Company
    fields = ['name', 'address', 'industry', 'homepage_url', 'description']
    success_url = reverse_lazy('model_test')

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.company_id = self.request.user
        entry.save()
        return super().form_valid(form)
    
def search_company(offer_user_id):
    try:
        company = Company.objects.get(company_id=offer_user_id)
        return company
    except Company.DoesNotExist:
        return None

class CreateJobEntryView(LoginRequiredMixin,CreateView):
    template_name = 'model_create.html'
    model = Job
    fields = ['number_of_people', 'description', 'is_public']
    success_url = reverse_lazy('model_test')


    def form_valid(self, form):
        entry = form.save(commit=False)
        test = self.request.user
        entry.company = search_company(self.request.user)
        entry.save()
        return super().form_valid(form)
    
class Error(TemplateView):
    template_name = 'error.html'
############################################################################################################

#show############################################################################################################
def judge_list_view(request):
    if request.user.is_senior: 
        # return CreateCompanyEntryView.as_view()
        return redirect('main_func:test_list_company')
    else:
        # return CreateSeniorEntryView.as_view()
        return redirect('main_func:test_list_senior')

#offering 側の一覧表示。つまり高齢者の一覧表示
class SeniorListView(LoginRequiredMixin,ListView):
    template_name = 'model_list.html'
    print("test")
    model = Senior

#高齢者側の一覧表示。これは案件一覧表示
class JobListView(LoginRequiredMixin,ListView):
    template_name = 'model_list.html'
    print("test")
    model = Job

#会社の一覧表示
class CompanyListView(LoginRequiredMixin,ListView):
    template_name = 'model_company_list.html'
    print("test")
    model = Company

#求人の詳細表示
class DetailJobView(LoginRequiredMixin, DetailView):
    template_name = 'model_detail.html'
    model = Job

#高齢者の詳細表示
class DetailSeniorView(LoginRequiredMixin, DetailView):
    template_name = 'model_detail.html'
    model = Senior

############################################################################################################
#edit
def judge_update_view(request):
    if request.user.is_senior: 
        # return CreateCompanyEntryView.as_view()
        return render(request,'model_update.html',{'pk':request.user.pk})
    else:
        # return CreateSeniorEntryView.as_view()
        return render(request,'model_update.html',{'pk':request.user.pk})
    
def search_senior(request):
    try:
        print(request.user.pk)
        senior = Senior.objects.get(senior_id_id=request.user.pk)
        return render(request, 'model_test.html', {'object':senior})
    except Company.DoesNotExist:
        return None

class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    template_name = 'model_update.html'
    model = Company
    fields = ['name', 'address', 'industry', 'homepage_url', 'description']
    success_url = reverse_lazy('model_test')

class UpdateJobView(LoginRequiredMixin, UpdateView):
    template_name = 'model_update.html'
    model = Job
    fields = ['number_of_people', 'description', 'is_public']
    success_url = reverse_lazy('model_test')

class UpdateSeniorView(LoginRequiredMixin, UpdateView):
    """
    def get_context_data(self):
        context = super().get_context_data()
        context = Senior.objects.get(senior_id_id = self.request.user.pk)
        return context
    """
    template_name = 'model_update.html'
    model = Senior
    fields = ['name', 'age', 'address','description']
    success_url = reverse_lazy('model_test')
