from selenium import webdriver
import unittest

# 新的测试类，继承unittest.TestCase
# 以test开头的都是测试方法A


class NewVisitorTest(unittest.TestCase):

    # 用于启动Firefox浏览器
    def setUp(self):
        self.browser = webdriver.Firefox()

    # 用于关闭Firefox浏览器
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")  # 无论如何都会产生错误信息


if __name__ == "__main__":
    unittest.main()
