import random
from src.grid_object import GridObject
from src.pickups import Item


class Cell(GridObject):
    """To avoid issues with objects with similar symbols, a Cell class was created"""
    def __init__ (self, name, symbol):
        super().__init__(name=name, symbol=symbol)

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.name == other.name # Compare by type, not object reference
        return False

    def __repr__(self):
        return f"Cell(´{self.symbol}', '{self.name}')"


class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."

    def __init__(self):
        """Skapa ett objekt av klassen Cell"""
        self.cell_types= {
            "wall": Cell("wall", "■"),
            "special_wall": Cell("special_wall", "■"),
            "trap": Cell("trap", "."),
            "exit": Cell("exit", "E"),
        }

        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(self.height)]

    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x]) #The cell object can be use directly
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.cell_types["wall"])
            self.set(self.width - 1, i, self.cell_types["wall"])

        for j in range(1, self.width - 1):
            self.set(j, 0, self.cell_types["wall"])
            self.set(j, self.height - 1, self.cell_types["wall"])


    def make_random_walls(self):
        """Skapa ett random antal av väggar i spelplanen"""
        wall_amount = random.randint(1, 5)  # Random amount of walls

        for x in range(wall_amount):
            random_x = self.get_random_x()
            random_y = self.get_random_y()

            # Avoid building a wall over players position
            if(random_x, random_y) == (self.player.pos_x, self.player.pos_y):
                continue

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # define all four directions to build the wall
            dx, dy = random.choice(directions) # select a random direction
            wall_length = random.randint(1, 5) #Random length of wall

            for i in range(wall_length):
                new_x = random_x + i * dx
                new_y = random_y + i * dy

                # if still inside boundaries, place a wall
                if 1 <= new_x < self.width -1 and 1 <= new_y < self.height -1:
                    self.set(new_x, new_y, self.cell_types["special_wall"])
                else:
                    break

    def set_traps(self, traps_number):
        for trap in range(traps_number):
            while True:
                # slumpa en position tills vi hittar en som är ledig
                x = self.get_random_x()
                y = self.get_random_y()
                if self.is_empty(x, y):
                    self.set(x, y, self.cell_types["trap"])
                    break

    def set_exit(self):
        x = self.get_random_x()
        y = self.get_random_y()
        if self.is_empty(x, y):
            self.set(x, y, self.cell_types["exit"])

    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width - 1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height - 1)

    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

    def no_items_left(self):
        """Returns True if no more items in the grid"""
        for x in range(self.width):
            for y in range(self.height):
                if isinstance(self.get(x, y), Item):
                    return False
        return True
