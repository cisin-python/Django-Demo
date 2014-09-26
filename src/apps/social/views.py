from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def articles(request):
    """
        Display articles
    """
    articles = Article.objects.all()
    ctx = {
        'articles': articles,
    }
    return render(request, "articles/articles.html", ctx)


def article_create_update(request, article_id=None):
    """
        Article create and update
    """
    if article_id:
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(request.POST or None, instance=article)
        message = "Article editing"
    else:
        form = ArticleForm(request.POST or None)
        message = "Article created"

    if form.is_valid():
        article = form.save(commit=False)
        article.save()
        messages.success(request, message)

        return redirect("social_articles")

    ctx = {
        'form': form,
        'edit': article_id is not None
    }
    return render(request, "articles/article_create.html", ctx)


def article_delete(request, article_id):
    """
        Article delete
    """
    article = get_object_or_404(Article, id=article_id)
    try:
        article.delete()
        messages.info(request, "Article successfully removed")
    except ProtectedError:
        messages.error(request, "Article cannot be removed")

    return redirect("social_articles")


def article_comments(request, article_id):
    "Article related comments display "
    article = get_object_or_404(Article, id=article_id)

    ctx = {
        'article': article,
    }
    return render(request, "articles/show.html", ctx)


def comment_create_update(request, article_id, comment_id=None):
    """
        comment create and update
    """

    if comment_id:
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(request.POST or None, instance=procedure)
        message = "Comment editing"
    else:
        form = CommentForm(request.POST or None)
        message = "Comment created"

    if form.is_valid():
        comment = form.save(commit=False)
        comment.articles = article_id
        comment.save()
        messages.success(request, message)

        return redirect("social_articles")

    ctx = {
        'form': form,
        'edit': comment_id is not None
    }
    return render(request, "comments/comment_create.html", ctx)
