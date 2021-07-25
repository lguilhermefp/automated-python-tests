from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")
username = driver.find_element_by_name('username')
print("my input element is:")
print(username)
driver.close()