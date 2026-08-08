'''
Exercise 2: Retry Simulation
Name: Rachit Basnet
Day 2
'''
# input variable
attempt = 1
max_attempts = 3
operation_successful = False

# keep trying until the maxinum numbber of  attempts is reached
while attempt <= max_attempts:

    print(f"Attempt {attempt}")

    # checking second attempt is successful
    if attempt == 3:
        operation_successful = True
        break

    attempt += 1

# checking if the operation was sucessful
if operation_successful:
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")
