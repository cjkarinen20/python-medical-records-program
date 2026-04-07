import FreeSimpleGUI as sg
import dataFunctions

# Reads the input fields and pass them to try_to_create_patient.
def read_input_values(values):
    first_name = values["FIRST_NAME"]
    last_name = values["LAST_NAME"]
    date_of_birth = values["DATE_OF_BIRTH"]
    height = values["HEIGHT"]
    weight = values["WEIGHT"]
    taking_medication = values["IS_TAKING_MEDICATION"]
    created_patient = dataFunctions.try_to_create_patient(first_name, last_name, date_of_birth, height, weight, taking_medication)
    return created_patient
    
# Create the Patient Intake Form.
def create_layout():
    return [
    [sg.Text("First Name"), sg.Input(key = "FIRST_NAME")],
    [sg.Text("Last Name"), sg.Input(key = "LAST_NAME")],
    [sg.Text("Date Of Birth"), sg.Input(key = "DATE_OF_BIRTH"), 
    sg.CalendarButton("Select Date", format = '%m/%d/%Y')],
    [sg.Text("Height"), sg.Input(key = "HEIGHT")],
    [sg.Text("Weight"), sg.Input(key = "WEIGHT")],
    [sg.Text("Is Taking Medication?"), sg.Checkbox("Yes", key = "IS_TAKING_MEDICATION")],
    [sg.Cancel(), sg.Button("Save")]]

# Create Patient Intake Form and load values from an existing patient (for edit feature)
def load_layout(patient):
    return [
    [sg.Text("First Name"), sg.Input(patient.first_name, key = "FIRST_NAME")],
    [sg.Text("Last Name"), sg.Input(patient.last_name, key = "LAST_NAME")],
    [sg.Text("Date Of Birth"), sg.Input(patient.date_of_birth, key = "DATE_OF_BIRTH"), 
    sg.CalendarButton("Select Date", format = '%m/%d/%Y')],
    [sg.Text("Height"), sg.Input(patient.height, key = "HEIGHT")],
    [sg.Text("Weight"), sg.Input(patient.weight, key = "WEIGHT")],
    [sg.Text("Is Taking Medication?"), sg.Checkbox("Yes", default = patient.taking_meds, key = "IS_TAKING_MEDICATION")],
    [sg.Cancel(), sg.Button("Save")]]

# Create patient intake form, display it, and capture user input.
def display_new_intake_form():
    patient_intake_layout = create_layout()
    patient_intake_window = sg.Window("New Patient Form", patient_intake_layout)
    
    save_success = False
    
    while True:
        event, values = patient_intake_window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif event == "Save":
            save_success = read_input_values(values)
            if save_success:
                print("Patient Saved.")
            break
        else:
            print("Could not save patient, invalid input.")
    patient_intake_window.close()
    return save_success

def load_intake_form(patient):
    patient_edit_layout = load_layout(patient)
    patient_edit_window = sg.Window("Edit Patient Form", patient_edit_layout)
    
    save_success = False
    
    while True:
        event, values = patient_edit_window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif event == "Save":
            save_success = read_input_values(values)
            if save_success:
                print("Patient Edits Saved.")
            break
        else:
            print("Could not save patient, invalid input.")
    patient_edit_window.close()
    return save_success