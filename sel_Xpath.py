from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv


data = pd.read_csv("C:/Users/ashni/OneDrive/Desktop/dump/Archana/10-20_mol_wt_exchange.csv")
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


"""
Testing Code ends~~
"""

# options = Options()
# options.binary_location = r'/usr/lib/chromium/chromium'
# driver = webdriver.Chrome(executable_path=r'/run/media/akn/Data/Codes/tikSeleniumTesting/Archana/geckodriver.exe', options=options)

i = 160 #random i beginning
k = 0 #current group of tabs' iteration
no_of_tabs = 20
# open n no_of_tabs
for j in range(no_of_tabs-1):
    driver.execute_script('''window.open("http://google.com","_blank");''')
    time.sleep(0.5)
while i < len(cds):
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
        if i >= len(cds): break
        driver.switch_to.window(driver.window_handles[j])
        try:
            element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[1]/div[1]/div[5]')
            if element.get_attribute('innerHTML').find('FATTY ACID BINDING PROTEIN HOMOLOG') != -1:
                l.append(unique_code[j+k+1])
                print(l)
                print("found")
            else:
                l.append("")
                print(l)
                # print(unique_code)
                print("\nExcept Block Running")

        except:
            l.append("")
            print(l)
    k+=no_of_tabs

# //*[@id="mdl_left_col_01"]/div[7]/div[1]/text()




    time.sleep(0.5)

print(cds[i])
dict  = {"Output" : l}
new_data = pd.DataFrame(dict)

new_data.to_csv("solution.csv")





#mdl_left_col_01 > div:nth-child(8) > div:nth-child(1) > a:nth-child(1)
#mdl_left_col_01 > div:nth-child(8) > div:nth-child(1)
#table.table:nth-child(4) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4)

# for i in range(len(cds)):
#     for j in range(10):
#
#     driver.get('https://swissmodel.expasy.org/interactive')
#     element = driver.find_element_by_id("id_target")
#     element.send_keys(cds[i])
#     driver.find_element_by_id("validateInputButton").click()
#     time.sleep(3)
#     driver.find_element_by_id("buildButton").click()
#     time.sleep(300)
#     element = driver.find_element_by_css_selector('table.table:nth-child(3) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4)')
#     if element.get_attribute('innerHTML').find('FATTY ACID BINDING PROTEIN') != -1:
#         l.append(cds[i])
#     print(l)
# #TsM_001185100

            # # Try insertion row-wise
            # with file:
            #     write = csv.writer(file)
            #     write.writerows({"Output" : l})

        #     time.sleep(0.5)
        # except:
        #     l.append("")
        #     print(l)
        #     # print(unique_code)
        #     print("\nExcept Block Running")

            # # Try insertion row-wise
            # with file:
            #     write = csv.writer(file)
            #     write.writerows({"Output" : l})