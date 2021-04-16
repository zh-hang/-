from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


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

        # 检测page title
        self.assertIn("To-Do", self.browser.title)

        # 检测h1标签中是否有To-Do
        header_text = self.browser.find_element_by_css_selector('h1').text
        self.assertIn('To-Do', header_text)

        # 检测有没有一个输入todo的输入框
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 向输入框中输入Buy peacock feathers
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 检验是否插入
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feather'for row in rows)
        )

        # 无论如何都会产生错误信息
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main()
