# app.py

from flask import Flask, render_template, jsonify
import random

print("hello")

app = Flask(__name__, static_folder='templates')
# app = Flask(__name__)

GRID_SIZE = 4

# Initialize the grid and add a new tile
def initialize_grid(grid_size):
    return [[0 for _ in range(grid_size)] for _ in range(grid_size)]

def add_new_tile(grid):
    # Find all empty cells
    empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]
    if empty_cells:
        # Choose a random empty cell
        i, j = random.choice(empty_cells)
        # Place a new tile (either 2 or 4) in the chosen cell
        grid[i][j] = random.choice([2, 4])
    return grid

grid = initialize_grid(GRID_SIZE)
grid_with_new_tile = add_new_tile(grid)

@app.route('/')
def index():
    return render_template('index.html', grid=grid_with_new_tile)

@app.route('/move/<direction>')
def move(direction):
    # Implement the logic for moving the tiles in the specified direction
    # Update the grid with the new position of the tiles after the move
    # Return the updated grid as JSON
    updated_grid = [[0, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # Placeholder for the updated grid
    return jsonify(updated_grid)

if __name__ == '__main__':
    app.run(debug=True)