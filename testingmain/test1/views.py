from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
import json
import urllib.request
import random

#Not using dry here for simplicity
# Create your views here.
def home(request):
    apicall("world")
    posts = Post.objects.filter(catalogue="world").order_by('-createdat')[:30]
    if posts:
        random_post = random.choice(Post.objects.filter(catalogue="world").order_by('-createdat'))
    else:
        random_post = None
    #posts = Post.objects.all().order_by('-createdat')
    return render(request,"index.html",{'posts': posts,
                                        'random_post':random_post,})
@login_required
def us(request):
    #apicall("us")
    posts = Post.objects.filter(catalogue="us").order_by('-createdat')[:30]
    if posts:
        random_post = random.choice(Post.objects.filter(catalogue="us").order_by('-createdat'))
    else:
        random_post = None
    return render(request,"index.html",{'posts': posts,
                                        'random_post':random_post,})
@login_required
def tech(request):
    #apicall("technology")
    posts = Post.objects.filter(catalogue="technology").order_by('-createdat')[:30]
    if posts:
        random_post = random.choice(Post.objects.filter(catalogue="technology").order_by('-createdat'))
    else:
        random_post = None
    return render(request,"index.html",{'posts': posts,
                                        'random_post':random_post,})
@login_required
def entertainment(request):
    #apicall("entertainment")
    posts = Post.objects.filter(catalogue="entertainment").order_by('-createdat')[:30]
    if posts:
        random_post = random.choice(Post.objects.filter(catalogue="entertainment").order_by('-createdat'))
    else:
        random_post = None
    return render(request,"index.html",{'posts': posts,
                                        'random_post':random_post,})
@login_required
def science(request):
    #apicall("science")
    posts = Post.objects.filter(catalogue="science").order_by('-createdat')[:30]
    if posts:
        random_post = random.choice(Post.objects.filter(catalogue="science").order_by('-createdat'))
    else:
        random_post = None
    return render(request,"index.html",{'posts': posts,
                                        'random_post':random_post,})
@login_required
def sports(request):
    #apicall("sports")
    posts = Post.objects.filter(catalogue="sports").order_by('-createdat')[:30]
    if posts:
        random_post = random.choice(Post.objects.filter(catalogue="sports").order_by('-createdat'))
    else:
        random_post = None
    return render(request,"index.html",{'posts': posts,
                                        'random_post':random_post,})
'''
#Api Call function
def apicall(category):
    apikey = "153b9076aa700285fa38bb9b8362496a"
    #url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=gh&max=10&apikey={apikey}"
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&max=10&apikey={apikey}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]

        for article in articles:
            # Extract relevant information from the article
            posttitle = article['title']
            postcontext = article['content']
            description = article['description']
            createdat = article['publishedAt']
            urlimg = article['image']
            posturl = article['url']
            print("hio")
            # Check if the article already exists in the database
            if not Post.objects.filter(posttitle=posttitle).exists():
                # Create a new Post object and save it in the database
                news_article = Post(
                    postcontext=postcontext,
                    catalogue=category,
                    description=description,
                    posttitle=posttitle,
                    createdat=createdat,
                    urlimg=urlimg,
                    posturl=posturl,
                )
                
                news_article.save()
'''
# Api Call function
def apicall(category):
    apikey = "153b9076aa700285fa38bb9b8362496a"
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&max=10&apikey={apikey}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))
            articles = data["articles"]

            for article in articles:
                # Extract relevant information from the article
                posttitle = article['title']
                postcontext = article['content']
                description = article['description']
                createdat = article['publishedAt']
                urlimg = article['image']
                posturl = article['url']
                print("hio")
                # Check if the article already exists in the database
                if not Post.objects.filter(posttitle=posttitle).exists():
                    # Create a new Post object and save it in the database
                    news_article = Post(
                        postcontext=postcontext,
                        catalogue=category,
                        description=description,
                        posttitle=posttitle,
                        createdat=createdat,
                        urlimg=urlimg,
                        posturl=posturl,
                    )
                    news_article.save()
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print("Received 403 Forbidden error. Skipping API call for category:", category)
        else:
            print("HTTPError occurred with code:", e.code)
    except urllib.error.URLError as e:
        print("URLError occurred:", e)
    except json.JSONDecodeError as e:
        print("JSONDecodeError occurred:", e)
    except Exception as e:
        print("An error occurred:", e)