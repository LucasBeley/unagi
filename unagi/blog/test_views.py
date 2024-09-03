from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Post


class IndexViewTest(TestCase):
    def setUp(self):
        self.url = reverse("blog:index")
        self.post1 = Post.objects.create(
            title="Post 1", content="Content 1", posted_at=timezone.now()
        )
        self.post2 = Post.objects.create(
            title="Post 2", content="Content 2", posted_at=timezone.now()
        )
        self.hidden_post = Post.objects.create(
            title="Hidden Post",
            content="Hidden Content",
            posted_at=timezone.now(),
            hidden_at=timezone.now(),
        )

    def test_view_returns_200_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "blog/index.html")

    def test_view_returns_only_visible_posts(self):
        response = self.client.get(self.url)
        posts = response.context["object_list"]
        self.assertIn(self.post1, posts)
        self.assertIn(self.post2, posts)
        self.assertNotIn(self.hidden_post, posts)


class PostViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post", content="Test Content", posted_at=timezone.now()
        )
        self.url = reverse("blog:post", kwargs={"pk": self.post.pk})

    def test_view_returns_200_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "blog/post.html")

    def test_view_displays_correct_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context["object"], self.post)