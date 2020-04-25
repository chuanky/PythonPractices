'''Country包含一个Market包含productions'''
class Country():
    def __init__(self, market, pos, tax):
        self.market = market
        self.pos = pos
        self.tax = tax
    
    def show_sell_prices(self):
        origin_prices = self.market.get_prices()
        sell_prices = {}
        for name, price in origin_prices.items():
            sell_prices[name] = price * (1 - self.tax)

        return sell_prices


class Market():
    def __init__(self, products, M, recover_rate):
        self.products = products
        self.M = M
        self.recover_rate = recover_rate
        self.prices = {}

    def get_consume_amount(self):
        result = {}
        self.get_prices()
        m = self.M * self.recover_rate
        for product in self.products:
            result[product.name] = m * product.preference / self.prices[product.name]

        self.consume_amount = result
        return result

    def get_produce_amount(self):
        result = {}
        for product in self.products:
            result[product.name] = product.init_quantity * self.recover_rate
        
        self.produce_amount = result
        return result

    def get_prices(self):
        for product in self.products:
            price = product.preference * self.M / product.quantity
            name = product.name
            self.prices[name] = price

        return self.prices

    def get_product(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p

    def sell(self, product_name, quantity):
        p = self.get_product(product_name)
        if p == None:
            print("product not found")
        else:
            p.quantity += quantity

    def pass_one_month(self):
        self.get_consume_amount()
        self.get_produce_amount()

        for product in self.products:
            name = product.name
            product_delta = self.produce_amount[name] - self.consume_amount[name]
            product.quantity += product_delta

        self.get_prices()
            

class Product():
    def __init__(self, name, quantity, preference):
        self.name = name
        self.quantity = quantity
        self.init_quantity = quantity
        self.preference = preference

    def consume(self, amount):
        self.quantity -= amount

    def product(self, amount):
        self.quantity += amount

def main():
    meat = Product('meat', 100, 0.7)
    wine = Product('wine', 100, 0.3)
    products = [meat, wine]

    market = Market(products, 10000, 0.3)
    country = Country(market, (0, 0), 0.1)

    print(country.market.get_prices())

    market.sell('meat', 30)
    print(market.get_prices())

    market.sell('wine', 30)

    for i in range(10):
        market.pass_one_month()
        print(market.get_prices())

main()