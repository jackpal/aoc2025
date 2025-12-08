#!/usr/bin/env python3

from aocd.models import Puzzle
from pathlib import Path
import heapq
from unionfind import unionfind
import networkx as nx

def solve(data: str, connect_count: int, part: int) -> int:
    lines = data.strip().splitlines()
    points = [tuple(map(int, line.split(','))) for line in lines]
    def distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
      dx = a[0] - b[0]
      dy = a[1] - b[1]
      dz = a[2] - b[2]
      return dx*dx + dy*dy + dz*dz
    if part == 1:
      heap = []
      for i, point in enumerate(points):
        for j in range(i+1, len(points)):
          heapq.heappush(heap, (distance(point, points[j]), i, j))
      u = unionfind(len(points))
      for i in range(connect_count):
        _, a, b = heapq.heappop(heap)
        u.unite(a, b)
      largest_cc = sorted([len(group) for group in u.groups()], reverse=True)[:3]
      product = 1
      for cc in largest_cc:
        product *= cc
      return product
    elif part == 2:
      G = nx.Graph()
      for i, point in enumerate(points):
        for j in range(i+1, len(points)):
          G.add_edge(i, j, weight=distance(point, points[j]))
      mst = nx.minimum_spanning_tree(G)
      highest_weight_edge = max(mst.edges(data=True), key=lambda edge: edge[2]['weight'])
      return pi[0] * pj[0]

def main():
  puzzle = Puzzle(year=2025, day=int(Path(__file__).stem))

  example = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
  example_a_result = 40
  example_b_result = 25272
  v = solve(example, 10, 1)
  print(v)
  assert(v == example_a_result)
  data = puzzle.input_data
  v = solve(data, 1000, 1)
  print(v)
  puzzle.answer_a = v

  v = solve(example, 0, 2)
  print(v)
  assert(v == example_b_result)
  data = puzzle.input_data
  v = solve(data, 0, 2)
  print(v)
  puzzle.answer_b = v

if __name__ == "__main__":
    main()