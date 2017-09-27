# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import resolve
from django.test import TestCase
from .views import index

# # Create your tests here.
# class HomePageTest(TestCase):
#     def test_root_url_resolves_to_home_page_viiew(self):
#         found = resolve('/')
#         self.assertEqual(found.func, index)s