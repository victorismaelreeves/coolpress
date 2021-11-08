from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from press.models import Category, CoolUser, Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cat = Category.objects.create(slug='random', label='Random News')
        cls.u = User.objects.create(first_name='pepe')
        cls.cu = CoolUser.objects.create(user=cls.u)
        cls.p = Post.objects.create(category=cls.cat, author=cls.cu)

    def test_sample_post(self):
        cnt_posts = Post.objects.count()
        self.assertEqual(cnt_posts, 1)
        self.assertEqual(self.cu.pk, 1)

    def test_post_detail(self):
        client = Client()
        url = reverse('posts-detail', kwargs={'post_id': self.p.pk})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post_obj'], self.p)

    def homework_test1(self):
        client = Client()
        url = reverse('posts-detail', kwargs={'post_id': self.p.pk})
        response = client.get(url)
        categories = Category.objects.all()
        self.assertEqual(response.context['categories'].count(), categories.count())

    def homework_test2(self):
        client = Client()
        unreachable_post_id = Post.objects.all().count() + 1
        url = reverse('posts-detail', kwargs={'post_id': unreachable_post_id})
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
