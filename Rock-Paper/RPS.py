import random

# Your main player function
def player(prev_play: str) -> str:
    """
    Returns the next move for the player based on the opponent's previous move.
    """
    # If this is the first round (prev_play is empty), choose a random move
    if prev_play == "":
        return random.choice(["R", "P", "S"])
    
    # If not the first round, counter the opponent's last move
    if prev_play == "R":
        return "P"  # Paper beats Rock
    elif prev_play == "P":
        return "S"  # Scissors beats Paper
    elif prev_play == "S":
        return "R"  # Rock beats Scissors
