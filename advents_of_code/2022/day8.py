from pprint import pprint


def read_grid(filename):
    grid = []
    with open(filename) as inp_file:
        for line in inp_file:
            grid.append(list(line.strip()))
    return grid


def visible_tree(grid, coord, direction):

    while True:
        new_coords = (coord[0] + direction[0], coord[1] + direction[1])
        if new_coords[0] < 0 or new_coords[0] >= len(grid) or new_coords[1] < 0 or new_coords[1] >= len(grid[0]):
            return
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= len(grid) or coord[1] >= len(grid[1]):
            yield new_coords
            coord = new_coords
            highest_tree = grid[new_coords[0]][new_coords[1]]
        else:
            if grid[new_coords[0]][new_coords[1]] > highest_tree:
                yield new_coords
                highest_tree = grid[new_coords[0]][new_coords[1]]
            coord = new_coords


def main():
    grid = read_grid("day8.txt")
    all_trees = set()
    for x in range(len(grid[0])):
        for tree in visible_tree(grid, (-1, x), (1, 0)):
            all_trees.add(tree)
        for tree in visible_tree(grid, (len(grid), x), (-1, 0)):
            all_trees.add(tree)
    for y in range(len(grid)):
        for tree in visible_tree(grid, (y, -1), (0, 1)):
            all_trees.add(tree)
        for tree in visible_tree(grid, (y, len(grid[0])), (0, -1)):
            all_trees.add(tree)
    edges = set([t for t in all_trees
                  if t[0] == 0 or t[1] == 0 or t[1] == len(grid[0]) - 1 or t[0] == len(grid) - 1
                  ])
    non_edges = all_trees - edges
    return len(all_trees)


def main2():
    grid = read_grid("day8.txt")
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            tree_size = grid[row][col]
            score = 1
            for dir_ in dirs:
                counter = 0
                new_c = col
                new_r = row
                while True:
                    new_r = new_r + dir_[0]
                    new_c = new_c + dir_[1]
                    if new_c < 0 or new_c == len(grid[0]):
                        break
                    if new_r < 0 or new_r == len(grid):
                        break
                    counter += 1
                    if grid[new_c][new_r] >= tree_size:
                        break

                score *= counter

            if score > max_score:
                max_score = score
                print(f"Tree: {row}, {col}: score {score}")

    return max_score




def test_main():
    assert main() == 21

def test_main2():
    assert main2() == 8

def max_scenic_score(grid):
  rows = len(grid)
  cols = len(grid[0])

  # Initialize the maximum scenic score to 0
  max_score = 0

  for i in range(rows):
    for j in range(cols):
      # Initialize the scenic score for the current tree to 1
      total_score = 1

      score = 0
      # Look up from the current tree
      for k in range(i-1, -1, -1):
        score += 1
        if grid[k][j] >= grid[i][j]:
          break

      total_score *= score

      score = 0
      # Look down from the current tree
      for k in range(i+1, rows):
        score += 1
        if grid[k][j] >= grid[i][j]:
          break
      total_score *= score

      score = 0
      # Look left from the current tree
      for k in range(j-1, -1, -1):
        score += 1
        if grid[i][k] >= grid[i][j]:
          break

      total_score *= score

      score = 0
      # Look right from the current tree
      for k in range(j+1, cols):
        score += 1
        if grid[i][k] >= grid[i][j]:
          break

      total_score *= score

      # Update the maximum scenic score
      max_score = max(max_score, total_score)

  return max_score

def test_scenic_score():
    # Test the function with the example from the problem statement
    grid = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 3], [3, 3, 5, 4, 5], [3, 5, 3, 9, 0]]
    grid = read_grid("day8.txt")
    assert max_scenic_score(grid) == 8  # Expected output: 8
