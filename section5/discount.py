amount = int(input("Enter the amount: "))
if amount <= 1000:
    discount = (amount * 10) / 100
    print("Discount is: ", discount)
elif 1000 < amount <= 5000:
    discount = (amount * 20) / 100
    print("Discount is: ", discount)
elif 5000 < amount <= 10000:
        discount = (amount * 30) / 100
        print("Discount is: ", discount)
elif amount > 10000:
    discount = (amount * 50) / 100
    print("Discount is: ", discount)

