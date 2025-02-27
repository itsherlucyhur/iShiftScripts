# iShiftScripts
## 1.1 System Overview

IShiftScripts is a Python-based automation solution designed to extract Purchase Orders (PO) and Work Orders (WO) data from the SAP S/4 HANA system. The script streamlines the financial tracking process by retrieving relevant data based on Purchase Requisitions (PRs) and Purchase Orders. By automating the data extraction, the automation scripts aim to reduce manual effort, and enhance efficiency of cost reporting and management in the team.  

## 1.2 Objectives

- Data Retrieval Automation from SAP  
- Improve Efficiency and Process Time 
- Enhance Accuracy & Consistency  
- Support Cost Tracking & Reporting – e.g. monthly work confirmation by each area to perform goods receipts. 

## 2.1 Usage

### 2.1.1 Requirements
Install the required dependencies (Selenium, pandas, numpy, pyautogui, openpyxl, etc.):\
```pip install -r requirements.txt```


### 2.1.2 Running the script:
```python main.py```


### 2.1.3 After running the script:
The output data file can be found in the Cost Tracker Folder. Find the latest file with today's date on it, which you can paste it at the end of the list on the Main Cost Tracker file (Cost Tracker Maintenance Control.xlsx). 
