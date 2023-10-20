import os
from typing import List, Tuple

def generate_maze(maze_str: str) -> List[List[str]]:
    return [list(row) for row in maze_str.strip().split("\n")]

def string_to_matrix(maze_str: str, end: int) -> List[List[str]]:
    maze_rows = maze_str.strip().split("\n")
    maze_matrix = [list(row) for row in maze_rows]
    for row in maze_matrix:
        while len(row) < end:
            row.append('#')
    return maze_matrix

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_matrix(maze: List[List[str]]):
    clear_screen()
    for row in maze:
        print("".join(row))

def main_loop(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]):
    px, py = start

    while (px, py) != end:
        maze[py][px] = 'P'
        display_matrix(maze)

        key = input("Presiona una tecla de flecha (Arriba, Abajo, Izquierda, Derecha): ").lower()

        if key == "w" and py > 0 and maze[py - 1][px] != '#':
            maze[py][px], py = '.', py - 1
        elif key == "s" and py < len(maze) - 1 and maze[py + 1][px] != '#':
            maze[py][px], py = '.', py + 1
        elif key == "a" and px > 0 and maze[py][px - 1] != '#':
            maze[py][px], px = '.', px - 1
        elif key == "d" and px < len(maze[0]) - 1 and maze[py][px + 1] != '#':
            maze[py][px], px = '.', px + 1

if __name__ == "__main__":
    maze_str = """..###################
....................#
###.###.#####.#####.#
#...#...#.#.#.#.....#
#####.#.#.#.#.#.###.#
#.....#.#...#.#...#.#
#.###.#.###.#.#####.#
#.#...#.#.#...#.....#
#.#######.#.#########
#.....#...........#.#
###.#####.#####.###.#
#.#.#.#.......#.#...#
#.#.#.###.#.#######.#
#.......#.#.#.......#
###.#.#####.#.#.###.#
#...#.....#...#.#.#.#
#.###########.#.#.###
#.........#...#.#.#.#
#.#.#.#####.#.###.#.#
#.#.#...#...#.......
###################."""

    maze_matrix = generate_maze(maze_str)
    
    start_position = (0, 0)
    end_position = (22, 21)

    main_loop(maze_matrix, start_position, end_position)
