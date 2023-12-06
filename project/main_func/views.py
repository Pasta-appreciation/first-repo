from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
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

class JobListView(LoginRequiredMixin,ListView):
    template_name = 'list_view_senior.html'
    model = Job

    def get_queryset(self):
        queryset = super().get_queryset()

        # フォームからのデータを取得
        prefecture = self.request.GET.get('prefecture', '')
        industry = self.request.GET.get('industry', '')
        occupation = self.request.GET.get('occupation', '')
        keyword = self.request.GET.get('keyword', '')

        # フィルタリング条件を設定
        filter_conditions = {}

        if prefecture != '選択なし':
            filter_conditions['prefecture__icontains'] = prefecture

        if industry != '選択なし':
            filter_conditions['industry__icontains'] = industry

        if occupation != '選択なし':
            filter_conditions['occupation__icontains'] = occupation

        if keyword:
            filter_conditions['description__icontains'] = keyword

        # フィルタリングを適用
        if filter_conditions:
            queryset = queryset.filter(**filter_conditions)

        return queryset
