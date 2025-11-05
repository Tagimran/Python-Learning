import datetime

# Write a program to create a new file and write your name.

with open("info.txt", "w") as file:     # "w" means write mode (creates new file)
    file.write("Name: Imran Sayyad\n")

print("Step 1: File created and name written successfully.")


# Append today’s date and time into that file.

current_time = datetime.datetime.now()
with open("info.txt", "a") as file:     # "a" means append mode
    file.write(f"Date & Time: {current_time}\n")

print("Step 2: Date and time appended successfully.")


# Read and display file contents.

print("\nStep 3: Reading file contents...\n")
with open("info.txt", "r") as file:     # "r" means read mode
    contents = file.read()
    print(contents)


# Create a list of 5 cities and save them into a file.

cities = ["Pune", "Mumbai", "Delhi", "Hyderabad", "Bangalore"]
with open("cities.txt", "w") as city_file:
    for city in cities:
        city_file.write(city + "\n")

print("Step 4: Cities saved into 'cities.txt'.")


# Read the file back and print each city name.

print("\nStep 5: Reading city names...\n")
with open("cities.txt", "r") as city_file:
    for line in city_file:
        print(line.strip())   # .strip() removes newline characters
