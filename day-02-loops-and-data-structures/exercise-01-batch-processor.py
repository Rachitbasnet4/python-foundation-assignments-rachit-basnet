'''
Exercise 1: Batch Processor
Name: Rachit Basnet
Day 2
'''

# looping through batch number from 1 to 10
for batch_number in range(1,11):
    print(f"Processing batch{batch_number}")

    # checking if the number is divisible by 3
    if batch_number % 3 ==0:
        print("Checkpoint  reached")
