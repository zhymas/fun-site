from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Article
from .forms import ArticleForm

def home(request):
    return render(request, 'main/home.html')


def news(request):
    news = Article.objects.all()
    return render(request, 'main/news.html', {'news': news})


def create_news(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author_name = request.user
            article.save()
            return redirect('news')
    form = ArticleForm()
    return render(request, 'main/create_news.html', {'form': form})


def detail_article(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'main/detail_news.html', {'article': article})