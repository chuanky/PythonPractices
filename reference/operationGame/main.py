'''
    类：1. 地点; 2. 货物; 3. 
'''


meat_quantity = 100
wine_quantity = 100
meat_prefer = 0.7
wine_prefer = 0.3
tax = 0.1

M = 10000

meat_price = meat_prefer * M / meat_quantity
wine_price = wine_prefer * M / wine_quantity

meat_price_sell = (1 - tax) * meat_price
wine_price_sell = (1 - tax) * wine_price

print("Meat Price: " + str(meat_price) + "; Wine Price: " + str(wine_price))

# 做生意
sell_meat_quantity = 20

meat_quantity += sell_meat_quantity

meat_price = meat_prefer * M / meat_quantity
wine_price = wine_prefer * M / wine_quantity

print("Meat Price: " + str(meat_price) + "; Wine Price: " + str(wine_price))

buy_wine_quantity = 20

wine_quantity -= buy_wine_quantity

meat_price = meat_prefer * M / meat_quantity
wine_price = wine_prefer * M / wine_quantity

print("Meat Price: " + str(meat_price) + "; Wine Price: " + str(wine_price))

# 消耗和补货
for i in range(10):
    m = 5000
    consume_meat = meat_prefer * m
    consume_wine = wine_prefer * m

    meat_produce = 50
    wine_produce = 50

    meat_delta = meat_produce - consume_meat / meat_price
    meat_quantity += meat_delta
    wine_delta = wine_produce - consume_wine / wine_price
    wine_quantity += wine_delta

    # print(meat_quantity, wine_quantity)

    meat_price = meat_prefer * M / meat_quantity
    wine_price = wine_prefer * M / wine_quantity

    print("Meat Price: " + str(meat_price) + "; Wine Price: " + str(wine_price))
    print("Meat Sell Price: " + str((1 - tax) * meat_price) + "; Wine Sell Price: " + str((1 - tax) * wine_price))