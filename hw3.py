d = int(input('할인율은? ')) # 20 

discount_A = int(input('A상품의 할인된 가격은? ')) # 8000

discount_B = int(input('B상품의 할인된 가격은? ')) # 12000

def get_fixed_price(discount_price) :
    price = discount_price * (1/(1-d/100))

    return price 

price_A = get_fixed_price(discount_A)
price_B = get_fixed_price(discount_B)

print('A상품의 정가는',price_A,"원")
print('B상품의 정가는',price_B,"원")