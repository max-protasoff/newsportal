from django.shortcuts import render
from django.http import HttpResponse
import json
import itertools
from django.shortcuts import redirect
import random
from datetime import datetime, time

def index(request):
    return redirect('/news')

def news(request, link):
    with open(r'C:\PycharmProjects\HyperNews Portal\HyperNews Portal\task\news.json', 'r') as jfile:
        jarr = json.load(jfile)
        for article in jarr:
            if article["link"] == int(link):
                data = article

    return render(request, "news/base.html", {"data": data})

def news_main(request):
    if not request.GET.get("q"):
        with open(r'C:\PycharmProjects\HyperNews Portal\HyperNews Portal\task\news.json', 'r') as jfile:
            jarr = json.load(jfile)

        #jarr.sort(key=lambda x: datetime.strptime(x['created'], "%Y-%m-%d %H:%M:%S"), reverse=True)

        #all_news = [{'date': date, 'values': list(news)} for date, news in itertools.groupby(jarr, lambda x: simple_date_fun(x['created']))]

        return render(request, "news/news_main.html", {"articles": jarr})
    else:
        with open(r'C:\PycharmProjects\HyperNews Portal\HyperNews Portal\task\news.json', 'r') as jfile:
            jarr = json.load(jfile)
        word = request.GET.get("q")
        filtered_arr = []
        for art in jarr:
            if word in art['title']:
                filtered_arr.append(art)
        return render(request, "news/news_main.html", {"articles": filtered_arr})

def simple_date_fun(date):
    return datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")

def create(request):
    if request.method == "POST":
        title_art = request.POST.get("title")
        text_art = request.POST.get("text")
        link_art = random.randint(1, 100)
        time_art = datetime.now()
        time_art = time_art.strftime("%Y-%m-%d %H:%M:%S")

        with open(r'C:\PycharmProjects\HyperNews Portal\HyperNews Portal\task\news.json', 'r', encoding="utf-8") as jfile:
            jarr = json.load(jfile)
        news_new = dict()
        news_new["created"] = str(time_art)
        news_new["text"] = text_art
        news_new["title"] = title_art
        news_new["link"] = link_art
        jarr.append(news_new)

        with open (r'C:\PycharmProjects\HyperNews Portal\HyperNews Portal\task\news.json', 'w', encoding="utf-8") as jfile:
            json.dump(jarr, jfile)

        return redirect("/news")


    return render(request, "news/create_article.html")




