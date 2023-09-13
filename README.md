Tic-Tac-Toe with AI Opponent
Overview
This is a simple implementation of the classic Tic-Tac-Toe game where you can challenge an AI opponent. Using the Minimax algorithm, the AI aims to make the optimal move every time, ensuring a competitive gameplay experience.

Table of Contents
Disclaimer
Prerequisites
Installation
Gameplay Instructions
Code Structure
Contribution & Feedback
Disclaimer
The graphical user interface in this project was sourced externally and is essential for the gameplay experience. All credits for the GUI go to its respective authors.

Prerequisites
Python (Version 3.6 or later is recommended)
Pygame library
Installation
Ensure you have Python installed. You can verify with python --version in your terminal.

Install the Pygame library:

bash
Copy code
pip install pygame
Clone the repository or download the game files.

Navigate to the directory with the game files using your terminal or command prompt.

Gameplay Instructions
Launch the game by running:

bash
Copy code
python archivo1.py
The game window will appear. Choose your side: 'X' or 'O'.

Click on an empty tile to make your move.

Watch as the AI opponent calculates and makes its move.

The game ends once there's a winner or if the board is completely filled (tie).

You can opt to play again by clicking on the "Play Again" button.

Code Structure
archivo1.py:

Contains the GUI logic.
Handles the game loop and user interactions.
archivo2.py:

Defines the game's logic, including the board's initial state, valid actions, game result after an action, and checking for terminal states.
Implements the Minimax algorithm to determine the AI's best possible move.
Contribution & Feedback
Improvements, bug fixes, and suggestions are welcome! While the graphical component isn't originally mine, feel free to provide feedback or contribute to the game logic or AI algorithm. Open an issue or submit a pull request if you have something to add.
