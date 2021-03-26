from selenium import webdriver

print('asd')
brower = webdriver.Firefox()
brower.get('http://localhost:8000')

assert 'Django' in brower.title