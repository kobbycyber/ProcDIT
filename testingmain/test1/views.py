from django.shortcuts import render,HttpResponse
from .models import Post
import json
import urllib.request

# Create your views here.
def home(request):
    getgnewsworld()
    posts = Post.objects.all()
    return render(request,"index.html",{'posts': posts})

def getgnewsworld():
    apikey = "153b9076aa700285fa38bb9b8362496a"
    category = "world"
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=gh&max=10&apikey={apikey}"

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