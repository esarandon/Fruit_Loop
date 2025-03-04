from src.grid import Grid
from src.player import Player
from src.printer import print_status, print_inventory, print_end_game
from . import pickups


player = Player(17, 5)

g = Grid()
g.set_player(player)
g.make_walls()
g.make_random_walls()
g.set_traps(3)
pickups.randomize(g)

command = "a"

# Loopa tills användaren trycker Q eller X.
running = True

while running and player.running:
    print_status(g, player.score)

    command = input("Use WASD to move, I for inventory and Q/X to quit. ")
    command = command.casefold()[:1]

    if command in ["q", "x"]:
        running = False
    elif command == "d": #move right
        player.move_player(g, 1, 0, command)
    elif command == "a": #move left
        player.move_player(g, -1, 0, command)
    elif command == "w": #move up
        player.move_player(g, 0, -1, command)
    elif command == "s": #move down
        player.move_player(g, 0, 1, command)
    elif command == "i":
        print_inventory(g, player.inventory)



# Hit kommer vi när while-loopen slutar
print_end_game(player.score)
