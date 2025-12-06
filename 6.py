#!/usr/bin/env python3

from aocd.models import Puzzle
from pathlib import Path

def solve_a(data: str) -> int:
    lines = data.strip().splitlines()
    def line_processor(line: str) -> list[int]:
        return [int(x) for x in line.split()]
    operands = [line_processor(line) for line in lines[:-1]]
    operators = [c for c in lines[-1].split()]
    expression_count = len(operators)
    operand_count = len(operands)

    total = 0
    for i in range(expression_count):
        op = operators[i]
        if op == '+':
          v = 0
          for j in range(operand_count):
            v += operands[j][i]
          total += v
        elif op == '*':
          v = 1
          for j in range(operand_count):
            v *= operands[j][i]
          total += v
    return total

def transpose(grid: list[str]) -> list[str]:
  source_width = len(grid[0])
  source_height = len(grid)
  dest_width = source_height
  dest_height = source_width
  new_grid = []
  for source_x in range(source_width):
    s = ""
    for source_y in range(source_height):
      s += grid[source_y][source_x]
    new_grid.append(s)
  return new_grid
    

def solve_b(data: str) -> int:
    lines = data.split('\n')
    operators = lines[-1].split()
    operand_grid = lines[:-1]
    operand_grid = transpose(operand_grid)
    operands = [int(line) for line in operand_grid if line.strip() != '']
    operand_count = (len(operand_grid) - len(operators) + 1) // len(operators)
    expression_count = len(operators)
    total = 0
    for i in range(expression_count):
        op = operators[i]
        if op == '+':
          v = 0
          for j in range(operand_count):
            v += operands[i * operand_count + j]
          total += v
        elif op == '*':
          v = 1
          for j in range(operand_count):
            v *= operands[i * operand_count + j]
          total += v
    return total

def main():
  puzzle = Puzzle(year=2025, day=int(Path(__file__).stem))

  example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +   """
  v = solve_a(example)
  print(v)
  assert(v == 4277556)
  data = puzzle.input_data
  v = solve_a(data)
  print(v)
  puzzle.answer_a = v

  v = solve_b(example)
  print(v)
  assert(v == 3263827)
  data = puzzle.input_data
  v = solve_b(data)
  print(v)
  puzzle.answer_b = v

if __name__ == "__main__":
    main()