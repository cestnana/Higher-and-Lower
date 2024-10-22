from game_data import data
import random

def choose_random_item():
  return random.choice(data)

def compare_items(item_a, item_b):
  return item_a['follower_count'] > item_b['follower_count']

def main():
  item_a = choose_random_item()
  item_b = choose_random_item()
  print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
  print(f"Compare B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  is_correct = compare_items(item_a, item_b)
  print(is_correct)
  

main()