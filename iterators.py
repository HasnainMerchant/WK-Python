import json

path = "JSON_CSV/"

json_file = open(path+"patient_data.json")
json_data = json.load(json_file)
p_iterable = json_data["patient_list"]
p_itr = iter(p_iterable)

while True:
    try:
        print(next(p_itr))
    except StopIteration:
        print("List Has No More Items")