'''
Exercise 5: Dataset Comparison
Name: Rachit Basnet
Day 2
'''

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# unique dataset from dataset_a and dataset_b
unique_dataset = dataset_a.union(dataset_b)

# common dataset in both a and b
common_dataset = dataset_a.intersection(dataset_b)

# dataset only in dataset_a
only_dataset_a = dataset_a.difference(dataset_b)

# dataset only in dataset_b
only_dataset_b = dataset_b.difference(dataset_a)

# output
print(f"All unique datasets: {unique_dataset}")
print(f"Common datasets: {common_dataset}")
print(f"Dataset only in dataset_a: {only_dataset_a}")
print(f"Dataset only in dataset_b: {only_dataset_b}")
