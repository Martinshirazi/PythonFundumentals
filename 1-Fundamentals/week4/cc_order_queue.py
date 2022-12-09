class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return None

        return self.items.pop(0)

    def show_queue(self):
        return self.items


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        order = dict(customer=customer, flavor=flavor, scoops=scoops)
        if flavor not in self.flavors:
            print('please select one of the following flavors')
            for i in self.flavors:
                print(i)
        if not 1 <= scoops <= 3:
            print("Choose between 1-3 scoops")

        if flavor in self.flavors:
            if 1 <= scoops <= 3:
                self.orders.enqueue(order)
                print("Order Created.Thank you!")

    def show_all_orders(self):
        print("\nAll pending Ice Cream Orders: ")
        for order in self.orders.show_queue():
            print("Customer:", order["customer"], "---", "Flavor:", order['flavor'], "---", "Scoops:", order['scoops'])

    def next_order(self):
        print("Next Order Up!")
        order = self.orders.dequeue()
        print('Customer:', order['customer'], '---', 'Flavor:', order['flavor'], '---', 'Scoops:', order['scoops'])


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()