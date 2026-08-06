'''
Stretch Exercise: Dataset Access Decision
Student: Rachit Basnet
Day: 1
'''
# List of roles that are allowed to access the system
allowed_role = ["analyst", "scientist", "engineer"]

# List of restricted datasets that cannot be accessed
restricted_datasets = ["salary_data", "personal_data"]

# Function to check whether a user has access
def check_acess(user_role, is_active, requested_dataset):
    # Check if the user account is inactive
    if not is_active:
        print("Access denied because the user is inactive.")
    # Check if the user's role is not allowed
    elif user_role not in allowed_role:
        print("Access denied because the role is not allowed.")
    # Check if the requested dataset is restricted
    elif requested_dataset in restricted_datasets:
        print("Access denied because the dataset is restricted.")
    # Grant access if all conditions are satisfied
    else:
        print("Access Granted. You can proceed")

# Test Case 1: Inactive user
print("Scenario 1:")
check_acess("analyst", False, "sales_data")

# Test Case 2: User with an unauthorized role
print("Scenario 2:")
check_acess("developer", True, "sales_data")

# Test Case 3: User requesting a restricted dataset
print("Scenario 3:")
check_acess("analyst", True, "salary_data")

# Test Case 4: Valid user requesting an allowed dataset
print("Scenario 4:")
check_acess("analyst", True, "sales_data")
