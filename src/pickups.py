from gi.overrides.keysyms import value

from src.grid_object import GridObject

class Item(GridObject):
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, symbol="?", value=20):
        super().__init__(name, symbol)
        self.value = value
        self.is_collectable=True


class Special_Item(GridObject):
    """Represent special items without value"""
    def __init__(self, name, symbol="?", value=0):
        super().__init__(name, symbol)
        self.value = value
        self.is_collectable = True

pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball")]
special_items = [Special_Item("key"), Special_Item("shovel"), Special_Item("chest")]


def randomize(grid):
    for item in pickups + special_items:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
