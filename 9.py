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
    def arange(start: int, stop: int) -> iterator[int]:
      if start <= stop:
        return range(start, stop+1)
      else:
        return arange(stop, start)

    # Compressed grid
    xs = sorted(set(a[0] for a in tiles))
    ys = sorted(set(a[1] for a in tiles))
    grid = [[0] * len(ys) for _ in xs]
    prev_ix = xs.index(tiles[-1][0])
    prev_iy = ys.index(tiles[-1][1])
    for x, y in tiles:
      curr_ix = xs.index(x)
      curr_iy = ys.index(y)
      if curr_ix != prev_ix:
        for xx in arange(prev_ix, curr_ix):
          grid[xx][curr_iy] = 1
      elif curr_iy != prev_iy:
        for yy in arange(prev_iy, curr_iy):
          grid[curr_ix][yy] = 1
      prev_ix = curr_ix
      prev_iy = curr_iy
    
    def check(ax: int, ay: int, bx: int, by: int) -> bool:
      a_ix = xs.index(ax)
      a_iy = ys.index(ay)
      b_ix = xs.index(bx)
      b_iy = ys.index(by)
      for ix in arange(a_ix, b_ix):
        for iy in arange(a_iy, b_iy):
          if grid[ix][iy] == 0:
            return False
      return True
    
    best = 0
    for i,(ax, ay) in enumerate(tiles):
      for bx, by in tiles[i+1:]:
        if ax == bx and ay == by:
          continue
        if check(ax, ay, bx, by):
          best = max(best, area(ax, ay, bx, by))
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