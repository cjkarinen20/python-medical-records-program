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

# Create patient intake form, display it, and capture user input.
def display_intake_form():
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