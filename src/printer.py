# TODO: flytta denna till en annan fil
def print_status(game_grid, score):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)

def print_inventory(game_grid, inventory):
    print("--------------------------------------")
    print(f"You have collected: {inventory}")
