from datetime import datetime

# Create two datetime objects
date1 = input("Enter your first date (MM-DD-YYYY): ")
date2 = input("Enter your second date (MM-DD-YYYY): ")

# Calculate the difference between two dates
date_difference = date2 - date1
print("Difference between dates:", date_difference)  # Output: 10 days, 0:00:00

# Adding a timedelta to a date
time_difference = datetime.timedelta(days=5)
new_date = date1 + time_difference
print("New date:", new_date)  # Output: 2023-08-31 00:00:00

# Subtracting a timedelta from a date
new_date = date2 - time_difference
print("New date:", new_date)  # Output: 2023-09-01 00:00:00








