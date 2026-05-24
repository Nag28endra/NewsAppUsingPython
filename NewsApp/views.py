from django.conf import settings
from django.shortcuts import render
from newsapi import NewsApiClient


def get_newsapi_client():
    return NewsApiClient(api_key=settings.NEWSAPI_KEY)


def get_articles(source):
    topheadlines = get_newsapi_client().get_top_headlines(sources=source)
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for article in articles:
        news.append(article['title'])
        desc.append(article['description'])
        img.append(article['urlToImage'])
        ur.append(article['url'])

    return zip(news, desc, img, ur)


def render_news_page(request, template_name, source):
    return render(request, template_name, context={"mylist": get_articles(source)})


def index(request):
    return render_news_page(request, 'index.html', 'TechRadar,techcrunch,wired,engadget,the-next-web,the-verge')


def TechRadar(request):
    return render_news_page(request, 'TechRadar.html', 'TechRadar')


def techcrunch(request):
    return render_news_page(request, 'techcrunch.html', 'techcrunch')


def wired(request):
    return render_news_page(request, 'wired.html', 'wired')


def theverge(request):
    return render_news_page(request, 'theverge.html', 'the-verge')


def thenextweb(request):
    return render_news_page(request, 'thenextweb.html', 'the-next-web')


def engadget(request):
    return render_news_page(request, 'engadget.html', 'engadget')
