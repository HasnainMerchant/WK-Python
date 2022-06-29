import json

class Patient:
    choice = 0

    def __init__(self, file_handle):
        self.patient_data = json.load(file_handle)

    def patient_menu(self):
        self.choice = int(input("\n1. CREATE PATIENT\n2. DELETE PATIENT\n3. UPDATE PATIENT\nCHOICE - "))
        if self.choice == 1:
            self.create_patient()
        elif self.choice == 2:
            self.delete_patient()
        elif self.choice == 3:
            self.update_patient()

    def display_data(self):
        print(self.patient_data)

    def create_patient(self):
        print("[+] CREATING PATIENT....")

        patient = {}

        patient["patient_id"] = int(input("ENTER PATIENT ID - "))
        patient["firstname"] = input("ENTER PATIENT's FIRSTNAME - ")
        patient["lastname"] = input("ENTER PATIENT's LASTNAME - ")
        patient["gender"] = input("ENTER PATIENT's GENDER - ")
        patient["age"] = int(input("ENTER PATIENT's AGE - "))

        self.patient_data["patient_list"].append(patient)

        print("[+] PATIENT SUCCESSFULLY CREATED !")
        self.save_data()
        print("[+] SAVED FILE !\n")

        self.display_data()

    def save_data(self):
        print("[+] SAVING TO FILE....")
        with open("patient_data.json", "w") as patient_data:
            json.dump(self.patient_data, patient_data, indent=8)
            print("[+] FILE UPDATED")

    def delete_patient(self):
        print("[-] DELETING PATIENT....")

    def update_patient(self):
        print("[+] UPDATING PATIENT....")

class Appointment:
    choice = 0
    def __init__(self, file_handle):
        self.appointment = json.load(file_handle)
    def appointment_menu(self):
        self.choice = int(input("\n1. GET APPOINTMENT\n2. EDIT APPOINTMENT\n3. DELETE APPOINTMENT\nCHOICE - "))
        if self.choice == 1:
            self.get_appointment()
        elif self.choice == 2:
            self.edit_appointment()
        elif self.choice == 3:
            self.delete_appointment()

    def get_appointment(self):
        print("[+] FETCHING APPOINTMENT....")
    def edit_appointment(self):
        print("[+] EDITING APPOINTMENT....")
    def delete_appointment(self):
        print("[-] DELETING APPOINTMENT....")

def main_menu():
    choice = int(input(("1. Patient Menu\n2. Appointment Menu\nChoice - ")))
    if choice == 1:
        p_file_name = input("ENTER PATIENT FILE NAME") + ".json"
        patient_data = open(p_file_name, "r")
        patient1 = Patient(patient_data)
        patient1.patient_menu()
    elif choice == 2:
        ap_file_name = input("ENTER APPOINTMENT FILE NAME")
        appointment_data = open(ap_file_name, "r")
        appointment1 = Appointment(appointment_data)
        appointment1.appointment_menu()

if __name__ == "__main__":
    main_menu()