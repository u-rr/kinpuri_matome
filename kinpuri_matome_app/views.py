from django.shortcuts import render
from .models import Article


def articles(request):
    articles = Article.objects.all().order_by("last_update")
    return render(request, "kinpuri_matome_app/articles.html", {"articles": articles})
