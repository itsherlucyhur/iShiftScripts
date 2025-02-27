# Sites (Transactions)
ME5A_site = 'https://shift.sanofi.com:44350/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html?sap-client=100#Shell-startGUI?sap-ui2-tcode=ME5A&sap-system=FIORIS4H'
ME5K_site = 'https://shift.sanofi.com:44350/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html?sap-client=100#Shell-startGUI?sap-ui2-tcode=ME5K&sap-system=FIORIS4H'
IW39_site = 'https://shift.sanofi.com:44350/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html?sap-client=100#Shell-startGUI?sap-ui2-tcode=IW39&sap-system=FIORIS4H'
ME23N_site = 'https://shift.sanofi.com:44350/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html?sap-client=100#Shell-startGUI?sap-ui2-tcode=ME23N&sap-system=FIORIS4H'
"""

Elements 

"""

# ME5A
iframe = 'application-Shell-startGUI-iframe'
purchase_requisition_field = '//*[@id="M0:46:::0:34"]'
purchasing_group_field = '//*[@id="M0:46:::1:78"]'
option1_purchasing_group = '/html/body/table/tbody/tr/td/div/div/div[1]/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[1]/td[2]/div/span/input'
option2_purchasing_group = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[2]/td[2]/div/span/span[1]'
option2_purchasing_group_input = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[2]/td[2]/div/span/input'
copy_button = '//*[@id="M1:48::btn[8]"]'
material_group_field = '//*[@id="M0:46:::3:78"]'
option1_material_group = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[1]/td[2]/div/span/input'
option2_material_group = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[2]/td[2]/div/span/span[1]'
option2_material_group_input = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[2]/td[2]/div/span/input'
option3_material_group = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[3]/td[2]/div/span/span[1]'
option3_material_group_input = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[3]/td[2]/div/span/input'
# copy_button_material_group = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/span[3]/div'
document_type_button = '//*[@id="M0:46:::6:78"]'
option1_document_type = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[1]/td[2]/div/span/input'
option2_document_type = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[2]/td[2]/div/span'
option2_document_type_input = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/section/div[2]/div[1]/table/tbody/tr[2]/td/div[1]/table/tbody/tr/td/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div[2]/table/tbody/tr[2]/td[2]/div/span/input'
# copy_button_document_type = '//*[@id="M1:48::btn[8]"]'
held_prs_checkbox = '//*[@id="M0:46:::20:3"]'
closed_reqs_checkbox = '//*[@id="M0:46:::21:3"]'
execute_button = '//*[@id="M0:50::btn[8]"]'
purchase_requisition_column = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/div[1]/div/div/table/tbody[1]/tr[1]/td[1]/div/div/table/tbody/tr/th[7]/div/table/tbody/tr'
clear_filter_button = '//*[@id="M0:48::btn[29]"]'
mrp_controller_filter = '//*[@id="M1:46:1::2:34"]'
delete_button = '//*[@id="M1:48::btn[16]"]'
check_button = '//*[@id="M1:50::btn[0]"]'
local_file_button = '//*[@id="M0:48::btn[45]"]'
copy_to_clipboard_button = '//*[@id="M1:46:2:1::4:0"]'
continue_button = '//*[@id="M1:50::btn[0]"]'

# ME5K
loading_status = '//*[@id="__bar0-BarLeft"]'
cost_center = '//*[@id="M0:46:::0:34"]'
pr_field = '//*[@id="M0:46:::10:78"]'
paste_from_clipboard = '//*[@id="M1:48::btn[24]"]'
copy_button_purchase_requisition = '//*[@id="M1:48::btn[8]"]'
held_prs_checkbox1 = '//*[@id="M0:46:::29:3"]'
closed_reqs_checkbox1 = '//*[@id="M0:46:::30:3"]'

