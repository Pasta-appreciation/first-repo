from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Senior, Company, Job, Matching

# Create your views here.
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
    success_url = reverse_lazy('main_func:test_create')


    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.senior_id = self.request.user
        entry.save()
        return super().form_valid(form)
    

class CreateCompanyEntryView(LoginRequiredMixin,CreateView):
    template_name = 'model_create.html'
    model = Company
    fields = ['name', 'address', 'industry', 'homepage_url', 'description']
    success_url = reverse_lazy('main_func:test_create')

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
    success_url = reverse_lazy('main_func:test_create')


    def form_valid(self, form):
        entry = form.save(commit=False)
        test = self.request.user
        entry.company = search_company(self.request.user)
        entry.save()
        return super().form_valid(form)
    
class Error(TemplateView):
    template_name = 'error.html'

def judge_list_view(request):
    if request.user.is_senior: 
        # return CreateCompanyEntryView.as_view()
        return redirect('main_func:test_list_company')
    else:
        # return CreateSeniorEntryView.as_view()
        return redirect('main_func:test_list_senior')


class ListCompanyView(LoginRequiredMixin,ListView):
    template_name = 'model_list.html'
    print("test")
    model = Senior

class ListSeniorView(LoginRequiredMixin,ListView):
    template_name = 'model_list.html'
    print("test")
    model = Job
