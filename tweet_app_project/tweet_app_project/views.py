from django.shortcuts import render


def base_home(request):
    return render(request, 'tweet_app_project/base_home.html')