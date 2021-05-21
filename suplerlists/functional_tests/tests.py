from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import unittest
import time

MAX_WAIT=10

# 新的测试类，继承LiveServerTestCase
# 以test开头的都是测试方法A


class NewVisitorTest(LiveServerTestCase):

    # 用于启动Firefox浏览器
    def setUp(self):
        self.browser = webdriver.Firefox()

    # 用于关闭Firefox浏览器
    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self,row_text):
        start_time=time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError,WebDriverException)as e:
                if time.time()-start_time>MAX_WAIT:
                    raise e
                time.sleep

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        # 检测page title
        self.assertIn("To-Do", self.browser.title)

        # 检测h1标签中是否有To-Do
        header_text = self.browser.find_element_by_css_selector('h1').text
        self.assertIn('To-Do', header_text)

        # 检测有没有一个输入todo的输入框
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 向输入框中输入Buy peacock feathers
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        # 检验是否插入
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # 向输入框中输入Use peacock feathers to make a fly
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 检验是否插入     
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 无论如何都会产生错误信息
        self.fail("Finish the test!")
