from django.shortcuts import render
 
def index_template(request):
    return render(request, 'index.html')

def model_test(request):
    return render(request, 'model_test.html')

