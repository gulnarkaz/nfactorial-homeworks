from django.test import TestCase
from django.utils import timezone
from ..models import News, Comment

class NewsModelTests(TestCase):

    def test_news_has_comments_true(self):
        news = News.objects.create(title="Test News", content="Test Content")
        Comment.objects.create(news=news, content="Test Comment 1")
        Comment.objects.create(news=news, content="Test Comment 2")
        self.assertTrue(news.has_comments())

    def test_news_has_comments_false(self):
        news = News.objects.create(title="Another Test News", content="Another Test Content")
        self.assertFalse(news.has_comments())