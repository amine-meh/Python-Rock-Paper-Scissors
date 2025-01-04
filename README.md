# Rock Paper Scissors Game

Welcome to the **Rock Paper Scissors** game, a classic hand game reimagined in Python! This project lets you play an interactive match of Rock, Paper, Scissors against a computer opponent.

## Features

- Play the traditional Rock, Paper, Scissors game.
- Dynamic opponent with random choices.
- Keep track of wins, losses, and ties.
- Option to quit anytime by entering 'Q'.

## How It Works

1. When you start the program, you'll be welcomed to the game.
2. You'll be prompted to choose one of the following:
   - `Rock`
   - `Scissors`
   - `Paper`
   - `Q` to quit the game.
3. The computer will randomly pick its option.
4. The game determines the winner based on the rules:
   - Rock beats Scissors
   - Scissors beat Paper
   - Paper beats Rock
5. The game announces the result and updates the scores.
6. Once you quit, the final scores are displayed.

## Installation

1. Ensure you have Python installed on your system (Python 3.6+ recommended).
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors.git
3. Navigate to the project directory:
   ```bash
   cd rock-paper-scissors

## Code Breakdown

- Random Choice for Computer:
    The computer's choice is generated randomly using the random.randint() method.
- Game Logic:
    Nested if-else conditions determine the winner based on player and computer choices.
- Tracking Scores:
    Variables user_wins, computer_wins, and ties keep track of the game outcomes.

  ## Contributing

  Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

  ## Possible Improvements

  - Add support for extended choices (e.g., "Lizard" and "Spock").
  - Implement a graphical user interface (GUI).
  - Allow users to set the number of rounds.
  - Include multiplayer support.
 
  ## License

  This project is licensed under the MIT License. See the LICENSE file for details.

  ### Have fun playing Rock Paper Scissors!
