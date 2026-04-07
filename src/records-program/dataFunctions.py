from patient import Patient
from datetime import datetime
import FreeSimpleGUI as sg

# Initial list of patients to populate the table.
patients = [Patient("Nimmi", "JingleBop", datetime(1990,1,6), 185, 90.3, True),
           Patient("Joe", "Blough", datetime(2000,7,2), 185, 90.3, False),
           Patient("Elfrick", "Belghini", datetime(1962,6,25), 185, 90.3, False)]

# Converts each patient into strings in a list.
def convert_patients_to_table_data():
    patient_data = []
    for patient in patients:
        strings = patient.convert_info_to_strings()
        patient_data.append(strings)
    return patient_data

# Delete patient and update list.
def delete_patient(indices):
    for index, item in enumerate(indices):
        try:
            del patients[item]
        except IndexError:
            return False
    return True
            
# Retrieve selected patient entry.
def retrieve_patient_selection(indices):
    patient_index = indices[0]
    selected_patient = patients[patient_index]
    return selected_patient

# Validates input and attempts to create a patient.
def try_to_create_patient(first_name, last_name, date_of_birth, height, weight, taking_medication):
    if len(first_name) < 2 or len(last_name) < 2 or date_of_birth == "" or height == "" or weight == "":
        return False
    try:
        date_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y')
        
        if date_of_birth > datetime.now():
            return False
        
        height = int(height)
        weight = float(weight)
        
        if height <= 0 or weight <= 0:
            return False
        
        taking_medication = True if taking_medication == "True" else False
        
        patient = Patient(first_name, last_name, date_of_birth, height, weight, taking_medication)
        patients.append(patient)
        
        return True
    
    except Exception as e:
        print(e)
        return False