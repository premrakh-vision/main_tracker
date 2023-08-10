from datetime import datetime

first_date = "2023-08-09 08:34:25.182392+05:30"
sec_date = "2023-08-09 08:34:40.182392+05:30"

# Convert the timestamp strings to datetime objects
format_string = '%Y-%m-%d %H:%M:%S.%f%z'
first_datetime = datetime.strptime(first_date, format_string)
sec_datetime = datetime.strptime(sec_date, format_string)

# Calculate the time difference
time_difference = sec_datetime - first_datetime

# Extract hours, minutes, and seconds from the time difference
hours = time_difference.seconds // 3600
minutes = (time_difference.seconds // 60) % 60
seconds = time_difference.seconds % 60

# Print the results
print(f"Time Difference: {hours} hours, {minutes} minutes, {seconds} seconds")
