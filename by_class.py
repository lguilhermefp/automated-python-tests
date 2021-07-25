from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")

content = driver.find_element_by_class_name('content')
print("my class element is:")
print(content)
driver.close()