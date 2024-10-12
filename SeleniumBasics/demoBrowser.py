from functools import reduce

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

service_obj: Service = Service('C:/Users/karth/Downloads/chromedriver-win64/chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service = service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

print(driver.title)
print(driver.current_url)
print(driver.find_element(By.NAME, 'radioButton').is_selected())
driver.find_element(By.XPATH, "//input[@value='radio1']").click()
driver.find_element(By.ID, 'name').send_keys('Elavarasan')

driver.find_element(By.ID, 'alertbtn').click()
alert = Alert(driver)
alert.accept()

print(driver.find_element(By.NAME, 'radioButton').is_selected())
print(driver.find_element(By.ID, 'radio-btn-example').is_displayed())
print(driver.find_element(By.CLASS_NAME,'logoClass').is_displayed())

action = ActionChains(driver)
(action.move_to_element
 (driver.find_element(By.ID, 'mousehover')).
 click(driver.find_element(By.XPATH, "//a[text()='Top']"))).perform()

select = Select(driver.find_element(By.CSS_SELECTOR, '#dropdown-class-example'))
select.select_by_value('option1')
print(select.first_selected_option.text)

(driver.find_element
 (By.XPATH, "//input[@placeholder='Type to Select Countries']").send_keys('India'))
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='India']")))
driver.find_element(By.XPATH, "//*[text()='India']").click()

curr_win: str = driver.current_window_handle
driver.find_element(By.ID, 'openwindow').click()
all_win: list[str] = driver.window_handles
for win in all_win:
    if win!=curr_win:
        driver.switch_to.window(win)
        print(driver.title)
        driver.close()
        driver.switch_to.window(curr_win)

frame = driver.find_element(By.ID, 'courses-iframe')
driver.switch_to.frame(frame)
print(driver.find_element(By.TAG_NAME, 'a').text)
driver.switch_to.default_content()

scroll_table = driver.find_element(By.XPATH, "//legend[text()='Web Table Fixed header']")
driver.execute_script('arguments[0].scrollIntoView(true);', scroll_table)
driver.get_screenshot_as_file('screen.png')

# scroll_bar = driver.find_element(By.CLASS_NAME, 'tableFixHead')
# driver.execute_script('arguments[0].scrollIntoView(true);', scroll_bar)

buttons: list[WebElement] = driver.find_elements(By.CSS_SELECTOR, '.btn-primary')
print(len(buttons))
legends: list[WebElement] = driver.find_elements(By.TAG_NAME, 'legend')
print(list(map(lambda x:x.text, legends)))
assert len(buttons)==5
prices = driver.find_elements(By.XPATH, "//table[@id='product' and @name='courses']//tr//td[3]")
sumVal: int = reduce(lambda x,y: int(x)+int(y),
                     [int(price.text.strip()) for price in prices])
print(sumVal)
linkElem: WebElement = driver.find_element(By.LINK_TEXT,
                               'Free Access to InterviewQues/ResumeAssistance/Material')
print(linkElem.get_attribute('class'))
driver.close()