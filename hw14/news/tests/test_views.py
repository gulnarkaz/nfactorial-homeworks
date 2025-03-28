from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from ..models import News, Comment



class NewsViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.news1 = News.objects.create(title="News 1", content="Content 1", created_at=timezone.now() - timezone.timedelta(days=2))
        self.news2 = News.objects.create(title="News 2", content="Content 2", created_at=timezone.now())
        self.comment1_news2 = Comment.objects.create(news=self.news2, content="Comment 1 for News 2", created_at=timezone.now() - timezone.timedelta(hours=1))
        self.comment2_news2 = Comment.objects.create(news=self.news2, content="Comment 2 for News 2", created_at=timezone.now())

    def test_news_list_view_ordered(self):
        response = self.client.get(reverse('news:news_list'))
        self.assertEqual(response.status_code, 200)
        news_list = list(response.context['news']) 
        self.assertEqual(news_list, [self.news2, self.news1])

    def test_news_detail_view_exists(self):
        news_102 = News.objects.create(pk=102, title="News 102", content="Content 102")
        response = self.client.get(reverse('news:news_detail_102'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['news'], news_102)

def test_news_detail_view_comments_ordered(self):
    """Тест проверяет, что страница детализации новости (URL '102/') выводит комментарии в отсортированном порядке по убыванию."""
    news_102 = News.objects.create(pk=102, title="News 102", content="Content 102")
    comment_a = Comment.objects.create(news=news_102, content="Comment A", created_at=timezone.now() - timezone.timedelta(seconds=30))
    comment_b = Comment.objects.create(news=news_102, content="Comment B", created_at=timezone.now())
    response = self.client.get(reverse('news:news_detail_102'))
    self.assertEqual(response.status_code, 200)
    comments_list = list(response.context['comments'])  # Преобразуем queryset в список
    self.assertEqual(comments_list, [comment_b, comment_a])