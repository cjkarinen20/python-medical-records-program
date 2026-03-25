from patient import Patient
from datetime import datetime
import FreeSimpleGUI as sg

patients = [Patient("Nimmi", "JingleBop", datetime(1990,1,6), 185, 90.3, True),
           Patient("Joe", "Blough", datetime(2000,7,2), 185, 90.3, False),
           Patient("Elfrick", "Belghini", datetime(1962,6,25), 185, 90.3, False)]
def convert_patients_to_table_data():
    patient_data = []
    for patient in patients:
        strings = patient.convert_info_to_strings()
        patient_data.append(strings)
    return patient_data
#print(convert_patients_to_table_data())

layout = [[sg.Text('Here is some text to display')]]
window = sg.Window('Title Here', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()