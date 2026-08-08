# Day 2 – Loops and Data Structures
This assignment focuses on Python loops, collections, comprehensions, and basic data processing. The exercises build practical skills using `for` loops, `while` loops, lists, sets, dictionaries, nested dictionaries, and an interactive contact book.

## Topics Covered
* `for` loops
* `while` loops
* `range()`
* `break` and `continue`
* Conditional statements (`if`, `elif`, `else`)
* Modulo operator (`%`)
* Lists
* List comprehensions
* Sets
* Set operations
* Dictionaries
* Dictionary comprehensions
* Nested dictionaries
* `isinstance()`
* `sorted()`, `sum()`, `len()`, and `max()`
* F-strings and formatted output
* User input
* Menu-driven programs

## Exercises Completed

### Exercise 1: Batch Processor

* Used a `for` loop and `range()` to process batches from 1 to 10.
* Used the modulo operator to identify every third batch.
* Displayed a checkpoint message after every third batch.

### Exercise 2: Retry Simulation

* Used a `while` loop to simulate retry attempts.
* Limited the operation to a maximum of three attempts.
* Used `break` to stop the loop when the operation succeeds.
* Simulated a successful operation on the second attempt.

### Exercise 3: Clean Numeric Values

* Worked with a list containing integers, `None`, and an invalid string.
* Used a `for` loop to filter valid integers.
* Used `continue` to skip invalid values.
* Used `isinstance()` to check whether values are integers.
* Solved the same problem again using a list comprehension.

### Exercise 4: Sales List Analysis

* Sorted sales amounts from highest to lowest.
* Filtered sales values above `100000`.
* Added 13% tax to each sales amount.
* Calculated the total sales amount.
* Calculated the average sales amount.
* Used list comprehensions where appropriate.

### Exercise 5: Dataset Comparison

* Worked with Python sets to compare two datasets.
* Found all unique dataset names.
* Found datasets common to both groups.
* Found datasets that exist only in `dataset_a`.
* Found datasets that exist only in `dataset_b`.

### Exercise 6: Student Score Dictionary

* Created a dictionary containing student names and scores.
* Printed each student and their score.
* Created a dictionary containing students who scored at least 60.
* Used a dictionary comprehension for filtering passing students.
* Found the student with the highest score.
* Calculated the average student score.

### Exercise 7: Nested Order Summary

* Worked with nested dictionaries to store order information.
* Printed order IDs and customer names.
* Filtered and displayed completed orders.
* Calculated the total amount of completed orders.
* Counted pending orders.
* Added a new order to the dictionary.

### Stretch Exercise: Contact Book Menu

* Built an interactive contact book using a `while` loop.
* Stored contacts using nested dictionaries.
* Added contacts with a name, phone number, and email address.
* Searched for contacts.
* Deleted contacts.
* Displayed all contacts.
* Handled missing contacts without crashing the program.
* Used `break` to exit the program.

## What I Learned

Through these exercises, I learned how to use Python loops and data structures to process and organize data.

Key concepts I practiced include:

* Using `for` loops with `range()` for repeated operations.
* Using `while` loops for programs that need to continue running until a condition is met.
* Using `break` to exit a loop early.
* Using `continue` to skip invalid values.
* Using the modulo operator to check whether a number is divisible by another number.
* Using list comprehensions to filter and transform lists.
* Using set operations to compare groups of data.
* Using dictionaries to store key-value data.
* Using dictionary comprehensions to create filtered dictionaries.
* Accessing and modifying data stored in nested dictionaries.
* Using built-in functions such as `sorted()`, `sum()`, `len()`, and `max()`.
* Formatting output using f-strings.
* Handling user input in an interactive command-line program.

## Challenges Faced

Some of the challenges I faced while completing these exercises were:

* Understanding how the modulo operator works with conditions.
* Understanding when to use `break` and `continue`.
* Working with list comprehensions and understanding their structure.
* Understanding set operations such as union, intersection, and difference.
* Finding the highest score from a dictionary based on its values.
* Accessing values inside nested dictionaries.
* Formatting calculated values using f-strings.
* Handling missing contacts when searching or deleting.
* Managing multiple options in the contact book menu.
* Keeping the contact book running until the user selects the exit option.

Working through these challenges helped me improve my understanding of Python control flow and data structures.

## Instructions for Running the Programs

### Prerequisites

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python3 --version
```

### Project Structure

The assignment follows this structure:

```text
day-02-loops-and-data-structures/
├── README.md
├── exercise-01-batch-processor.py
├── exercise-02-retry-simulation.py
├── exercise-03-clean-values.py
├── exercise-04-sales-analysis.py
├── exercise-05-dataset-comparison.py
├── exercise-06-student-scores.py
├── exercise-07-order-summary.py
└── stretch-contact-book.py
```

### Running an Exercise

Navigate to the Day 2 directory:

```bash
cd day-02-loops-and-data-structures
```

Run an individual exercise using:

```bash
python3 exercise-01-batch-processor.py
```

For example:

```bash
python3 exercise-02-retry-simulation.py
python3 exercise-03-clean-values.py
python3 exercise-04-sales-analysis.py
python3 exercise-05-dataset-comparison.py
python3 exercise-06-student-scores.py
python3 exercise-07-order-summary.py
```

To run the stretch contact book:

```bash
python3 stretch-contact-book.py
```

The contact book is interactive, so follow the instructions displayed in the terminal.

### Dependencies

These exercises use only Python's built-in features.

**No external libraries or packages are required.**
