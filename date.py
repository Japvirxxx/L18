from datetime import date , time , datetime

today = date.today()

now = datetime.now()

print("Today's date:", today)
print("\nCurrent time:", now)

print("\nCurrent year:", now.year)
print("\nCurrent month:", now.month)
print("\nCurrent day:", now.day)