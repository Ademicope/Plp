def calculate_discount(price, discount_percent):
    """This function calculates the final price ater applying a discount.
    """

    discount = price * discount_percent / 100
    if discount_percent >= 20:
        final_price = price - discount
    else:
        final_price = price
    return final_price


price = calculate_discount(int(input("Enter the price: ")), int(input("Enter the discount percentage: ")))
print(price)