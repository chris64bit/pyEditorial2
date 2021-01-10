from content.views import Index
from content.models import BlogCategory, VideocastCategory, PodcastCategory, Blog
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.templatetags.static import static
from django.test import TestCase
import environ
import os


class BlogCategoryModelTest(TestCase):
    def test_saving_and_retrieving_BlogCategory(self):
        first_category = BlogCategory()
        first_category.title = 'Category1'
        first_category.save()
        second_category = BlogCategory()
        second_category.title = 'Category2'
        second_category.save()

        saved_category = BlogCategory.objects.all()
        self.assertEqual(saved_category.count(), 2)
        first_saved_category = saved_category[0]
        second_saved_category = saved_category[1]
        self.assertEqual(first_saved_category.title, 'Category1')
        self.assertEqual(second_saved_category.title, 'Category2')

class VideocastCategoryModelTest(TestCase):
    def test_saving_and_retrieving_VideocastCategory(self):
        first_videocast_category = VideocastCategory()
        first_videocast_category.title = 'VideoCastCategory1'
        first_videocast_category.save()
        second_videocast_category = VideocastCategory()
        second_videocast_category.title = 'VideoCastCategory2'
        second_videocast_category.save()

        saved_videocast_category = VideocastCategory.objects.all()
        self.assertEqual(saved_videocast_category.count(), 2)
        first_saved_videocast_category = saved_videocast_category[0]
        second_saved_videocast_category = saved_videocast_category[1]
        self.assertEqual(first_saved_videocast_category.title, 'VideoCastCategory1')
        self.assertEqual(second_saved_videocast_category.title, 'VideoCastCategory2')

class PodcastCategoryModelTest(TestCase):
    def test_saving_and_retrieving_PodcastCategory(self):
        first_podcast_category = PodcastCategory()
        first_podcast_category.title = 'PodCastCategory1'
        first_podcast_category.save()
        second_podcast_category = PodcastCategory()
        second_podcast_category.title = 'PodCastCategory2'
        second_podcast_category.save()

        saved_podcast_category = PodcastCategory.objects.all()
        self.assertEqual(saved_podcast_category.count(), 2)
        first_saved_podcast_category = saved_podcast_category[0]
        second_saved_podcast_category = saved_podcast_category[1]
        self.assertEqual(first_saved_podcast_category.title, 'PodCastCategory1')
        self.assertEqual(second_saved_podcast_category.title, 'PodCastCategory2')
