from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# --------------------------------
# Step0: Initial Webdriver Chrome (keep browser opening after code running completely)
ser = Service(r""C:\Users\Ba Truong Huu\Downloads\Compressed\chromedriver.exe"")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser,options=chrome_option)

# --------------------------------
# Load HTML selenium, fill input and search
page = 'https://s.cafef.vn/lich-su-kien.chn'
driver.get(page)
#
# search_input = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div/div[1]/div/input[2]')
# search_button = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div/div[2]/button[1]')
#
# search_input.send_keys('') #fill input
# search_button.click() #click Search

# # --------------------------------
# # wait table and get html
# table_location = (By.XPATH,'//*[@id="gridGiaThuoc"]/div[2]/table') #get table location
# table = WebDriverWait(driver,10).until(EC.visibility_of_element_located(table_location)) #wait 10s for element table visible
#
# table_html = table.get_attribute('outerHTML')
# soup = BeautifulSoup(table_html)

# --------------------------------
# print table
# rows = soup.find_all('tr')
# for row in rows:
#     cells = row.find_all('td')
#     for cell in cells:
#         print(cell.text)

# --------------------------------


all_data = []
page_number = 1
# Loop through the pages
while True:
    # Locate the table element
    table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//table')))

    # Extract the data from the table using Pandas
    table_html = table.get_attribute('outerHTML')
    df = pd.read_html(table_html)[0]  # Assuming the first table on the page is the one you want
    all_data.append(df)

    # Check if there is a next page button
    next_page_button = driver.find_elements(By.XPATH,f'// *[ @ id = "ContentPlaceHolder1_LichSuKien2_rptPage_btnpage_"{page_number+1}""]')
    if not next_page_button:
        break
    # Click the next page button
    next_page_button[0].click()

    # Increment the page number
    page_number += 1

    # Click the next page button
    next_page_button[0].click()

# Combine the data from all pages into a single DataFrame
combined_data = pd.concat(all_data, ignore_index=True)
