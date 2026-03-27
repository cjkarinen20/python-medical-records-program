import FreeSimpleGUI as sg

def read_input_values(values):
    first_name = values["FIRST_NAME"]
    last_name = values["LAST_NAME"]
    date_of_birth = values["DATE_OF_BIRTH"]
    height = values["HEIGHT"]
    weight = values["WEIGHT"]
    taking_medication = values["IS_TAKING_MEDICATIONS"]
    print(first_name)
    print(last_name)
    print(date_of_birth)
    print(height)
    print(weight)
    print(taking_medication)
    
#Create the Patient Intake Form.
def create_layout():
    return [
    [sg.Text("First Name"), sg.Input(key = "FIRST_NAME")],
    [sg.Text("Last Name"), sg.Input(key = "LAST_NAME")],
    [sg.Text("Date Of Birth"), sg.Input(key = "DATE_OF_BIRTH"), 
    sg.CalendarButton("Select Date", format = '%Y/%m/%d')],
    [sg.Text("Height"), sg.Input(key = "HEIGHT")]
    [sg.Text("Weight"), sg.Input(key = "WEIGHT")]
    [sg.Text("Is Taking Medication?"), sg.Checkbox("Yes", key = "IS_TAKING_MEDICATION")],
    [sg.Cancel(), sg.Button("Save")]]

# Create patient intake form, display it, and capture user input.
def display_intake_form():
    patient_intake_layout = create_layout()
    patient_intake_window = sg.Window("New Patient Form", patient_intake_layout)
    
    while True:
        event, values = patient_intake_window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif event == "Save":
            read_input_values(values)
            break
    patient_intake_window.close()