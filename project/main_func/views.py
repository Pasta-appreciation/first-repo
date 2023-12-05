from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Senior, Company, Job, Matching

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

def search_jobs(request):
    keyword = request.GET.get('keyword', '')
    area = request.GET.get('area', '')
    keyword = request.GET.get('keyword', '')
    area = request.GET.get('area', '')
    results = Job.objects.filter(description__icontains=keyword, prefecture__icontains=area)
    return render(request, 'list_view_senior.html', {'results': results, 'keyword': keyword, 'area': area})