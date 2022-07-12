import json

def load_data(filename):
    patient_file = open(filename, "r")
    patient_data = json.load(patient_file)
    return patient_data


def update_name(id, updated_name, pdata):
    for patient in pdata["patients_list"]:
        if patient["patient_id"] == id:
            patient["firstname"] = updated_name

def save_updated_data(pdata):
    with open("patient_data.json", "w") as patient_data:
        json.dump(pdata, patient_data, indent=8)

        print("[+] FILE UPDATED\n")

patient_data = load_data("patient_data.json")
print("[+] BEFORE UPDATE\n")
print(patient_data["patients_list"])
print("[+] AFTER UPDATE\n")
update_name(1, "Thomas", patient_data)
print(patient_data["patients_list"])
print("[+] SAVING FILE\n")
save_updated_data(patient_data)