# IW39
completed_checkbox = '//*[@id="M0:46:::1:29"]'
historical_checkbox = '//*[@id="M0:46:::1:42"]'
work_order_field = '//*[@id="M0:46:::4:78"]'
start_period = '#M0\:46\:\:\:14\:34'
end_period = '#M0\:46\:\:\:14\:59'
copy_button_work_order = '//*[@id="M1:48::btn[8]"]'
menu_dropdown = 'cua2sapmenu_btn'
list_select = '/html/body/table/tbody/tr/td/div/div/div/div[2]/span[1]/div/div[2]/table/tbody/tr[1]'
more_dropdown = '/html/body/table/tbody/tr/td/div/form/div/div[1]/div/div[1]/div/div/div/div[1]/span[17]/div'
main_table = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/div[1]/div/div/table/tbody[1]/tr[2]/td[2]/div/div/table'
list_expand = '/html/body/table/tbody/tr/td/div/div/span[2]/div/div[2]/table/tbody/tr[3]'
save_dropdown = '/html/body/table/tbody/tr/td/div/div/div/div[2]/span[20]/div/div[2]/table/tbody/tr[12]'
save_select = '/html/body/table/tbody/tr/td/div/div/div/div[2]/span[3]/div/div[2]/table/tbody/tr[12]'
file_dropdown = '/html/body/table/tbody/tr/td/div/div/div/div[2]/span[19]/div/div[2]/table/tbody/tr[3]'
file_select = '/html/body/table/tbody/tr/td/div/div/div/div[2]/span[2]/div/div[2]/table/tbody/tr[3]'
copy_to_clip_additional_data = '//*[@id="M1:46:2:1::4:0"]'

#ME23N
# header = '//*[@id="M0:46:1:2:1::0:0"]' # XPATH
header = '#M0\:46\:1\:2\:1\:\:0\:0'      # CSS
status = 'M0:46:1:2:2:1:1::0:8-title'       # ID
other_po_button = '#M0\:48\:\:btn\[17\]'
po_field = '//*[@id="M1:46:1::0:21"]'   # xpath
purch_requisition = '#M1\:46\:1\:\:3\:0-txt' 
search_field = '#M1\:46\:1\:\:0\:21'
search = '//*[@id="M1:50::btn[0]"]'
item_overview = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[3]/div/div[1]/div/div/div'
po = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/div[8]/table/tbody/tr/td/div/div/div/div[2]/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div/table/tbody/tr[1]/td[3]/div/span/span/span'
# /html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/div[8]/table/tbody/tr/td/div/div/div/div[2]/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div/table/tbody/tr[1]/td[3]/div/span/span
ordered_text = '//*[@id="M0:46:1:2:2:1:1:2B264:1::0:0"]'    # xpath
ordered = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[2]/td/div[9]/table/tbody/tr/td/div/div/div/div[5]/div/div[1]/span/span'
other_ordered = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[2]/td/div[9]/table/tbody/tr/td/div/div/div/div[4]/div/div[1]/span/span'
delivered_text = '//*[@id="M0:46:1:2:2:1:1:2B264:1::1:0"]'
delivered = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[2]/td/div[9]/table/tbody/tr/td/div/div/div/div[5]/div/div[3]/span/span'
other_delivered = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[2]/td/div[9]/table/tbody/tr/td/div/div/div/div[4]/div/div[3]/span/span'
invoiced_text = '//*[@id="M0:46:1:2:2:1:1:2B264:1::3:0"]'
invoiced = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[2]/td/div[9]/table/tbody/tr/td/div/div/div/div[5]/div/div[7]/span/span'
other_invoiced = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[2]/td/div[9]/table/tbody/tr/td/div/div/div/div[4]/div/div[7]/span/span'
item_detail = '#M0\:46\:1\:4\:1\:\:0\:0'    # CSS
purchase_order_history = '#M0\:46\:1\:4\:2\:1\:2\:1\:\:0\:16-title' # CSS
po_history = '#M0\:46\:1\:4\:2\:1\:2\:1\:\:0\:16-title'
key_word = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/div[9]/table/tbody/tr/td/div/div/div/div/div/div[1]/div/div/table/tbody[1]/tr[2]/td[1]/div/div/table/tbody[1]/tr[1]/td[1]/div/span/span'
diff_key_word = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/div[8]/table/tbody/tr/td/div/div/div/div/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div/table/tbody/tr[1]/td[1]/div/span/span'
date = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/div[9]/table/tbody/tr/td/div/div/div/div/div/div/div/div/table/tbody[1]/tr[2]/td[1]/div/div/table/tbody[1]/tr[1]/td[5]/div/span/span[1]'
diff_date = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/div[8]/table/tbody/tr/td/div/div/div/div/div/div[1]/div/div/table/tbody[1]/tr[2]/td[1]/div/div/table/tbody/tr[1]/td[5]/div/span/span[1]'
# po 3000013186 3000014521 E004767170
# pr 29006684
pr_search = '/html/body/table/tbody/tr/td/div/div/div/div[11]/div/footer/div[1]/div/div/div[1]/span[2]/div'
pr_status = '/html/body/table/tbody/tr/td/div/form/div/div[4]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/div[8]/div'
pr_item_detail = '#M0\:46\:1\:4\:1\:\:0\:0'
