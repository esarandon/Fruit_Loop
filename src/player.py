from . import pickups

class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.inventory = []
        self.score = 0
        self.grace_step = 0
        self.running = True

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        # TODO: returnera True om det inte står något i vägen
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy
        target_cell = grid.get(new_x, new_y)

        if target_cell == grid.cell_types["wall"]:
            return False

        if target_cell == grid.cell_types["special_wall"]:
            if "shovel" in self.inventory:
                grid.clear(new_x, new_y)
            else:
                return False

        if target_cell == grid.cell_types["exit"]:
            grid.set(self.pos_x, self.pos_y, grid.empty)
            self.running = False

        if target_cell == grid.cell_types["trap"]:
            self.score -= 10
            """Once a trap has been discovered, all traps will show in the grid but still work"""
            grid.cell_types["trap"].symbol = "X"
            grid.set(new_x, new_y, grid.cell_types["trap"])
            print("You fell into a trap! You lose 10 points")

        return True

    def move_player(self, g, dx, dy, command):
        maybe_item = None

        if command in ("w", "a", "d", "s") and self.can_move(dx, dy, g):
            maybe_item = g.get(self.pos_x + dx, self.pos_y + dy)
            self.move(dx, dy)
            if self.grace_step != 0:
                self.grace_step -= 1
            else:
                self.score -= 1

        if isinstance(maybe_item, (pickups.Item, pickups.Special_Item))\
                :
          self.handle_item(maybe_item, g)

    def check_chest(self, item, g):
        """Cheks if the player can open the chest"""
        if item.name == "chest":
            if "key" in self.inventory:
                print("You have a key, opening chest. +100 point!")
                self.score += 100
                self.inventory.remove("key")
                g.set(self.pos_x, self.pos_y, g.empty)  # Remove opened chest from grid
                g.clear(self.pos_x, self.pos_y)
            else:
                print("You need a key to open the chest")
                return False
        return True

    def handle_item(self, item, g):
        """Handles what happens when the player finds an item"""
        if isinstance(item, pickups.Special_Item):
            print(f"You found a special item: {item.name}")
            if item.name == "chest":
                if not self.check_chest(item, g):
                    return
            else:
                """If special_item but not chest, collect item"""
                self.inventory.append(item.name)
                self.grace_step = 5
        else:
            # Handle regular item
            self.score += item.value
            print(f"You found a {item.name}, +{item.value} points.")
            self.inventory.append(item.name)
            self.grace_step = 5

        if item.name != "chest":
            # Remove item from grid, unless is a chest
            g.set(self.pos_x, self.pos_y, g.empty)
            g.clear(self.pos_x, self.pos_y)
            # Test if all items have been picked:
            if self.end_game(g):
                g.set_exit()

    def end_game(self, g):
        if g.no_items_left():
            return True
        return False
