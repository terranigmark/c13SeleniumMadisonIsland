from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

base_url = 'https://madison-island.com/'
driver = webdriver.Chrome()

driver.get(base_url)
assert base_url in driver.current_url, 'No estas en Madison Island'
sections = driver.find_elements(By.CLASS_NAME, 'collection-grid-item')
sections[0].click()
assert 'women' in driver.current_url, 'No estas en la seccion women'


sleep(2)
driver.quit()