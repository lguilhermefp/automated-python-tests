from selenium import webdriver;
from selenium.webdriver import ActionChains;
from selenium.webdriver.support.ui import Select;
from selenium.webdriver.common.keys import Keys;
import time;

driver = webdriver.Chrome();
driver.get('https://wiki.python.org/moin/FrontPage');

search = driver.find_element_by_id("searchinput");
search.clear();
search.send_keys("Beginner");
search.send_keys(Keys.RETURN);
time.sleep(4);

select = Select(driver.find_element_by_xpath("//select[@name='action']"));
select.select_by_visible_text("Raw Text");
time.sleep(4);

driver.close();
