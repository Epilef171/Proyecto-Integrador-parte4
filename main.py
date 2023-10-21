import os
import keyboard
import time
from typing import List, Tuple

def generate_maze(maze_str: str) -> List[List[str]]:
    return [list(row) for row in maze_str.strip().split("\n")]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_matrix(maze: List[List[str]]):
    clear_screen()
    for row in maze:
        print("".join(row))

def main_loop(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]):
    px, py = start
    end_x, end_y = end

    while True:
        maze[py][px] = 'P'
        display_matrix(maze)

        key = None
        while key is None:
            for direction in ['left', 'right', 'up', 'down']:
                if keyboard.is_pressed(direction):
                    key = direction

        maze[py][px] = '.'
        if key == 'left' and px > 0 and maze[py][px - 1] != '#':
            px -= 1
        elif key == 'right' and px < len(maze[0]) - 1 and maze[py][px + 1] != '#':
            px += 1
        elif key == 'up' and py > 0 and maze[py - 1][px] != '#':
            py -= 1
        elif key == 'down' and py < len(maze) - 1 and maze[py + 1][px] != '#':
            py += 1

        if (px, py) == (end_x, end_y):
            print("¡Has llegado al final!")
            break

        time.sleep(0.2)  # Espera corta para evitar movimientos rápidos

if __name__ == "__main__":
    maze_str = """..###################
#...................#
#.###.#.###.#.#######
#...#.#...#.#.....#.#
#########.#.#.#.#.#.#
#.#.#.....#.#.#.#...#
#.#.###.###.###.#.###
#.......#...#.#.#.#.#
###.###.#####.#####.#
#.#...#.............#
#.#.###.###########.#
#.....#.....#.....#.#
#.###.###.###.###.#.#
#.#.#...#...#...#...#
#.#.#############.###
#.#.......#.........#
#.#.#.###.###.#.###.#
#.#.#...#...#.#.#...#
###.###.###.###.#.###
#.....#...#.....#.###
#################...."""

    maze_matrix = generate_maze(maze_str)
    
    start_position = (0, 0)
    end_position = (21, 21)

    main_loop(maze_matrix, start_position, end_position)
