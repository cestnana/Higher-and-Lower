from game_data import data  # Import the 'data' containing information about the items
import random # Import 'random' to select items randomly

def choose_random_item():
  # Select a random item from the data list
  return random.choice(data)

def compare_items(item_a, item_b):
  # Compare follower counts of two items and return True if item_a has more followers
  return item_a['follower_count'] > item_b['follower_count']

def main():
  score = 0  # Initialize score
  while True: # Infinite loop to keep the game running until the user quits
    item_a = choose_random_item()
    item_b = choose_random_item()
    # Display details of the two items for comparison
    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(f"Compare B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
    # Get the user's choice and convert it to lowercase
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = compare_items(item_a, item_b)
    # print(is_correct) # Test output
    # Determine the correct answer based on the follower count comparison
    correct_answer = 'a' if compare_items(item_a, item_b) else 'b'
    # Check if the user's choice matches the correct answer
    is_correct = user_choice == correct_answer
    
    if is_correct:
      # Inform the user they guessed correctly
      print("You're right!")
      score += 1
      print(f"Your current score: {score}")
    else:
      # Inform the user of the correct answer if they guessed wrong
      print(f"Sorry, that's wrong. {correct_answer.upper()} has more followers.")
      
        # Add a play again option
    if input("Play again? (y/n): ").lower() != 'y':
      break # Exit the loop and end the game
  
  # Display the follower counts of the last compared items
  print(f"A: {item_a['name']} has {item_a['follower_count']} million followers.")
  print(f"B: {item_b['name']} has {item_b['follower_count']} million followers.")
  # Print the final score after the game ends
  print(f"Final score: {score}")

# Run the main function to start the game
main()