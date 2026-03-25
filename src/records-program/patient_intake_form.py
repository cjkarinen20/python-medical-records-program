import FreeSimpleGUI as sg

patient_intake_layout = [
    [sg.Text("First Name"), sg.Input()],
    [sg.Text("Last Name"), sg.Input()],
    [sg.Text("Date Of Birth"), sg.Input(), 
    sg.CalendarButton("Select Date")],
    [sg.Text("Height"), sg.Input()]
    [sg.Text("Weight"), sg.Input()]
    [sg.Text("Is Taking Medication?"), sg.Checkbox("Yes")],
    [sg.Cancel(), sg.Button("Save")]]

def display_intake_form():
    patient_intake_window = sg.Window("New Patient Form", patient_intake_layout)