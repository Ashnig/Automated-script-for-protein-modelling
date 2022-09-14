from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv


data = pd.read_csv("/media/akn/Data/Codes/tikSeleniumTesting/Archana2/Archana/10-20_mol_wt_exchange.csv", engine='python')
cds = data["sorted amino acids"]
unique_code = data["Unique code"]
l = []

"""
Testing Code begins:
"""

from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'normal'
# chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(options=options)
# driver.get('https://google.com')
# driver = webdriver.Chrome(ChromeDriverManager().install())


# # Output file open
# file = open('solution.csv', 'a+', newline ='')



"""
Testing Code ends~~
"""

# options = Options()
# options.binary_location = r'/usr/lib/chromium/chromium'
# driver = webdriver.Chrome(executable_path=r'/run/media/akn/Data/Codes/tikSeleniumTesting/Archana/geckodriver.exe', options=options)

i = 1 #random i beginning
k = 0 #current group of tabs' iteration
no_of_tabs = 15
# open n no_of_tabs
for j in range(no_of_tabs-1):
    driver.execute_script('''window.open("http://google.com","_blank");''')
    time.sleep(0.5)
while i < 20:
    for j in range(no_of_tabs):
        if i >= len(cds): break
        driver.switch_to.window(driver.window_handles[j])
        driver.get('https://swissmodel.expasy.org/interactive')
        element = driver.find_element(By.ID, "id_target")
        element.send_keys(cds[i])
        driver.find_element(By.ID, "validateInputButton").click()
        time.sleep(3)
        driver.find_element(By.ID, "buildButton").click()
        time.sleep(0.5)
        i += 1
    print("Len CDS:", len(cds), "and i at: ", i)
    time.sleep(300)
    for j in range(no_of_tabs):
        desc = []
        if i >= len(cds): break
        driver.switch_to.window(driver.window_handles[j])
        # try:
        element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[1]/div[1]/div[5]/div[1]/div[1]/div/div[7]/div[1]')
        # if element.get_attribute('innerHTML').find('FATTY ACID BINDING PROTEIN HOMOLOG') != -1:
        # l.append(unique_code[j+k+1])
        desc.append(element)
        temp_dict = {"Description":desc}
        desc_data = pd.DataFrame(temp_dict)

        # else:
        #     l.append("")
        #     print(l)
        #     # print(unique_code)
        #     print("\nExcept Block Running")
        # print(element)
        # print(l)
        # print(unique_code)
    k+=no_of_tabs


# //*[@id="mdl_left_col_01"]/div[7]/div[1]/text()
# /html/body/div[2]/div[3]/div/div/div[1]/div[1]/div[5]/div[1]/div[1]/div/div[7]/div[1]
    time.sleep(0.5)

print(cds[i])
dict  = {"Output" : l}
new_data = pd.DataFrame(dict)

new_data.to_csv("solution.csv")
