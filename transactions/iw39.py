import time
import win32clipboard
import pyperclip
import pyautogui

# Importing all element locations from variable.py file
from variables import *

# Selenium imports
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


def process_IW39_data(final_dict, wo_pr_dict, file_name):
    with open(file_name, encoding="utf8") as f:
        for _ in range(10):
            next(f)
        for line in f:
            line = line.split('|')
            if len(line) > 1:
                work_order = int(line[1].strip())
                purchase_requisition = wo_pr_dict[work_order]
                for i in purchase_requisition:
                    final_dict[i]['PM Type'] = line[4].strip()
                    final_dict[i]['Building#'] = str(line[9].strip()[4:7])
                    final_dict[i]['Settlement Cost Center'] = line[10].strip()                       
    return final_dict


def transaction_IW39(driver, wait):
    #Query Definition
    driver.get(IW39_site)
    time.sleep(4)
    
    driver.switch_to.window(driver.window_handles[3])
    driver.switch_to.default_content()
    # driver.switch_to.active_element
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.ID, iframe)))
    driver.switch_to.frame(driver.find_element(By.ID, iframe))
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.XPATH, completed_checkbox)))
    time.sleep(1)

    # Click on checkboxes
    driver.find_element(By.XPATH, completed_checkbox).click()
    driver.find_element(By.XPATH, historical_checkbox).click()

    # click on Order 
    driver.find_element(By.XPATH, work_order_field).click()
    time.sleep(3)

    # Click the field and paste
    driver.find_element(By.XPATH, paste_from_clipboard).click()
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)

    driver.find_element(By.XPATH, copy_button_work_order).send_keys(Keys.F8)
    time.sleep(1)
    # Find Start Period and Clear the field 
    start_period_input = driver.find_element(By.CSS_SELECTOR, start_period)
    start_period_input.click()
    start_period_input = driver.find_element(By.CSS_SELECTOR, start_period)
    start_period_input.clear()
    # Find End Period and Clear the field
    end_period_input = driver.find_element(By.CSS_SELECTOR, end_period)
    end_period_input.click()
    end_period_input = driver.find_element(By.CSS_SELECTOR, end_period)
    end_period_input.clear()

    wait.until(EC.element_to_be_clickable((By.XPATH, layout)))
    layout_input = driver.find_element(By.XPATH, layout)
    layout_input.click()
    layout_input.clear()

    # Choose Custom layout for display 
    layout_input.send_keys("/TSCCWO") 
    time.sleep(1)
    driver.find_element(By.XPATH, execute_button).click()   # execute to view data results
    time.sleep(2)
   
    wait.until(EC.element_to_be_clickable((By.ID, menu_dropdown)))
    moredropdown = driver.find_element(By.ID, menu_dropdown)
    moredropdown.click()
    time.sleep(2)
    listdropdown = driver.find_element(By.XPATH, list_select)
    listdropdown.click()
    time.sleep(1)
    driver.find_element(By.XPATH, save_select).click()
    time.sleep(1)
    driver.find_element(By.XPATH, file_select).click()
    time.sleep(2)
    driver.find_element(By.XPATH, copy_to_clip_additional_data).click()
    time.sleep(2)
    driver.find_element(By.XPATH, continue_button).click()
    time.sleep(2)
    data_from_clipboard = ""
    win32clipboard.OpenClipboard()
    data_from_clipboard = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data_from_clipboard