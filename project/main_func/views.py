from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Senior, Company, Company, Matching

# Create your views here.
class CreateSeniorEntryView(LoginRequiredMixin,CreateView):
    template_name = 'model_test.html'
    model = Senior
    fields = ['name', 'age', 'address','description','']
    success_url = reverse_lazy('main_func:model_test')

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.user = self.request.user
        entry.save()
        return super().form_valid(form)
    
class Company_view(TemplateView):
    template_name = 'mypage_offering.html'