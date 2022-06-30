import json

path = "JSON_CSV/"
def patient_generator():
    json_file = open(path+"patient_data.json")
    json_data = json.load(json_file)
    for patient in json_data["patient_list"]:
        yield patient

for i in patient_generator():
    print(i)
    input()