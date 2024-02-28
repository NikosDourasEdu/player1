from datetime import datetime

data = [
    ("Emily", "1990-05-15"),
    ("Alexander", "1985-10-25"),
    ("Sophia", "2000-03-08"),
    ("Liam", "1978-12-18"),
    ("Olivia", "1995-07-03"),
    ("William", "1982-09-12"),
    ("Isabella", "2002-11-30"),
    ("James", "1970-02-28"),
    ("Charlotte", "1988-06-10"),
    ("Benjamin", "1999-04-05")
]

# Get today's month and day
today_month_day = datetime.now().strftime("%m-%d")

for person in data:
    name, birthdate = person
    if today_month_day == birthdate[5:]:
        print(f"Hello {name}! Happy birthday!!!!!!!!!!!!!!!!!!!!! You were born on {birthdate}")
    else:
        print(f"Hello {name}! You were born on {birthdate}")
