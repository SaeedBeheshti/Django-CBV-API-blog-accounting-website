from django.test import TestCase
from django.urls import reverse, resolve
from .views import Indexview

class Testurl(TestCase):
    def test_blog_index_url_resolve(self):
        url = reverse('blog:cbv.test')
        self.assertEqual(resolve(url).func.view_class, Indexview)
