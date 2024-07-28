from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm

# Create your views here.
def home(request):
    return render(request, 'tweet_app/home.html')


def tweet_display(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_app/tweet_display.html', {'tweets':tweets})

def tweet_create(request):
    if request.method == 'POST':   # checking if the user request is POST
        form = TweetForm(request.POST, request.FILES)  # creating Form with method POST and will be able to access files
        if form.is_valid():
            tweet = form.save(commit=False) # creating a tweet and saving it partially
            tweet.user = request.user # adding a user to the created tweet
            tweet.save() # saving the tweet into the db
            return redirect('tweet_display') # after successful creation display the tweet_display page
    else:
        form = TweetForm() # the default form, if it is not a POST method
    return render(request, 'tweet_app/tweet_create.html', {'form':form}) # rendering the form 


def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user) # retriving the selected tweet for thr edit
    if request.method == 'POST':   # checking if the user request is POST
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_display')
    else: 
        form = TweetForm(instance=tweet) # instance is added as we will give pre-filled form to the user of a specific tweet.
    return render(request, 'tweet_app/tweet_create.html', {'form':form})   


def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_display')
    return render(request, 'tweet_app/delete_confirmation.html', {'tweet':tweet})