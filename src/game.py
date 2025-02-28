from .grid import Grid
from .player import Player
from .printer import print_status, print_inventory
from . import pickups



player = Player(17, 5)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
g.make_random_walls()
pickups.randomize(g)

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g, score)

    command = input("Use WASD to move, I for inventory and Q/X to quit. ")
    command = command.casefold()[:1]

    def move_player(dx, dy, command):
        global score
        maybe_item = None

        if command in ("w", "a", "d", "s") and player.can_move(dx, dy, g):
            maybe_item = g.get(player.pos_x + dx, player.pos_y + dy)
            player.move(dx, dy)
            score -= 1

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            inventory.append(maybe_item.name)
            g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)

    if command == "d": #move right
        move_player(1, 0, command)
    elif command == "a": #move left
        move_player(-1, 0, command)
    elif command == "w": #move up
        move_player(0, -1, command)
    elif command == "s": #move down
        move_player(0, 1, command)
    elif command == "i":
        print_inventory(g, inventory)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
