class ItemType:
    def __init__(self, name:str, price:float,quantity:int) -> None:
        """
        Initialize an item with the given name, price, and quantity.
        """
        if price <= 0:
            raise ItemError(f"Item price must be greater than zero: {name}")
        if not isinstance(name, str):
            raise ItemError(f"Item name must be a string: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.unlocked = True
    def __lt__(self, value):
        if isinstance(value, ItemType):
            return self.price < value.price 
        return False
    def __eq__(self, value):
        if isinstance(value, ItemType):
            return self.name == value.name 
        return False
    def __repr__(self) -> str:
        return f"name: {self.name} -  price: {self.price} -  quantity: {self.quantity} - status: {self.unlocked}"
class Inventory: 
    def __init__(self,stock:list[ItemType]) -> None:
        self.stock = stock
    def validate_items(self,items:list[ItemType]):
        """
        Validate that all items in the given list are in stock and unlocked.
        Raises an InventoryError if any item is not in stock, or if any item is locked.
        """
        for item in items:
            if not isinstance(item,ItemType):
                raise InventoryError(f"Invalid item type: {item}")
            if item.quantity == 0:
                raise InventoryError(f"Item out of stock: {item}")
            if not item.unlocked:
                raise InventoryError(f"Item is locked: {item}")
    def lock(self,item_type:ItemType) ->None:
        for item in self.stock:
            if item == item_type :
                if not item.unlocked:
                    raise InventoryError(f"Item already locked: {item}")
                item.unlocked = False
                return "Item locked successfully"
        raise InventoryError(f"Item not found in stock: {item_type}")
    def unlock(self,item_type:ItemType) ->None:
        for item in self.stock:
            if item == item_type:
                if item.unlocked:
                    raise InventoryError(f"Item already unlocked: {item}")
                item.unlocked = True
                return "Item unlocked successfully"
        raise InventoryError(f"Item not found in stock: {item_type}")
    def purchase(self,item_type:ItemType) ->None:
        for item in self.stock:
            if item == item_type:
                self.validate_items([item])
                item.quantity -= 1
                return "Item purchased successfully"
            raise InventoryError (f" Item not found in stock: {item_type}")
class InventoryError(Exception):
    pass
class ItemError(ValueError):
    pass
try:
    stock = [
        ItemType("item1", 10.0, 5),
        ItemType("item2", 15.0, 1),
        ItemType("item3", 20.0, 3)
    ]
    inventory = Inventory(stock)
    inventory.lock(stock[0])
    inventory.purchase(stock[2])
    inventory.unlock(stock[0])
    inventory.purchase(stock[1])
    inventory.purchase(stock[1])
except InventoryError as e:
    print(f"Inventory error: {e}")

    