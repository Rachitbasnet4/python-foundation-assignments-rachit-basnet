'''
Exercise 4: Customer Record Cleaner
Student: Rachit Basnet
Day: 1
'''

# Raw user data with extra spaces and inconsistent capitalization
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Convert age from string to integer
cleaned_age = int(raw_age)

# Check if the person is an Adult or Minor based on age
status = "Adult" if cleaned_age >= 18 else "Minor"

# Display the cleaned and formatted data
print(f"Name: {raw_name.strip().title()}") 
print(f"City: {raw_city.strip().title()}") 
print(f"Age: {cleaned_age}") 
print(f"Status: {status}")
