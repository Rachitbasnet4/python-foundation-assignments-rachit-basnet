'''
Exercise 1: Sales Summary
Student: Rachit Basnet
Day: 1
'''

# Input Values
product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

# Calculations
gross_sales = unit_price * quantity_sold
discount_amount = gross_sales * discount_percentage
final_sale = gross_sales - discount_amount

# Display the results
print(f"Product: {product_name}")
print(f"Gross sales: NPR {gross_sales:.2f}")
print(f"Discount: NPR {discount_amount:.2f}")
print(f"Final Sale: NPR {final_sale:.2f}")
