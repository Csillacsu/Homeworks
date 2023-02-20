from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# browser = webdriver.Chrome('S:\oktatási anyagok\chromedriver.exe') # elavult verzió
s = Service(executable_path='S:\oktatási anyagok\chromedriver.exe')
o = Options()
o.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=s, options=o)
browser.get('https://www.selenium.dev/')