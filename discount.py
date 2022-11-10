from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()
day_of_week = 2
total = float(input("Please Enter the Subtotal: "))

if day_of_week == 1:

    discount = round(total*0.1, 2)
    total_discount = round(total - discount, 2)
    tax = round(total_discount*0.06, 2)
    total_amount = total + tax - discount
    print(f"Discount Amount: {discount}")
    print(f"Sales tax amount: {tax}")
    print(f"Total: {total_amount}")

elif day_of_week == 2:

    discount = round(total*0.1, 2)
    total_discount = round(total - discount, 2)
    tax = round(total_discount*0.06, 2)
    total_amount = total + tax - discount
    print(f"Discount Amount: {discount}")
    print(f"Sales tax amount: {tax}")
    print(f"Total: {total_amount}")

else:
    tax = round(total*0.06, 2)
    total_amount = total + tax
    print(f"Sales tax amount: {tax}")
    print(f"Total: {total_amount}")