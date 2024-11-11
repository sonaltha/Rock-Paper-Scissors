import random
# RPS_game.py

# Example of a simple bot (Quincy)
def quincy(prev_play: str) -> str:
    """Quincy always plays Rock."""
    return "R"

# Another bot: a random player
def random_bot(prev_play: str) -> str:
    """This bot plays randomly."""
    return random.choice(["R", "P", "S"])

# Function to simulate a match between two players
def play(player1, player2, num_games=1000, verbose=False):
    """
    Simulate a match between player1 and player2.
    Each player is a function that takes in the opponent's previous play and returns the next move.
    """
    # Initialize history of moves
    player1_history = []
    player2_history = []
    
    # Track wins, losses, ties
    player1_wins = 0
    player2_wins = 0
    ties = 0
    
    for game in range(num_games):
        # Get moves for both players based on previous history (or no history for the first round)
        move1 = player1(prev_play=player2_history[-1] if player2_history else "")
        move2 = player2(prev_play=player1_history[-1] if player1_history else "")
        
        # Determine the winner of this round
        if move1 == move2:
            ties += 1
        elif (move1 == "R" and move2 == "S") or (move1 == "P" and move2 == "R") or (move1 == "S" and move2 == "P"):
            player1_wins += 1
        else:
            player2_wins += 1
        
        # Add moves to history
        player1_history.append(move1)
        player2_history.append(move2)
        
        # Optionally print the results of the game
        if verbose:
            print(f"Game {game + 1}: Player 1: {move1}, Player 2: {move2}")
    
    # Return the results as a dictionary
    return {
        "player1_wins": player1_wins,
        "player2_wins": player2_wins,
        "ties": ties
    }

