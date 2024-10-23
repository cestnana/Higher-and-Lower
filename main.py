from game_data import data
import random

def choose_random_item():
  return random.choice(data)

def compare_items(item_a, item_b):
  return item_a['follower_count'] > item_b['follower_count']

def main():
  score = 0  # Initialize score
  item_a = choose_random_item()
  item_b = choose_random_item()
  print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
  print(f"Compare B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  is_correct = compare_items(item_a, item_b)
  print(is_correct)
  correct_answer = 'a' if compare_items(item_a, item_b) else 'b'
  is_correct = user_choice == correct_answer
  
  if is_correct:
    print("You're right!")
    score += 1
    print(f"Your current score: {score}")
  else:
    print(f"Sorry, that's wrong. {correct_answer.upper()} has more followers.")
  
  print(f"A: {item_a['name']} has {item_a['follower_count']} million followers.")
  print(f"B: {item_b['name']} has {item_b['follower_count']} million followers.")
  print(f"Final score: {score}")

main()