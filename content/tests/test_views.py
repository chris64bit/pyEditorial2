from content.views import Index
from content.models import BlogCategory, VideocastCategory, PodcastCategory, Blog
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.templatetags.static import static
from django.test import TestCase
import environ
import os


class HomePageViewTest(TestCase):
    def test_homepage_template(self):
        self.user = User.objects.create_user(username='test_user', password=os.environ.get('EXAMPLE_PASSWORD'))
        response = self.client.get(f'/')
        self.assertTemplateUsed(response, 'index.html')

    #def test_displays_all_list_article(self):
        #self.user = User.objects.create_user(username='testuser', password='12345')
        #first_category = BlogCategory()
        #first_category.title = 'Category1'
        #first_category.save()
        #prefix = 'https://' if request.is_secure() else 'http://'
        #image_path= "/static/images/"
        #Blog.objects.create(title='title1', slug='slug1', publish=True, content="content1", )
        #Blog.objects.create(title='title2', slug='slug2', publish=True, content="content2", )
        #response = self.client.get('/')
        #self.assertIn('itemey 1', response.content.decode())
        #self.assertIn('itemey 2', response.content.decode())

    #def test_root_url_resolves_to_home_page_view(self):
    #found = resolve('/')
    #self.assertEqual(found.func, home_page)

class SearchPageViewTest(TestCase):
    def test_search_template(self):
        self.user = User.objects.create_user(username='testuser', password=os.environ.get('EXAMPLE_PASSWORD'))
        response = self.client.get(f'/search/')
        self.assertTemplateUsed(response, 'search.html')

class BlogPageViewTest(TestCase):
    def test_blog_template(self):
        self.user = User.objects.create_user(username='testuser', password=os.environ.get('EXAMPLE_PASSWORD'))
        response = self.client.get(f'/blog/')
        self.assertTemplateUsed(response, 'archive.html')

class videocastPageViewTest(TestCase):
    def test_videocast_template(self):
        self.user = User.objects.create_user(username='testuser', password=os.environ.get('EXAMPLE_PASSWORD'))
        response = self.client.get(f'/videocast/')
        self.assertTemplateUsed(response, 'archive.html')

class podcastPageViewTest(TestCase):
    def test_podcast_template(self):
        self.user = User.objects.create_user(username='testuser', password=os.environ.get('EXAMPLE_PASSWORD'))
        response = self.client.get(f'/podcast/')
        self.assertTemplateUsed(response, 'archive.html')

class faqPageViewTest(TestCase):
    def test_faq_template(self):
        self.user = User.objects.create_user(username='testuser', password=os.environ.get('EXAMPLE_PASSWORD'))
        response = self.client.get(f'/faq/')
        self.assertTemplateUsed(response, 'faq.html')


class BlogCategoryTest(TestCase):
     #def test_can_save_a_category_POST_request(self):
        #self.client.post('/admin/content/blogcategory/add/', data={'title': 'Category1'})
        #BlogCategory.objects.create(title=title)
        #self.assertEqual(BlogCategory.objects.count(), 1)
        #new_category = BlogCategory.objects.first()
        #self.assertEqual(new_category.title, 'Category1')

    def test_redirects_after_POST(self):
        response = self.client.post('/admin/content/blogcategory/add/', data={'title': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/admin/login/?next=/admin/content/blogcategory/add/')
