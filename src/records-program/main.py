from patient import Patient
from datetime import datetime

patients = [Patient("Nimmi", "JingleBop", datetime(1,6,1990), 185, 90.3, True),
           Patient("Joe", "Blough", datetime(7,2,2000), 185, 90.3, False),
           Patient("Elfrick", "Belghini", datetime(6,25,1962), 185, 90.3, False)]

print(patients[0].convert_info_to_strings())