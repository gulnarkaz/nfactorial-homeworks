from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.urls import reverse_lazy
from .models import News, Comment
from .forms import NewsForm, CommentForm
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        default_group = Group.objects.get(name='default')
        user.groups.add(default_group)
        return super().form_valid(form)

@login_required
@permission_required('news.add_news', raise_exception=True)
def add_news(request):
    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            new_news = news_form.save(commit=False)
            new_news.author = request.user  # Связываем новость с автором
            new_news.save()
            return redirect(reverse('news:news_detail', args=[new_news.pk]))
    else:
        news_form = NewsForm()
    return render(request, 'news/add_news.html', {'news_form': news_form})

class NewsUpdateView(View):
    template_name = 'news/edit_news.html'
    form_class = NewsForm

    @method_decorator(login_required)
    @method_decorator(permission_required('news.change_news', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        news = self.get_object()
        if news.author != request.user and not request.user.has_perm('news.change_news'):
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(News, pk=self.kwargs['pk'])

    def get(self, request, pk):
        news = self.get_object()
        form = self.form_class(instance=news)
        return render(request, self.template_name, {'form': form, 'news': news})

    def post(self, request, pk):
        news = self.get_object()
        form = self.form_class(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:news_detail', args=[news.pk]))
        return render(request, self.template_name, {'form': form, 'news': news, 'errors': form.errors})

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})

@login_required
def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comments.all().order_by('-created_at')
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.author = request.user
            new_comment.created_at = timezone.now()
            new_comment.save()
            return redirect(reverse('news:news_detail', args=[pk]))

    return render(request, 'news/news_detail.html', {'news': news, 'comments': comments, 'comment_form': comment_form})

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

class DeleteNewsView(DeleteView):
    model = News
    template_name = 'news/delete_confirm.html'
    success_url = reverse_lazy('news:news_list')

    def test_func(self):
        news = self.get_object()
        return self.request.user == news.author or self.request.user.has_perm('news.delete_news')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'news/comment_delete_confirm.html'

    def get_success_url(self):
        return reverse_lazy('news:news_detail', kwargs={'pk': self.object.news.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.has_perm('news.delete_comment')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)