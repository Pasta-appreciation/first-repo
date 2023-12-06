from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
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
    template_name = 'list_view_offering.html'
    model = Senior
    def get_queryset(self):
        queryset = super().get_queryset()
        # フォームからのデータを取得
        keyword = self.request.GET.get('keyword', '')
        age = self.request.GET.get('age', '')
        sex = self.request.GET.get('sex', '')
        area = self.request.GET.get('area', '')
        industry = self.request.GET.get('industry', '')
        occupation = self.request.GET.get('occupation', '')
        # フィルタリング条件を設定
        filter_conditions = {}
        if keyword != '':
            filter_conditions['description__icontains'] = keyword
        if age != '':
            filter_conditions['age__lte'] = age
        if sex != '選択なし':
            filter_conditions['sex__icontains'] = sex
        if area != '選択なし':
            filter_conditions['address__icontains'] = area
        if industry != '選択なし':
            filter_conditions['industry__icontains'] = industry
        if occupation != '選択なし':
            filter_conditions['occupation__icontains'] = occupation


        
        # フィルタリングを適用
        if filter_conditions:
            queryset = queryset.filter(**filter_conditions)
        return queryset
        

#高齢者側の一覧表示。これは案件一覧表示
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
    template_name = 'mypage_senior.html'
    model = Senior

#会社の詳細表示
class DetailCompanyView(LoginRequiredMixin, DetailView):
    template_name = 'mypage_offering.html'
    model = Company

############################################################################################################
#edit
##path.joinすれば良いのよ！！！！！！！！！！！！！！！
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

def search_senior_for_2(request):
    try:
        print(request.user.pk)
        senior = Senior.objects.get(senior_id_id=request.user.pk)
        return render(request, 'mypage_senior.html', {'object':senior})
    except Company.DoesNotExist:
        return None

class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    template_name = 'company_update.html'
    model = Company
    fields = ['name', 'address', 'industry', 'homepage_url', 'description']
    success_url = reverse_lazy('main_func:search_company_update')

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
    template_name = 'senior_update.html'
    model = Senior
    fields = ['name', 'age', 'address','description']
    success_url = reverse_lazy('main_func:search_senior_update')


############################################################################################################

#gpt############################################################################################################
#高齢者への提案機能
def display_model_data(request):
    # モデルのデータを取得
    job_data = Job.objects.all()
    company_data = Company.objects.all()
    print(request.user.pk)
    senior_data = Senior.objects.get(senior_id_id=request.user.pk)

    # テンプレートにデータを渡してレンダリング
    return render(request, 'test_gpt.html', {'job_data': job_data, 'senior_data': senior_data})

from .gpt import embedding, make_recommend
def run_gpt(request):
    job_data = Job.objects.all()
    job_details = []
    for job in job_data:
        details = [
            "##job_id:"+str(job.job_id),
            "##company_id:"+str(job.company.company_id_id),
            "company_description:"+str(job.company.description),
            "prefecture:"+str(job.prefecture),
            "salary:"+str(job.salary),
            "job_description:"+str(job.description),
            # 他のフィールドも同様に追加します
        ]
        job_details.append(' '.join(details))
    all_job_details = '\\'.join(job_details)
    vectorestore = embedding(all_job_details)
    
    senior_data = Senior.objects.get(senior_id_id=request.user.pk)
    senior_details = []
    details = [
            "applicant_name:"+str(senior_data.name),
            "applicant_address:"+str(senior_data.address),
            "applicant_descripton:"+str(senior_data.description),
    ]
    senior_details.append(''.join(details))
    all_senior_details = '\\'.join(senior_details)
    print(all_senior_details)
    res = make_recommend(all_senior_details, vectorestore)
    return render(request, 'test_gpt.html', {'job_data': job_data, 'senior_data': senior_data, 'gpt_res': res})
############################################################################################################


def search_company(request):
    try:
        print(f"request.user.pk:{request.user.pk}")
        company = Company.objects.get(company_id_id=request.user.pk)
        return redirect('main_func:company_my_page',company.pk)
    except Company.DoesNotExist:
        return None
    
def search_company_for_update(request):
    try:
        print(f"request.user.pk:{request.user.pk}")
        company = Company.objects.get(company_id_id=request.user.pk)
        return redirect('main_func:update_company',company.pk)
    except Company.DoesNotExist:
        return None
    
def search_seior_for_update(request):
    try:
        print(f"request.user.pk:{request.user.pk}")
        senior = Senior.objects.get(senior_id_id=request.user.pk)
        return redirect('main_func:update_senior',senior.pk)
    except Senior.DoesNotExist:
        return None

