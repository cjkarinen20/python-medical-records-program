import FreeSimpleGUI as sg
import patientIntakeForm
import dataFunctions 
 
# Headings for the Patient information table.
table_headings = ["First Name", "Last Name", "Date of Birth", "Height", "Weight", "Is Taking Medication?"]

# Patient Table Data.
table_data = dataFunctions.convert_patients_to_table_data()

# Button to Add New Patients.
def press_add_patient_button(patient_window):
    save_success = patientIntakeForm.display_intake_form()
    if save_success:
        table_data = dataFunctions.convert_patients_to_table_data()
        patient_window["PATIENT_TABLE"].update(values = table_data)
        
# Button to Delete Patients.
def press_delete_patient_button(patient_window):
    selected_indices = values["PATIENT_TABLE"]
    if not selected_indices: 
        sg.popup('Please select an entry to delete.')
    else:
        dialogChoice = sg.popup_yes_no("Do you want to delete this entry?", title="Confirm Deletion")
        if dialogChoice == "Yes":
            delete_success = dataFunctions.delete_patient(selected_indices)
            if delete_success:
                table_data = dataFunctions.convert_patients_to_table_data()
                patient_window["PATIENT_TABLE"].update(values = table_data)
            else:
                print("Could not delete patient: invalid index.")
        elif dialogChoice == "No":
            return
    
# Properties for the Patient Window GUI.
patient_window_layout = [
    [sg.Text("All Patient Data"), sg.Button("Add New Patient"), sg.Button("Delete Patient")],
    [sg.Table(headings = table_headings, values = table_data, key = "PATIENT_TABLE", enable_events = True)]]
patient_window = sg.Window('Patient List', patient_window_layout)

# Display Patient Window.
while True:
    event, values = patient_window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Add New Patient":
        press_add_patient_button(patient_window)
    elif event == "Delete Patient":
        press_delete_patient_button(patient_window)
        
patient_window.close()