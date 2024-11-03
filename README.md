# Higher or Lower Game

A command-line game where players guess which of two items has more social media followers.

## Description

This game challenges players to compare two randomly selected items and guess which one has more followers. Players earn points for correct guesses and continue playing until they make a wrong guess.

## Features

- Random selection of items to compare
- Score tracking
- Continuous gameplay with the option to play again
- Input validation for user choices
- Detailed comparison display showing item descriptions and countries

## How to Play

1. Run the game using Python:
   ```bash
   python main.py
   ```

2. For each round:
   - You'll see two items (A and B) with their descriptions
   - Type 'A' or 'B' to guess which has more followers
   - If correct, your score increases and you continue to the next round
   - If wrong, the game ends and you can choose to play again

## Requirements

- Python 3.x
- `game_data.py` file containing the items data

## Data Structure

The game expects `game_data.py` to contain a list of dictionaries with the following structure: