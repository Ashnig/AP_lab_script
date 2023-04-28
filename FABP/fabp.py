#this will be your third step

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
#import csv


data = pd.read_csv("______", engine='python') #fill the blank with the path of the output_file-2.csv
cds = data["sorted amino acids"]
unique_code = data["Unique code"]
l = []



options = Options()
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(options=options)


i = 1 #random i beginning
k = 0 #current group of tabs' iteration

no_of_tabs = 500 #Here you can change the number of tabs,
#I am using 500 tabs in this code but you can change 


# this code will open n no_of_tabs
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
        # try:
        ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[1]/div[1]/div[5]')
        if ele.get_attribute('innerHTML').find('FATTY ACID BINDING PROTEIN HOMOLOG') != -1:
            l.append(unique_code[j+k+1])
            print(type(ele))
            print(ele.get_attribute('innerHTML'))

        else:
            l.append("")
            print(l)
            # print(unique_code)
            print("\nExcept Block Running")
        print(ele)
        print(l)
        print(unique_code)
    k+=no_of_tabs

    time.sleep(0.5)

print(cds[i])
dict  = {"Output" : l}
new_data = pd.DataFrame(dict)

new_data.to_csv("Results.csv")#this is your final csv file and in this file the required data will be solved


