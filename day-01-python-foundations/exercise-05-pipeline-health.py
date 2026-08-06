'''
Exercise 5: Pipeline Health Status
Student: Rachit Basnet
Day: 1
'''

# Function to evaluate the health of a data pipeline
def pipeline_health(rows_loaded, rows_failed, runtime_minutes):
    # Calculate the total number of processed rows
    total_rows = rows_loaded + rows_failed

    # Calculate the percentage of failed rows
    failure_rate = (rows_failed / total_rows)*100

    # Classify the pipeline health based on failure rate and runtime
    # Healthy: Failure rate is 2% or less and runtime is 20 minutes or less
    # Warning: Failure rate is more than 2% but not more than 5%
    # Critical: Failure rate is greater than 5%
    if failure_rate <= 2 and runtime_minutes <= 20:
        status = "Healthy"
    elif failure_rate <= 5:
        status = "Warning"
    else:
        status = "Critical"

    # Display the pipeline health report
    print(f"Rows Loaded: {rows_loaded}")
    print(f"Rows Failed: {rows_failed}")
    print(f"Runtime: {runtime_minutes}")
    print(f"Failure Rate: {failure_rate}%")
    print(f"Health Status: {status}")
    print("-"*30)


# Test case 1
pipeline_health(9800, 200, 18)

# Test case 2
pipeline_health(9500, 500, 15)

# Test case 3
pipeline_health(9900, 100, 30)
