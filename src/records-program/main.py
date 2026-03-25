
import FreeSimpleGUI as sg
from data_functions import *

#Headings for the Patient information table.
table_headings = ["First Name", "Last Name", "Date of Birth", "Height", "Weight", "Is Taking Medication?"]

table_data = convert_patients_to_table_data()

#Properties for the Patient Window GUI.
patient_window_layout = [[sg.Table(headings = table_headings, values = convert_patients_to_table_data())]]
patient_window = sg.Window('Patient List', patient_window_layout)

while True:
    event, values = patient_window.read()
    if event == sg.WIN_CLOSED:
        break
patient_window.close()