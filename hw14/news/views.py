from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import News, Comment
from .forms import NewsForm, CommentForm 
from django.views import View

class NewsUpdateView(View):
    template_name = 'news/edit_news.html'
    form_class = NewsForm

    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        form = self.form_class(instance=news)
        return render(request, self.template_name, {'form': form, 'news': news})

    def post(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        form = self.form_class(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:news_detail', args=[news.pk]))
        return render(request, self.template_name, {'form': form, 'news': news, 'errors': form.errors})
def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comments.all().order_by('-created_at')
    comment_form = CommentForm()  # Создаем экземпляр формы для комментария

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.created_at = timezone.now()
            new_comment.save()
            return redirect(reverse('news:news_detail', args=[pk]))

    return render(request, 'news/news_detail.html', {'news': news, 'comments': comments, 'comment_form': comment_form})

def add_news(request):
    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            new_news = news_form.save()
            return redirect(reverse('news:news_detail', args=[new_news.pk]))
    else:
        news_form = NewsForm()
    return render(request, 'news/add_news.html', {'news_form': news_form})

def news_detail_102(request):
    news = get_object_or_404(News, pk=102)
    comments = news.comments.all().order_by('-created_at')
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.created_at = timezone.now()
            new_comment.save()
            return redirect(reverse('news:news_detail', args=[102]))

    return render(request, 'news/news_detail.html', {'news': news, 'comments': comments, 'comment_form': comment_form})