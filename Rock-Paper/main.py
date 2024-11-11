# main.py

from RPS_game import play, quincy, random_bot  # Import the play function and bots from RPS_game
from RPS import player  # Import your player function from RPS.py

# Play 1000 games between 'player' (your bot) and 'quincy', and show the results of each game
result = play(player, quincy, 1000, verbose=True)

# Print the final results
print("Results of the match:")
print(f"Player 1 (your bot) wins: {result['player1_wins']}")
print(f"Player 2 (Quincy) wins: {result['player2_wins']}")
print(f"Ties: {result['ties']}")
