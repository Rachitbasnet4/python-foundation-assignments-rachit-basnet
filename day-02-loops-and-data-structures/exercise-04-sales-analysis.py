'''
Exercise 4: Sales List Analysis
Name: Rachit Basnet
Day 2
'''

# input
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# sroting the list from highest to lowest
sorted_sales = sorted(monthly_sales, reverse=True)

# creating the list containif value above 100000
sales_above_100000 = [sale for sale in monthly_sales if sale > 100000]

# creating a list where each amount has 13% tax added
sales_with_tax = [sale * 1.13 for sale in monthly_sales]

# calculating total sale amount
total_sale = sum(monthly_sales)

# calculating average sales amount
avg_sale = total_sale / len(monthly_sales)

# output
print(f"Sorted sales: {sorted_sales}")
print(f"Sales above 100000: {sales_above_100000}")
print(f"Sales with 13% tax: {sales_with_tax}")
print(f"Total sale: {total_sale}")
print(f"Average sale: {avg_sale}")
