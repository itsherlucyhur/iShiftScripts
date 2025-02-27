# Utility imports
import time
import logging
import pandas as pd
import datetime

# Importing all element locations from variable.py file
from variables import *

# ME5A import
from transactions.me5a import *
from transactions.me5k import *
from transactions.iw39 import *
from transactions.me23n import *
# Selenium imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


# Configure the logging settings
logging.basicConfig(filename="Raw Data\\logs\\python_script.txt", level=logging.INFO, format="%(asctime)s - %(message)s")
def log_message(message):
    # Logs the message with a timestamp
    logging.info(message)

def read_cost_tracker(file_path):
    # To read both 2023 and 2024 PR's
    # return pd.read_excel(file_path, index_col=None, sheet_name=['2023', '2024'], na_values=['NA'], usecols="E")
    return pd.read_excel(file_path, index_col=None, sheet_name='2024', na_values=['NA'], usecols="E")

def raw_data_to_text(data_from_clipboard, filename):
    if data_from_clipboard != "":
        with open(filename, 'w', encoding='utf8') as f:
            f.writelines(data_from_clipboard)
            f.close()

def write_to_excel(data, filename):
    df = pd.DataFrame(data).T
    df = df.map(lambda x: x.encode('unicode_escape').decode('utf-8') if isinstance(x, str) else x)
    df.to_excel(excel_writer = filename, index_label="PRs")

if __name__ == "__main__":
    file_path = 'Cost Tracker Maintenance Control.xlsx'
    
    # Driver options
    options = webdriver.EdgeOptions()
    options.add_argument("start-maximized")
    options.add_argument("log-level=3")
    options.add_argument("user-data-dir=C:\\Users\\U1037410\\AppData\\Local\\Microsoft\\Edge\\User Data")
    # Create WebDriver object
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(10)
    time.sleep(10)
    # Define wait for explicit waits
    wait = WebDriverWait(driver, 10)
    final_dict = {}
    # Get time
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%b %d %Y")
    
    """
    
    ME5A
    
    """

    clipboard_data = transaction_ME5A(driver, wait)
    raw_data_filename = "Raw Data\\ME5A\\" + current_date + " Raw Data" + ".txt"
    raw_data_to_text(clipboard_data, raw_data_filename)
    pr_from_file = read_cost_tracker(file_path)
    # pr_from_file = pd.concat([pr_from_file['2023'], pr_from_file['2024']])
    final_dict = compare_cost_tracker_me5a(pr_from_file, raw_data_filename)
    filename =  "Transaction Excel Data\\ME5A\\" + current_date + ".xlsx"
    write_to_excel(final_dict, filename)

    """

    ME5K

    """
    clipboard_data = transaction_ME5K(driver, wait)
    raw_data_filename = "Raw Data\\ME5K\\" + current_date + " Raw Data" + ".txt"
    raw_data_to_text(clipboard_data, raw_data_filename)
    final_dict, wo_pr_dict = process_ME5K_data(final_dict, raw_data_filename)
    filename = "Transaction Excel Data\\ME5K\\" + current_date + ".xlsx"
    write_to_excel(final_dict, filename)

    """
    
    IW39
    
    """
    clipboard_data = transaction_IW39(driver, wait)
    raw_data_filename = "Raw Data\\IW39\\" + current_date + " Raw Data" + ".txt"
    raw_data_to_text(clipboard_data, raw_data_filename)
    final_dict = process_IW39_data(final_dict, wo_pr_dict, raw_data_filename)
    filename = "Transaction Excel Data\\IW39\\" + current_date + ".xlsx"
    write_to_excel(final_dict, filename)

    cost_tracker_filename = 'Cost Tracker\\Cost Tracker ' + current_date + '.xlsx'
    write_to_excel(final_dict, cost_tracker_filename)
    driver.quit()

    """
    
    ME23N

    final_dict = transaction_ME23N(driver, wait, final_dict)
    # Final Data
    cost_tracker_filename = 'Cost Tracker\\Cost Tracker ' + current_date + '.xlsx'
    write_to_excel(final_dict, cost_tracker_filename)
    driver.quit()

    """

    