#!/usr/bin/env python3

from aocd.models import Puzzle
from pathlib import Path

def solve(data: str, part: int) -> int:
  lines = data.strip().splitlines()
  tiles = [tuple(map(int, line.split(','))) for line in lines]
  def area(ax: int, ay: int, bx: int, by: int) -> int:
    return abs(ax-bx+1) * abs(ay-by+1)
  if part == 1:
    return max(area(a[0], a[1], b[0], b[1]) for a in tiles for b in tiles)
  elif part == 2:
    x0, x1, y0, y1 = (min(a[0] for a in tiles), max(a[0] for a in tiles), min(a[1] for a in tiles), max(a[1] for a in tiles))
    # dialate so flood fill works
    x0 -= 1
    x1 += 2
    y0 -= 1
    y1 += 2
    def arange(start: int, stop: int) -> iterator[int]:
      if start <= stop:
        return range(start, stop+1)
      else:
        return arange(stop, start)

    def flood(grid: list[list[str]], x: int, y: int, src: str, dst: str):
      active = set(((x, y),))
      while active:
        x, y = active.pop()
        if not (x0 <= x < x1 and y0 <= y < y1):
          continue
        if grid[x-x0][y-y0] != src:
          continue
        grid[x-x0][y-y0] = dst
        active.add((x+1, y))
        active.add((x-1, y))
        active.add((x, y+1))
        active.add((x, y-1))
    
    def show(grid: list[list[str]]):
      for row in grid:
        print(''.join(row))
    
    def check(grid: list[list[str]], ax: int, ay: int, bx: int, by: int) -> int:
      for x in arange(ax, bx):
        for y in arange(ay, by):
          if grid[x-x0][y-y0] == ' ':
            return -1
      return area(ax, ay, bx, by)
    
    grid = [['.'] * (y1 - y0) for _ in range(x1 - x0)]
    prev = tiles[-1]
    for x, y in tiles:
      xp, yp = prev
      for xx in arange(xp, x):
        grid[xx - x0][yp - y0] = 'g'
      for yy in arange(yp, y):
        grid[x - x0][yy - y0] = 'g'
      prev = (x, y)
    # show(grid)
    # print()
    flood(grid, x0, y0, '.', ' ')
    # show(grid)
    best = 0
    for i,(ax, ay) in enumerate(tiles):
      for bx, by in tiles[i+1:]:
        if ax == bx and ay == by:
          continue
        best = max(best, check(grid, ax, ay, bx, by))
    return best

def main():
  puzzle = Puzzle(year=2025, day=int(Path(__file__).stem))

  example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
  example_a_result = 50
  example_b_result = 24

  v = solve(example, 1)
  print("Example A:", v)
  assert(v == example_a_result)
  data = puzzle.input_data
  v = solve(data, 1)
  print("Part A:", v)
  puzzle.answer_a = v

  v = solve(example, 2)
  print("Example B:", v)
  assert(v == example_b_result)
  data = puzzle.input_data
  v = solve(data, 2)
  print("Part B:", v)
  puzzle.answer_b = v

if __name__ == "__main__":
    main()