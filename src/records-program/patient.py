from datetime import datetime

class Patient:
    
    def __init__(self, first_name, last_name, date_of_birth, height, weight, taking_meds):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.height = height
        self.weight = weight
        self.taking_meds = taking_meds
        
    def convert_info_to_strings(self):
        date_of_birth = datetime.strftime(self.date_of_birth, '%m/%d/%Y') #MM/DD/YYYY
        height = str(self.height)
        weight = str(self.weight)
        taking_meds = str(self.taking_meds)
        
        return [self.first_name, self.last_name, date_of_birth, height, weight, taking_meds]