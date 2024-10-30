from game_data import data  # Import the 'data' containing information about the items
import random # Import 'random' to select items randomly

def choose_random_item():
  # Select a random item from the data list
  return random.choice(data)

def compare_items(item_a, item_b):
  # Compare follower counts of two items and return True if item_a has more followers
  return item_a['follower_count'] > item_b['follower_count']
  # What if the follower counts are equal?

# Main function to run the game
def main():
  score = 0  # Initialize score
  while True:  # Infinite loop to keep the game running until the user quits
    item_a = choose_random_item()
    item_b = choose_random_item()
    
    # Ensure item_b is different from item_a
    while item_a == item_b:
      item_b = choose_random_item()
    
    # Display details of the two items for comparison
    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(f"Compare B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
    
    # Get the user's choice with input validation
    while True:
      user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
      if user_choice in ['a', 'b']:
        break
      else:
        print("Invalid input. Please enter 'A' or 'B'.")
    
    # Determine the correct answer based on the follower count comparison
    correct_answer = 'a' if compare_items(item_a, item_b) else 'b'
    # Check if the user's choice matches the correct answer
    is_correct = user_choice == correct_answer
    
    if is_correct:
      # Inform the user they guessed correctly
      print("You're right!")
      score += 1
      print(f"Your current score: {score}")
      continue  # Skip the play again prompt and continue to next round
    else:
      # Inform the user of the correct answer if they guessed wrong
      print(f"Sorry, that's wrong. {correct_answer.upper()} has more followers.")
      print(f"Game Over! Your final score: {score}")
      score = 0  # Reset score when wrong
      
      # Add a play again option with input validation (only when wrong)
      while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again in ['y', 'n']:
          break
        else:
          print("Invalid input. Please enter 'y' or 'n'.")
      
      if play_again != 'y':
        break  # Exit the loop and end the game
  
  # Display the follower counts of the last compared items
  print(f"A: {item_a['name']} has {item_a['follower_count']} million followers.")
  print(f"B: {item_b['name']} has {item_b['follower_count']} million followers.")
  # Print the final score after the game ends
  # print(f"Final score: {score}")

# Run the main function to start the game
main()
