from patient import Patient
from datetime import datetime
import FreeSimpleGUI as sg

#Initial list of patients to populate the table.
patients = [Patient("Nimmi", "JingleBop", datetime(1990,1,6), 185, 90.3, True),
           Patient("Joe", "Blough", datetime(2000,7,2), 185, 90.3, False),
           Patient("Elfrick", "Belghini", datetime(1962,6,25), 185, 90.3, False)]

#Converts each patient into strings in a list.
def convert_patients_to_table_data():
    patient_data = []
    for patient in patients:
        strings = patient.convert_info_to_strings()
        patient_data.append(strings)
    return patient_data