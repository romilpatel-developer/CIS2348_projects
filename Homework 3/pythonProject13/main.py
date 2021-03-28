# Name- Romilkumar Patel
# PSID_ 1765483

class ItemToPurchase:
    # default costructor
    def __init__(self):
        # attributes
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    # method
    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(
            self.item_price * self.item_quantity))


if __name__ == "__main__":
    # prompt user for two items
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    # prompt item 2
    print("\nItem 2")
    item2 = ItemToPurchase()
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    # print info
    total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    print("\nTotal: $" + str(total_cost))