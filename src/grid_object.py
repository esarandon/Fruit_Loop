class GridObject:
    """Base class for all objects in the grid"""
    def __init__(self, name, symbol=None, is_collectable=False):
        self.name = name
        self.symbol = symbol
        self.is_collectable = is_collectable

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', ´{self.symbol}"

    def __str__(self):
        return self.symbol