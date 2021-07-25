from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://selenium.dev/')

content_by_id = driver.find_element_by_id('gsc-iw-id1')
print('my id element is:')
print(content_by_id)

content_by_name = driver.find_element_by_name('submit')
print('my name element is:')
print(content_by_name)

content_by_xpath = driver.find_element_by_xpath("//section[@class='hero homepage']/h1[1]")
print('my xpath element is:')
print(content_by_xpath)

content_by_class = driver.find_element_by_class_name('selenium-backers')
print("my class element is:")
print(content_by_class)

driver.close()
