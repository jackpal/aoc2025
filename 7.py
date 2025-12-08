#!/usr/bin/env python3

from aocd.models import Puzzle
from pathlib import Path
from collections import Counter

def solve_a(data: str) -> int:
  return solve(data, 1)

def solve_b(data: str) -> int:
  return solve(data, 2)

def solve(data: str, part: int) -> int:
    lines = data.strip().splitlines()
    width = len(lines[0])
    height = len(lines)
    start = lines[0].index('S')
    beams = Counter()
    beams[start] = 1
    if part == 1:
      result = 0
    else:
      result = 1
    for line in lines[1:]:
      new_beams = Counter()
      for i,c in beams.items():
        if line[i] == '^':
          assert(0 < i < width-1)
          if part == 1:
            result += 1
          else:
            result += c
          new_beams[i-1] += c
          new_beams[i+1] += c
        else:
          new_beams[i] += c
      beams = new_beams
    return result

def main():
  puzzle = Puzzle(year=2025, day=int(Path(__file__).stem))

  example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
  v = solve_a(example)
  print(v)
  assert(v == 21)
  data = puzzle.input_data
  v = solve_a(data)
  print(v)
  puzzle.answer_a = v

  v = solve_b(example)
  print(v)
  assert(v == 40)
  data = puzzle.input_data
  v = solve_b(data)
  print(v)
  puzzle.answer_b = v

if __name__ == "__main__":
    main()