import random

# Sample list of words to use in the game
words = ["elephant", "cat", "house", "mountain", "river", "airplane", "butterfly"]

def get_word():
  """Get a random word from the list."""
  return random.choice(words)

def play_game():
  score = 0
  current_word = get_word()

  while True:
    print(f"Current word: {current_word} (Length: {len(current_word)})")
    
    next_word = get_word()
    guess = input(f"Is the next word '{next_word}' higher or lower in length? (h/l): ").lower()

    if (guess == 'h' and len(next_word) > len(current_word)) or \
       (guess == 'l' and len(next_word) < len(current_word)):
      score += 1
      print("Correct! Your score:", score)
      current_word = next_word  # Move to the next word
    else:
      print(f"Wrong! Final score: {score}")
      break

# Start the game
play_game()