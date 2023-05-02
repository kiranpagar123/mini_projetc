class Flower:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def order_more(self, quantity):
        self.quantity += quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def sell_bouquet(self):
        if len(self.flowers) == 0:
            print("No flowers in the bouquet to sell.")
        else:
            for flower in self.flowers:
                print(f"Selling {flower.name}")
                flower.quantity -= 1
            self.flowers = []

    def __str__(self):
        if len(self.flowers) == 0:
            return "Empty Bouquet"
        else:
            return "Bouquet:\n" + "\n".join(str(flower) for flower in self.flowers)


# Flower Shop Ordering To Go
rose = Flower("Rose", 10)
lily = Flower("Lily", 5)
tulip = Flower("Tulip", 3)

flowers = [rose, lily, tulip]

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(lily)
bouquet.add_flower(tulip)

print("Flower Inventory:")
for flower in flowers:
    print(flower)

print("\nBouquet Inventory:")
print(bouquet)

bouquet.sell_bouquet()

print("\nFlower Inventory after selling a bouquet:")
for flower in flowers:
    print(flower)

rose.order_more(5)
lily.order_more(10)

print("\nUpdated Flower Inventory:")
for flower in flowers:
    print(flower)

print("\nUpdated Bouquet Inventory:")
print(bouquet)

bouquet.sell_bouquet()

print("\nFlower Inventory after selling an updated bouquet:")
for flower in flowers:
    print(flower)
