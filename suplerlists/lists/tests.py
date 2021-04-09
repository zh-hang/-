from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest


from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')  # 解析url的function
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correst_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

# 用于验证该测试机制是否运行
# class SomkeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)

# Create your tests here.
