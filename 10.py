#!/usr/bin/env python3

from aocd.models import Puzzle
from pathlib import Path

def solve(data: str, part: int) -> int:
  lines = data.strip().splitlines()
  return -1

def main():
  puzzle = Puzzle(year=2025, day=int(Path(__file__).stem))

  example = """"""
  example_a_result = -7
  example_b_result = -8

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