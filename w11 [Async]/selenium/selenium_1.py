'''
geckodriver should be on your system PATH
https://github.com/mozilla/geckodriver/releases
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get('https://ya.ru/')

# get the search textbox
search_field = driver.find_element_by_id('text')
search_field.clear()

# enter search keyword and submit
search_field.send_keys('mipt one')
search_field.submit()


# close the browser window
# driver.quit()