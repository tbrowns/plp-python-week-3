
def calculate_discount(price, discount_percent):
    if discount_percent < 20 : return price
    return price * (1 - discount_percent / 100)

print(15*"*","Discount Calculator",15*"*" )
price = int(input("Enter the original price: "))
discount_percent = int(input("Enter discount percent: "))
print(calculate_discount(price, discount_percent))