from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Load driver and wait for page to render before using it
driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeTBkDPkWaf70uurOnSZ9ymTGFQiIPjcfnLbWakVjIcivmh3A/viewform?fbclid=IwAR0aFOmhB0NlyYaL6eV1wa-HPtffPf3ZwNSrZiwMfS3kqoexc_19uF-DNiY")
time.sleep(2)

# First page items
my_form_items = ["Nicholas", "Sturk", "226-700-9529"]
input_fields = driver.find_elements_by_css_selector('input[type="text"]')

# Enter info
for (key, field) in zip(my_form_items, input_fields): 
   time.sleep(0.5)
   field.send_keys(key)

# Next page button
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()

# Say no to all radio buttons
radio_buttons = driver.find_elements_by_css_selector('.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle')
for button in radio_buttons: 
   time.sleep(0.5)
   button.click()

# Submit form
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]').click()

