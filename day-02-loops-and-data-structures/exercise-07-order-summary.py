'''
Exercise 7: Nested Order Summary
Name: Rachit Basnet
Day 2
'''

# nested order dictionary
orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# output: printing every order id and customer
for order_id, order_details in orders.items():
    print(f"Order ID and Customer:\n{order_id}: {order_details['customer']}")

print(f"\n")

# output: printing only completed
for order_id, order_details in orders.items():
    if order_details["status"] == "Completed":
        print(f"{order_id}:{order_details["status"]}")

# calculating the total amount of completed order
total_amount = 0

for order_details in orders.values():
    if order_details["status"]=="completed":
        total_amount += order_details["amount"]

# output
print(f"\nThe total amount of completed order is Rs.{total_amount}\n")

# counting pending order
pending_order = 0

for order_details in orders.values():
    if order_details["status"]=="Pending":
            pending_order += 1

# output
print(f"The number of pending order is {pending_order}\n")

# adding new order to the dictionary
orders["ORD-004"] = {
    "customer": "Rachit",
    "amount": 5000,
    "status": "Completed"
}

# output
print(f"Upated order:\n{orders}")
