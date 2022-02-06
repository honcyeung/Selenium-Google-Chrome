from selenium import webdriver

chrome_brower = webdriver.Chrome('./chromedriver')

chrome_brower.maximize_window()
chrome_brower.get('https://www.seleniumeasy.com/selenium-webdriver-tutorials')

# get page title
page_title = 'Webdriver Tutorials for Beginners - Step by Step | Selenium Easy'
assert page_title in chrome_brower.title

# logo = chrome_brower.find_element_by_class_name('site-logo')
# print(logo)

title = chrome_brower.find_element_by_class_name('section-title')
# get inner html elements
print(title.get_attribute('innerHTML'))

# assert 'Selenium Easy' in chrome_brower.page_source

# automate text input
email = chrome_brower.find_element_by_id('mce-EMAIL')
email.clear()
email.send_keys('gooooood')

# automate clicks
button = chrome_brower.find_element_by_id('mc-embedded-subscribe')
button.click()

# user_button = chrome_brower.find_element_by_css_selector('#get-input > .btn')
# print(user_button)

# chrome_brower.close()
# chrome_brower.close()
chrome_brower.quit()
