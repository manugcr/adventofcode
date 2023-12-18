import os

# Define the range of numbers (14 to 31)
day_numbers = range(14, 32)

# Create folders and files
for day_number in day_numbers:
    # Create folder
    folder_name = f"day_{day_number:02d}"
    os.makedirs(folder_name, exist_ok=True)

    # Create input.txt file
    input_file_path = os.path.join(folder_name, "input.txt")
    with open(input_file_path, "w") as input_file:
        input_file.write(f"This is input.txt for day {day_number}.\n")

    # Create README.md file
    readme_file_path = os.path.join(folder_name, "README.md")
    with open(readme_file_path, "w") as readme_file:
        readme_file.write(f"# Day {day_number}\n\nThis is the README for day {day_number}.\n")

print("Folders and files created successfully.")

