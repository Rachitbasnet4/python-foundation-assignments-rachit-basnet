'''
Exercise 3: File Validator
Student: Rachit Basnet
Day: 1
'''

# List of allowed file extensions
allowed_extensions = [".csv", ".json", ".parquet"]

# Keep asking the user until a valid file is entered
while True:
    # Get the file name from the user, remove extra spaces, and convert it to lowercase
    file_name = input("Enter the file name: ").strip().lower()

    # Check if the file name ends with one of the allowed extensions
    if file_name.endswith(tuple(allowed_extensions)):
        print("Valid file.")
        break
    # If the file extension is not allowed, display an error message
    else:
        print("Invalid file. Only .csv, .json, and .parquet files are allowed. Try again.")
