import FreeSimpleGUI as sg
import patientIntakeForm
import dataFunctions 
 
# Headings for the Patient information table.
table_headings = ["First Name", "Last Name", "Date of Birth", "Height", "Weight", "Is Taking Medication?"]

# Patient Table Data.
table_data = dataFunctions.convert_patients_to_table_data()

# Button to Add New Patients.
def press_add_patient_button(patient_window):
    save_success = patientIntakeForm.display_new_intake_form()
    if save_success:
        table_data = dataFunctions.convert_patients_to_table_data()
        patient_window["PATIENT_TABLE"].update(values = table_data)

# Button to Edit Existing Patients.
def press_edit_patient_button(patient_window):
    selected_indices = values["PATIENT_TABLE"]
    
    if not selected_indices: # No patient entry was selected.
        sg.popup("Please select an entry to edit.", title = "No Selection.")
    elif len(selected_indices) > 1: # More than one entry was selected.
        sg.popup("Please select only ONE entry to edit.", title = "Too Many Selections.")
    else:
        patient = dataFunctions.retrieve_patient_selection(selected_indices)
        dataFunctions.delete_patient(selected_indices)
        save_success = patientIntakeForm.load_intake_form(patient)
        if save_success:
            table_data = dataFunctions.convert_patients_to_table_data()
            patient_window["PATIENT_TABLE"].update(values = table_data)

# Button to Delete Patients.
def press_delete_patient_button(patient_window, values):
    selected_indices = values["PATIENT_TABLE"]
    if not selected_indices: # No patient entry was selected.
        sg.popup("Please select an entry to delete.", title = "No Selection.")
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
    [sg.Text("All Patient Data"), sg.Button("Add New Patient"), sg.Button("Edit Patient"), sg.Button("Delete Patient")],
    [sg.Table(headings = table_headings, values = table_data, key = "PATIENT_TABLE", enable_events = True, enable_click_events = True)]]
patient_window = sg.Window('Patient List', patient_window_layout)

# Tracking variables for table column sort
last_col_clicked = -1
is_ascending = True

# Display Patient Window.
while True:
    event, values = patient_window.read()
    
    if isinstance(event, tuple) and event[0] == "PATIENT_TABLE":
        
        # event[2] = (row, col)
        row, col = event[2]
        
        if row == -1 and col is not None:
            # If clicking same column, toggle direction
            if col == last_col_clicked:
                is_ascending = not is_ascending
            else:
                # If click new column, default to ascending
                is_ascending = True
                last_col_clicked = col
                
            table_data = sorted(table_data, key=lambda x: x[col], reverse=not is_ascending) # Sort table_data
            
            # Refresh Table Graphics
            patient_window["PATIENT_TABLE"].update(values=table_data)
            
    if event == sg.WIN_CLOSED:
        break
    elif event == "Add New Patient":
        press_add_patient_button(patient_window)
    elif event == "Delete Patient":
        press_delete_patient_button(patient_window)
    elif event == "Edit Patient":
        press_edit_patient_button(patient_window)
        
patient_window.close()