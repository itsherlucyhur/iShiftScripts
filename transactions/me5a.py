import time
import datetime
import win32clipboard
import pandas as pd
import re

# Importing all element locations from variable.py file
from variables import *

# Selenium imports
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
    
requester_mapping = {
    # Mapping of user IDs to requester names (to be filled as needed) 
    # 'User ID': 'Requester name'
}

def compare_cost_tracker_me5a(pr_from_file, raw_data_filename):
    """
    Compares purchase requisition numbers from the main cost tracker file with raw data extracted from SAP ME5A transaction
    """ 
    master_dict = {}        # stores all extracted PR details 
    final_dict = {}         # stores new PRs not in the cost tracker 
    fetched_list = []       # list to track new extracted PR numbers 

    with open(raw_data_filename, encoding="utf8") as f:
        for _ in range(10):     # Skip first 10 lines
            next(f)

        for line in f:
            line = line.split('|')

            if len(line) > 1:
                if '2025' in line[2].strip():
                    # Check if purchase_requisition is an integer
                    try:
                        purchase_requisition = int(line[4].strip())  # Try converting the 5th element
                        purchase_order = line[5].strip()
                    except ValueError:
                        # If not an integer, shift one column down and use the next element
                        line.pop(3)

                    if purchase_order != "":
                        purchase_order = int(purchase_order)
                    else:
                        purchase_order = ""
                    fetched_list.append(purchase_requisition)
                    master_dict[purchase_requisition] = {}

                    # Map requester ID to name if available 
                    try:
                        requester_name = requester_mapping[line[1].strip()]
                    except:
                        requester_name = line[1].strip()
                    master_dict[purchase_requisition]['Requester'] = requester_name

                    # Convert date format
                    date_list = (line[2].strip()).split('.')
                    date = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]))
                    date = date.strftime("%d-%b-%y")

                    # Add extracted values to the dictionary
                    master_dict[purchase_requisition]['Date'] = date
                    master_dict[purchase_requisition]['ETS Area'] = ""
                    master_dict[purchase_requisition]['To Be Tracked'] = ""
                    master_dict[purchase_requisition]['CBRE or non-CBRE'] = ""
                    master_dict[purchase_requisition]['Description'] = line[3].strip()      # This will now be the 4th element after pop
                    master_dict[purchase_requisition]['PR#'] = int(purchase_requisition)
                    master_dict[purchase_requisition]['PO#'] = purchase_order
                    master_dict[purchase_requisition]['Vendor'] = ""
                    master_dict[purchase_requisition]['CC#'] = ""
                    master_dict[purchase_requisition]['HACAT'] = line[7].strip()
                    master_dict[purchase_requisition]['SHIFT GL#'] = ""
                    Quantity = float(re.sub(",", "", line[8].strip()))
                    Valuation_Price = float(re.sub(",", "", line[10].strip()))
                    total_amount = Valuation_Price * Quantity
                    master_dict[purchase_requisition]['Total Amount'] = float(total_amount)
                    master_dict[purchase_requisition]['Remaining Amount'] = float(total_amount)
                    master_dict[purchase_requisition]['WO#'] = ""
                    master_dict[purchase_requisition]['Building#'] = ""
                    master_dict[purchase_requisition]['PM Type'] = ""
                    master_dict[purchase_requisition]['Settlement Cost Center'] = ""
                    master_dict[purchase_requisition]['Work Done/ Goods Delivered'] = ""
                    master_dict[purchase_requisition]['Invoice Status'] = ""
                    master_dict[purchase_requisition]['GR Date'] = ""
                    master_dict[purchase_requisition]['If GR done and no invoice, days of GR'] = ""
                    master_dict[purchase_requisition]['GR/Invoice Action required'] = ""
                    master_dict[purchase_requisition]['Recovered?'] = ""
                    master_dict[purchase_requisition]['Entered into E-Buy'] = ""
                    master_dict[purchase_requisition]['Approval Date'] = ""
                    master_dict[purchase_requisition]['Comments'] = ""
                    master_dict[purchase_requisition]['3-Quote Initiative? (Yes? No? N/Ap?)'] = ""
                    master_dict[purchase_requisition]['If no, Exemption type or Comment'] = ""


    # Convert PR numbers from the cost tracker to a set for comparison 
    final_list = {int(float(i)) for i in pr_from_file['PR#'].dropna()}
    print("Columns in input file:", pr_from_file.columns)
    fetched_list = set(fetched_list)

    # Identify new PRs pulled that are not in the cost tracker file 
    unique_values = fetched_list.difference(final_list)     # extracting items that aren't in the cost tracker yet 

    # Store new PRs in the final dictionary 
    for i in unique_values:
        final_dict[i] = master_dict[i]      # storing new values found
    
    # df_pr = pd.DataFrame(unique_values)
    df_pr = pd.DataFrame(list(unique_values), columns=["PR#"])
    print(df_pr)
    df_pr.to_clipboard(index=False, header=False)
    time.sleep(1)

    return final_dict   


