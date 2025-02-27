import time
import datetime
import pandas as pd

# Importing all element locations from variable.py file
from variables import *

# Selenium imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

current_date = datetime.datetime.now()
current_date = current_date.strftime("%b %d %Y")
filename='C:\\Users\\U1014080\\OneDrive - Sanofi\\Documents\\src\\iShiftScripts\\Transaction Excel Data\\ME23N\\'  + current_date + '.csv'


def read_cost_tracker(file_path):
    # To read both 2023 and 2024 PR's
    # return pd.read_excel(file_path, index_col=None, sheet_name=['2023', '2024'], na_values=['NA'], usecols="E")
    return pd.read_excel(file_path, index_col=None, sheet_name='2024', na_values=['NA'], usecols="E")

def write_to_excel(data, filename):
    df = pd.DataFrame(data).T
    df = df.applymap(lambda x: x.encode('unicode_escape').decode('utf-8') if isinstance(x, str) else x)
    df.to_excel(excel_writer = filename, index_label="PRs")



def transaction_ME23N(driver, wait, master_dict):
    driver.get(ME23N_site)
    driver.switch_to.window(driver.window_handles[3])
    driver.switch_to.default_content()
    wait.until(EC.element_to_be_clickable((By.ID, iframe)))
    driver.switch_to.frame(driver.find_element(By.ID, iframe))
    # Open Header
    wait.until(EC.element_to_be_clickable((By.XPATH, header)))
    driver.find_element(By.XPATH, header).send_keys(Keys.CONTROL, Keys.F2)
    time.sleep(2)
    # Open status
    wait.until(EC.element_to_be_clickable((By.ID, status)))
    driver.find_element(By.ID, status).click()
    time.sleep(1)
    for key, value in enumerate(master_dict.items()):
        purchase_order = value[1]['PO#']
        if purchase_order != "":
            time.sleep(1)
            try:
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, other_po_button)))
                driver.find_element(By.CSS_SELECTOR, other_po_button).click()
            except Exception as e:
                time.sleep(3)
                driver.find_element(By.CSS_SELECTOR, other_po_button).click()
            
            wait.until(EC.element_to_be_clickable((By.XPATH, po_field)))
            driver.find_element(By.XPATH, po_field).clear()
            driver.find_element(By.XPATH, po_field).send_keys(purchase_order)
            wait.until(EC.element_to_be_clickable((By.XPATH, search)))
            driver.find_element(By.XPATH, search).send_keys(Keys.ENTER)
            time.sleep(4)
            # Ordered Text
            try:
                ordered = driver.find_element(By.XPATH, ordered_text).text
            except Exception as e:
                time.sleep(3)
                ordered = driver.find_element(By.XPATH, ordered_text).text
            ordered = float(str(ordered.replace(",", "")))

            # Delivered Text
            delivered = driver.find_element(By.XPATH, delivered_text).text
            delivered = float(str(delivered.replace(",", "")))

            # Invoiced Text
            wait.until(EC.visibility_of_element_located((By.XPATH, invoiced_text)))
            try:
                invoiced = driver.find_element(By.XPATH, invoiced_text).text
            except Exception as e:
                time.sleep(3)
                invoiced = driver.find_element(By.XPATH, invoiced_text).text
            invoiced = float(str(invoiced.replace(",", "")))

            if ordered == delivered:
                master_dict[purchase_order]['Work Done/Goods Received?'] = 'Yes'
                master_dict[purchase_order]['GR done?'] = 'Yes'
            else:
                master_dict[purchase_order]['Work Done/Goods Received?'] = ''

            # print('PO {}\nOrdered {}\nInvoiced {}'.format(purchase_order, ordered, invoiced))
            if ordered == invoiced:
                value[1]['Invoice Status'] = 'Approved'
            elif  ordered < invoiced < (ordered + ordered*0.05):
                value[1]['Invoice Status'] = 'Approved'
            elif 0.0 < invoiced < ordered :
                value[1]['Invoice Status'] = 'Partial'
            else:
                value[1]['Invoice Status'] = ''

            driver.find_element(By.CSS_SELECTOR, item_detail).send_keys(Keys.CONTROL, Keys.F4)
            # gr_keyword = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/div/form/div/div[5]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[3]/td/div[9]/table/tbody/tr/td/div/div/div/div/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div/table/tbody[1]/tr[1]/td[1]/div/span/span').text
            # if 'WE' in gr_keyword:
            #     gr_date = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/div/form/div/div[5]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[3]/td/div[9]/table/tbody/tr/td/div/div/div/div/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div/table/tbody[1]/tr[1]/td[5]/div/span/span[1]').text
            #     date_list = (gr_date.strip()).split('.')
            #     date = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]))
            #     date = date.strftime("%d-%b-%y")
            #     master_dict[all_pos[i]]['GR Date, if done'] = date

            # driver.find_element(By.XPATH, '//*[@id="M0:46"]').send_keys(Keys.SHIFT, Keys.F3)
            df = pd.DataFrame(value)
            df.to_csv(filename, mode='a', index=False, header=False)

    return master_dict


if __name__ == "__main__":
    # Driver options
    options = webdriver.EdgeOptions()
    options.add_argument("start-maximized")
    options.add_argument("log-level=3")
    options.add_argument("user-data-dir=C:\\Users\\U1014080\\AppData\\Local\\Microsoft\\Edge\\User Data")
    # Create WebDriver object
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(10)
    time.sleep(10)
    # Define wait for explicit waits
    wait = WebDriverWait(driver, 10)

