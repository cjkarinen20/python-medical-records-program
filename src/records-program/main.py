from patient import Patient
from datetime import datetime
import PySimpleGUI as sg

patients = [Patient("Nimmi", "JingleBop", datetime(1,6,1990), 185, 90.3, True),
           Patient("Joe", "Blough", datetime(7,2,2000), 185, 90.3, False),
           Patient("Elfrick", "Belghini", datetime(6,25,1962), 185, 90.3, False)]
def convert_patients_to_table_data():
    patient_data = []
    for patient in patients:
        strings = patient.convert_info_to_strings()
        patient_data.append(strings)
    return patient_data

print(convert_patients_to_table_data())