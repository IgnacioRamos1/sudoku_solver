# Sudoku Solver

This Sudoku solver project represents a personal challenge to tackle a complex problem without relying on established solutions or guides.

Starting from scratch, I began by dissecting the Sudoku board, breaking it down into manageable pieces and rigorously validating each row, column, and 3x3 square against the game's rules.

Once the validation was complete, I ventured into the solving phase. Using recursion and innovative strategies, I approached each empty cell, methodically filling them with valid numbers without external assistance.

As I refined the solver, it grew more adept, employing techniques to identify obvious moves and deduce numbers based on patterns within the board. This process mirrored my own journey of learning and adaptation.

## Recursion algorithm
As I continued to develop the Sudoku solver, I encountered the concept of recursion. Initially intimidating, recursion soon became a powerful tool in my arsenal. With recursion, I rewrote the solver, making it more elegant and efficient.

This new approach allowed the solver to explore every possible solution methodically. By recursively diving deeper into the puzzle and backtracking when necessary, it could systematically solve even the most challenging Sudoku grids.

### Considerations
If you want to test the Solver for your self make sure to:

- Have numpy installed (for the recursion algorithm):
`pip install numpy`

- Get the Sudokus from: (Make sure to select the one-line output format)
[Sudokus QQWing](https://qqwing.com/generate.html)
