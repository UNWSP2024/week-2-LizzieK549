def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    item1 = input("Enter name of item 1: ")
    item2 = input("Enter name of item 2: ")
    item3 = input("Enter name of item 3: ")
    item4 = input("Enter name of item 4: ")
    item5 = input("Enter name of item 5: ")

    subtotal = 89    #cost pre-tax
    tax = subtotal* .07
    total=subtotal + tax

    print("Thanks for shopping! Your subtotal is: $", subtotal)
    print("Tax amount: $", tax)

    print("Your total is: $", total)





calculate_total_purchase()