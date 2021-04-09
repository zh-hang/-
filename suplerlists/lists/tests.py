from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')  # 解析url的function
        self.assertEqual(found.func, home_page)

# 用于验证该测试机制是否运行
# class SomkeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)

# Create your tests here.
