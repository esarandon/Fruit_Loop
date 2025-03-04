def print_status(game_grid, score):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)

def print_inventory(game_grid, inventory):
    print("--------------------------------------")
    print(f"You have collected: {inventory}")

def print_end_game(score):
    print("-------You won!-------")
    print(f"Total score: {score}")
    print("\nThank you for playing!")