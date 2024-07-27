from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tweet_app/home.html')
