from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import scrape

GOOGLE_FORM_API = 'https://forms.gle/DxHVR7nJXae1qb8D7'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome()

'''
    Filling the form by creating new entries for each 
    address, housing link and renting prices
'''
for n in range(len(scrape.list_links)):
    driver.get(GOOGLE_FORM_API)
    driver.maximize_window()

    time.sleep(2)
    # ---> Filling address field
    address_field = driver.find_element(By.CLASS_NAME, 'zHQkBf')
    address_field.send_keys(scrape.list_add[n])

    time.sleep(1)
    # ---> Filling price field
    price_field = driver.find_element(by=By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')
    price_field.send_keys(scrape.list_prices[n])

    time.sleep(1)
    # ---> Filling links field
    link_field = driver.find_element(by=By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                           '1]/div/div[1]/input')
    link_field.send_keys(scrape.list_links[n])

    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

driver.quit()