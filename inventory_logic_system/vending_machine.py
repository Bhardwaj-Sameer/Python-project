items = [
    "Coke", "Chips", "Water", "Cookies", "Gum",
    "Juice", "Chocolate Bar", "Popcorn", "Iced Tea",
    "Candy", "Pretzels", "Energy Drink"
]

prices = [
    1.50, 2.00, 1.00, 2.25, 0.75,
    1.80, 2.40, 3.00, 1.70,
    1.10, 1.60, 3.25
]

bill=0

#Steps:
#1 Print the Menu
# Ask the user's choice
# Add total bill
# Ask for seconds
# Print the total bill
# Admin feature


while(True):
    for index, item in enumerate(items):
        print(f"{index+1}) {item} ({prices[index]})")
#menu printed

    req = input("What would you like to have? ('q' if you're full!)")
    if(req=="q"):
        break
    if(req.isdigit()):
        
        idx=int(req)-1
        if(0<=idx<len(items)):
            print(f"Here's your {items[idx]}")
            bill+=prices[idx]
        else:
            print("Please enter a valid item")
    elif(req=="admin"):
        new_item =input("What would you like to add? ")
        new_price=float(input("At what price? "))

        items.append(new_item)
        prices.append(new_price)
        print("Item added successfully!!")
    else:
        print("Please enter a number")

print(f"Your total bill is ${bill}")