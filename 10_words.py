from datetime import datetime
import csv, os

data = []

file_name = "data1.csv"

file_path = os.path.join(os.path.expanduser("~"), "Desktop", "myProjects", "player1", file_name)

with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        name, birthdate = row
        data.append((name, birthdate))

# Get today's month and day
today_month_day = datetime.now().strftime("%m-%d")

for person in data:
    name, birthdate = person
    if today_month_day == birthdate[5:]:
        print(f"\nHello {name}! Happy birthday!!!!!!!!!!!!!!!!!!!!! You were born on {birthdate}")
    else:
        print(f"Hello {name}! You were born on {birthdate}")
