from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")
login_form = driver.find_element_by_id('loginForm')
print("my login form element is:")
print(login_form)
driver.close()