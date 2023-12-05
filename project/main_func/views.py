from django.shortcuts import render
from django.views.generic import CreateView
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
    
