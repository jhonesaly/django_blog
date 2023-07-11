from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm
from .views import home, post, addcomment

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_post_url_resolves(self):
        url = reverse('post', args=[1])
        self.assertEqual(resolve(url).func, post)

    def test_addcomment_url_resolves(self):
        url = reverse('addcomment', args=[1])
        self.assertEqual(resolve(url).func, addcomment)


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', brief='Test Brief', content='Test Content', author=self.user)

    def test_post_str_method(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_comment_str_method(self):
        comment = Comment.objects.create(post=self.post, name='Test Name', comment='Test Comment')
        self.assertEqual(str(comment), 'Test Name')


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', brief='Test Brief', content='Test Content', author=self.user)
        self.comment_form_data = {
            'name': 'Test Name',
            'comment': 'Test Comment',
        }

        print("Author:", self.user)
        print("Post:", self.post)


    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_view(self):
        response = self.client.get(reverse('post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')

    def test_addcomment_view(self):
        response = self.client.post(reverse('addcomment', args=[self.post.id]), data=self.comment_form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/posts/{self.post.id}/')

        comment = Comment.objects.last()
        self.assertEqual(comment.name, 'Test Name')
        self.assertEqual(comment.comment, 'Test Comment')
        self.assertEqual(comment.post, self.post)
