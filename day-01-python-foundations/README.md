# Day 1: Python Foundations

## Topics Covered

* Variables
* Data Types
* String Methods
* Arithmetic Operators
* Comparison Operators
* Logical Operators
* Conditional Statements (`if`, `elif`, `else`)
* Functions
* Lists
* User Input
* Ternary Expressions

---

## Exercises

### 1. Sales Summary

* Created variables for product details.
* Calculated gross sales, discount amount, and final sales amount.

### 2. Data Quality Checker

* Calculated the total number of problematic rows.
* Computed the percentage of problematic rows.
* Classified the dataset as **Excellent**, **Acceptable**, or **Needs Cleaning**.

### 3. File Validator

* Accepted a filename from the user.
* Normalized the input using `strip()` and `lower()`.
* Validated whether the file extension was one of the supported formats:

  * `.csv`
  * `.json`
  * `.parquet`

### 4. Customer Record Cleaner

* Cleaned raw customer information using string methods.
* Converted the age from a string to an integer.
* Determined whether the customer is an **Adult** or **Minor** using a ternary expression.

### 5. Pipeline Health Status

* Calculated the pipeline failure rate.
* Determined the pipeline health status based on failure rate and runtime.
* Implemented the solution using a reusable function.

### 6. Dataset Access Decision

* Implemented role-based dataset access control.
* Checked user activity, allowed roles, and restricted datasets.
* Displayed specific reasons whenever access was denied.
* Tested multiple access scenarios.

---

## How to Run

If all exercises are in one file:

```bash
python day1_assignment.py
```

If each exercise is in a separate file:

```bash
python exercise-01-sales-summary.py
python exercise-02-data-quality-checker.py
python exercise-03-file-validator.py
python exercise-04-customer-record-cleaner.py
python exercise-05-pipeline-health-status.py
python exercise-06-dataset-access-decision.py
```

---

## What I Learned

During this assignment, I learned how to use Python fundamentals to solve practical problems related to data engineering. I practiced working with variables, data types, string methods, conditional statements, functions, user input, and lists. I also learned how to validate data, classify results based on business rules, and organize code into reusable functions for better readability.

---

## Challenges Faced

One challenge was implementing the file validator correctly. Initially, I attempted to use a `for` loop to validate the filename, but I realized that iterating over each character was unnecessary. I solved this by using the `endswith()` method to check the file extension directly. Another challenge was writing the conditional logic for the pipeline health and dataset access exercises, which I resolved by testing multiple scenarios to ensure the output matched the requirements.

---

## Code Structure

Each Python file includes:

* A descriptive docstring with the exercise name, student name, and day number.
* Meaningful variable names.
* Short comments where necessary.
* Clear and readable output.
* Proper formatting and organization.
* Code that runs without errors and follows the assignment requirements.
