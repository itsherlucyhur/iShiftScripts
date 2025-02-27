import time
import win32clipboard
import pandas as pd
import pyperclip
import pyautogui

# Importing all element locations from variable.py file
from variables import *

# Selenium imports
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def process_ME5K_data(final_dict, file_name):
    wo_list = []
    wo_pr_dict = {}
    with open(file_name, encoding="utf8") as f:
        for _ in range(10):
            next(f)
        for line in f:
            line = line.split('|')
            if len(line) > 1:
                purchase_requisition = int(line[4].strip())
                work_order_number = int(line[9].strip())
                wo_list.append(work_order_number)
                if work_order_number in wo_pr_dict:
                    wo_pr_dict[work_order_number].append(purchase_requisition)
                else:
                    wo_pr_dict[work_order_number] = [purchase_requisition]
                final_dict[purchase_requisition]['WO#'] = int(work_order_number)
                final_dict[purchase_requisition]['Vendor'] = line[15].strip()
                final_dict[purchase_requisition]['SHIFT GL#'] = int(line[18].strip())
    
    df_wo = pd.DataFrame(wo_list)
    df_wo.to_clipboard(index=False, header=False)

    return final_dict, wo_pr_dict


def transaction_ME5K(driver, wait):
    driver.get(ME5K_site)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.default_content()
    wait.until(EC.presence_of_element_located((By.ID, iframe)))
    my_frame = driver.find_element(By.ID, iframe)
    driver.switch_to.frame(my_frame)
    wait.until(EC.presence_of_element_located((By.XPATH, cost_center)))
    driver.find_element(By.XPATH, cost_center).send_keys('*')
    driver.find_element(By.XPATH, "//html").click()  
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.XPATH, pr_field)))
    driver.find_element(By.XPATH, pr_field).click()
    time.sleep(1)
    
    # Handle the pop-up that asks for permission to paste
    try:
        alert = Alert(driver)
        driver.find_element(By.XPATH, paste_from_clipboard).send_keys(Keys.CONTROL, 'v')  # Added line to allow paste when pop-up window shows
        time.sleep(2)  # Wait for the paste operation to complete
    except:
        print("No alert found, continuing...")
        time.sleep(1)

    # Click the field and paste
    driver.find_element(By.XPATH, paste_from_clipboard).click()
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    driver.find_element(By.XPATH, copy_button_purchase_requisition).send_keys(Keys.F8)
    time.sleep(3)
    driver.find_element(By.XPATH, held_prs_checkbox1).click()
    time.sleep(1)
    driver.find_element(By.XPATH, closed_reqs_checkbox1).click()
    driver.find_element(By.XPATH, execute_button).click()
    time.sleep(5)

    wait.until(EC.presence_of_element_located((By.XPATH, local)))
    driver.find_element(By.XPATH, local).click()
    time.sleep(2)

    driver.find_element(By.XPATH, copy_to_clipboard_button).click()
    driver.find_element(By.XPATH, continue_button).click()
    time.sleep(3)
    
    data_from_clipboard = ""
    win32clipboard.OpenClipboard()
    data_from_clipboard = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data_from_clipboard
