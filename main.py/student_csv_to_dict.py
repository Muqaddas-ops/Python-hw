
import json
import csv
import os

# Paths
json_path = "data/data.json"
csv_path = "output/family_members.csv"

# Create output directory if not exists
os.makedirs("output", exist_ok=True)

# Only create CSV if it doesn't already exist
if not os.path.exists(csv_path):
    # Load JSON data
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Write to CSV
    with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["student_name", "member_id", "member_name", "age", "relative"])
        writer.writeheader()

        for student in data["students"]:
            for member in student["familymemebers"]:
                writer.writerow({
                    "student_name": student["name"],
                    "member_id": member["id"],
                    "member_name": member["name"],
                    "age": member["age"],
                    "relative": member["relative"]
                })

    print(f"CSV file created: {csv_path}")
else:
    print("CSV already exists. Skipping creation.")