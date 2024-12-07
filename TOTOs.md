# TODOs for Higher and Lower Game

## Core Game Logic
- [x] Create a data structure to store items with their rates/values
- [x] Implement function to randomly select two items for comparison
- [x] Display choice A and choice B to the user
- [x] Implement user input for selecting between A and B
- [x] Compare user's choice with the correct answer (higher rate/value)
- [x] Provide feedback on whether the user's choice was correct
- [x] Implement game loop (continue with correct choice becoming new A)
- [x] Track user's score (consecutive correct answers)

## Basic Features
- [x] Initialize the game with a set of items and their rates/values
- [x] Implement game over condition (when user makes an incorrect choice)
- [x] Display final score at the end of the game

## Error Handling
- [x] Validate user input (ensure it's a valid choice: A or B)
- [x] Handle invalid inputs gracefully

## Game Flow
- [x] Create a game start function
- [x] Implement a game over function
- [x] Add option to play again or quit

## Data Management
- [x] Create a function to load items and their rates from a file or database
- [x] Ensure there are enough unique items for extended game-play

## Testing
- [x] Test the item selection logic
- [x] Verify correct comparison of rates/values
- [x] Ensure proper game flow (start to finish)

## Enhancements (After core logic is working)
- [?] Implement a high score system
- [?] Add categories for items (e.g., countries by population, movies by box office)
- [?] Create difficulty levels (e.g., more obscure items, closer rate/value differences)
- [?] Add a time limit for each choice

## Documentation
- [x] Add comments to explain core logic functions
- [x] Create a basic README with game instructions and rules

## User Interface
- [x] Improve the display of choices (possibly add visual elements)
- [x] Show additional information about items after each round

