import FreeSimpleGUI as sg
import patientIntakeForm
import dataFunctions 
 
#Headings for the Patient information table.
table_headings = ["First Name", "Last Name", "Date of Birth", "Height", "Weight", "Is Taking Medication?"]

#Patient Table Data.
table_data = dataFunctions.convert_patients_to_table_data()

#Button to Add New Patients.
def press_add_patient_button(patient_window):
    patientIntakeForm.display_intake_form()
    table_date = dataFunctions.convert_patients_to_table_data()
    patient_window["PATIENT_TABLE"].update(values = table_data)
    

#Properties for the Patient Window GUI.
patient_window_layout = [
    [sg.Text("All Patient Data"), sg.Button("Add New Patient")],
    [sg.Table(headings = table_headings, values = table_data, key = "PATIENT_TABLE")]]
patient_window = sg.Window('Patient List', patient_window_layout)

while True:
    event, values = patient_window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Add New Patient":
        press_add_patient_button(patient_window)
patient_window.close()