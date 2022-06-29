import csv

csv_columns = ["Patient_ID", "First_Name", "Last_Name", "Gender", "Age"]
def csv_dict_read():
    patient_list = []
    csv_file = open("patient_data.csv", "r")
    csv_data = csv.DictReader(csv_file)
    for item in csv_data:
        patient_list.append(item)

    print(patient_list)
    return patient_list

def csv_read():
    csv_file = open("patient_data.csv", "r")
    # csv_cols = csv_file.readline()
    # print(csv_cols)
    csv_data = csv.reader(csv_file)
    for col in csv_data:
        print(col)

def csv_dict_write():
    patient_list = csv_dict_read()
    csv_file = open("patient_data.csv", "w")
    csv_data = csv.DictWriter(csv_file, csv_columns)
    csv_data.writeheader()
    for item in patient_list:
        csv_data.writerow(item)

csv_dict_read()