def transaction_ME5A(driver, wait):
    """
    Automates the SAP ME5A transaction on the SAP S/4 HANA database to extract purchase requisition data.
    """ 
    # Query Definition
    driver.get(ME5A_site)
    wait.until(EC.presence_of_element_located((By.ID, iframe)))
    driver.switch_to.frame(driver.find_element(By.ID, iframe))
    wait.until(EC.presence_of_element_located((By.XPATH, purchase_requisition_field)))
    
    # PR Field 
    purchase_requisition = driver.find_element(By.XPATH, purchase_requisition_field)
    purchase_requisition.send_keys("*")
    driver.find_element(By.XPATH, "//html").click()  

    # Purchasing Group
    wait.until(EC.presence_of_element_located((By.XPATH, purchase_requisition_field))) 
    driver.find_element(By.XPATH, purchasing_group_field).click()
    time.sleep(1) 

    wait.until(EC.presence_of_element_located((By.XPATH, option1_purchasing_group)))
    option1 = driver.find_element(By.XPATH, option1_purchasing_group)
    option1.send_keys('01K')
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, option2_purchasing_group)))
    option2 = driver.find_element(By.CSS_SELECTOR, option2_purchasing_group).click() 
    option2 = driver.find_element(By.XPATH, option2_purchasing_group_input)
    option2.send_keys('01L')
    driver.find_element(By.XPATH, copy_button).send_keys(Keys.F8)
    time.sleep(1)

    # Material Group
    wait.until(EC.presence_of_element_located((By.XPATH, material_group_field)))
    driver.find_element(By.XPATH, material_group_field).click() 
    wait.until(EC.presence_of_element_located((By.XPATH, option1_document_type)))
    material1 = driver.find_element(By.XPATH, option1_material_group)
    material1.send_keys('MC2002')
    driver.find_element(By.XPATH, "//html").click()  

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, option2_material_group)))
    material2 = driver.find_element(By.CSS_SELECTOR, option2_material_group).click()
    material2 = driver.find_element(By.XPATH, option2_material_group_input)
    material2.send_keys('MC2014')


    material3 = driver.find_element(By.XPATH, option3_material_group).click()
    material3 = driver.find_element(By.XPATH, option3_material_group_input)
    material3.send_keys('CS5025')
    driver.find_element(By.XPATH, copy_button).click()
    time.sleep(2)

    # Checkboxes
    driver.find_element(By.XPATH, held_prs_checkbox).click()
    driver.find_element(By.XPATH, closed_reqs_checkbox).click()
    driver.find_element(By.XPATH, execute_button).click()           # click execute

    wait.until(EC.presence_of_element_located((By.XPATH, purchase_requisition_column)))
    time.sleep(1)

    # Choose Custom Layout to display results
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, choose_layout)))
    driver.find_element(By.CSS_SELECTOR, choose_layout).click()

    tscc_element = wait.until(
    EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '/TSCC')]"))
    )
    tscc_element.click()
    time.sleep(2)
    driver.find_element(By.XPATH, local_file_button).click()

    # Copy extracted PR data to clipboard 
    wait.until(EC.presence_of_element_located((By.XPATH, copy_to_clipboard_button)))
    driver.find_element(By.XPATH, copy_to_clipboard_button).click()
    driver.find_element(By.XPATH, continue_button).click()
    time.sleep(2)

    data_from_clipboard = ""
    win32clipboard.OpenClipboard()      # retrieve clipboard data
    data_from_clipboard = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    return data_from_clipboard