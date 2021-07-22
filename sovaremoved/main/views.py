from django.shortcuts import render
# Create your views here.
def index(request):
    data = {
        'title': 'Home page',
        'values': ["Jisoo", "Hello", "123"]
    }
    return render(request, 'main/home.html', data)

def about(request):
    return render(request, 'main/about.html')
