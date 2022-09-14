from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

data = pd.read_csv("C:/Users/ashni/OneDrive/Desktop/py4e/Biox/10-20_mol_wt.csv")
cds = data["sorted amino acids"]
l = []


options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\ashni\OneDrive\Desktop\py4e\Biox\geckodriver.exe', options=options)

LEN = len(cds)
i = 0
while i < LEN:
    for j in range(10):
        driver.get('https://swissmodel.expasy.org/interactive')
        element = driver.find_element_by_id("id_target")
        element.send_keys(cds[i])
        driver.find_element_by_id("validateInputButton").click()
        time.sleep(3)
        driver.find_element_by_id("buildButton").click()

        i += 1
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    time.sleep(240)
    element = driver.find_element_by_css_selector('table.table:nth-child(3) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4)')
    if element.get_attribute('innerHTML').find('FATTY ACID BINDING') != -1:
        l.append(cds[i])
    print(l)
