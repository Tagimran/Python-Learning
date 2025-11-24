import json

# Convert dict → JSON string
data_dict = {"name": "Imran", "age": 20, "city": "Pune"}
json_string = json.dumps(data_dict)
print("JSON String:", json_string)

# Convert JSON → dict
json_input = '{"name": "Imran", "age": 20, "city": "Pune"}'
converted_dict = json.loads(json_input)
print("Converted Dict:", converted_dict)

# Save Python list into JSON file
tasks = ["Study", "Gym", "Python Project"]
with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)
print("tasks.json created!")

# Read JSON file and print values
with open("tasks.json", "r") as f:
    loaded_tasks = json.load(f)

print("Values from tasks.json:")
for t in loaded_tasks:
    print("-", t)

# Update a JSON file (modify 1 field)
with open("data.json", "r") as f:
    info = json.load(f)

info["age"] = 21

with open("data.json", "w") as f:
    json.dump(info, f, indent=4)

print("data.json updated!")