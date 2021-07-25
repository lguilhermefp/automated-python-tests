from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://seleniumhq.org/")

content_by_id = driver.find_element_by_id("q")
print("my id element is:")
print(content_by_id)

content_by_name = driver.find_element_by_name("q")
print("my name element is:")
print(content_by_name)

content_by_xpath = driver.find_element_by_xpath("//div[@id='mainContent']/h2[1]")
print("my xpath element is:")
print(content_by_xpath)

content_by_class = driver.find_element_by_class_name('selenium-sponsors')
print("my class element is:")
print(content_by_class)

driver.close()
