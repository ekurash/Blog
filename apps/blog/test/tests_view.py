from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory

from apps.blog.models import Post
from apps.blog.views import ListPostView


class PostListViewTest(TestCase):

    def test_posts_in_the_context(self):
        client = Client()
        response = client.get('/blog/')
        self.assertEquals(list(response.context['object_list']), [])

        Post.objects.create(title='Test title', content='Lorem ipsum')
        response = client.get('/blog/')
        self.assertEquals(response.context['object_list'].count(), 1)

    def test_contacts_in_the_context_request_factory(self):
        factory = RequestFactory()
        request = factory.get('/blog/')
        response = ListPostView.as_view()(request)
        self.assertEquals(list(response.context_data['object_list']), [])

        Post.objects.create(title='Test title', content='Lorem ipsum')
        response = ListPostView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
