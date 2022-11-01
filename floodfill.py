# code to implement Floodfill

from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]



def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.

    if (input_board[x][y] == old):
        
        # since strings are immutable in python, I used slicing to edit the string in the board
        input_board[x] = input_board[x][0:y] + new + input_board[x][y+1:]
        flood_fill(input_board, old, new, x+1, y) # down
        flood_fill(input_board, old, new, x-1, y) # up
        flood_fill(input_board, old, new, x, y+1) # right
        flood_fill(input_board, old, new, x, y-1) # left
    
    if input_board == None or input_board[x][y] == new:
        return input_board
    
    elif( (x<0) or (x >= len(input_board[x])) or (y < 0) or (y >= len(input_board[0])) or input_board[x][y] != old ):
        return input_board

        
    
modified_board = flood_fill(input_board=board, old=".", new="M", x=5, y=12)
print("\n")

for a in modified_board:
    print(a)
    

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....
