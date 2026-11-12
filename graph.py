from collections import deque


class GraphStructure:

  def __init__(self):
    # Mapping para sa SUMICAO (7 letters)
    self.nodes = {1: 'S', 2: 'U', 3: 'M', 4: 'I', 5: 'C', 6: 'A', 7: 'O'}
    self.graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6, 7],
        4: [2, 7],
        5: [2, 7],
        6: [3],
        7: [3, 4, 5],
    }

  def print_diagram(self):
    print('GRAPH: SUMICAO')
    print('Vertices: 1-S, 2-U, 3-M, 4-I, 5-C, 6-A, 7-O')
    print('Undirected edges:')
    print('  1-S -- 2-U')
    print('  1-S -- 3-M')
    print('  2-U -- 4-I')
    print('  2-U -- 5-C')
    print('  3-M -- 6-A')
    print('  3-M -- 7-O')
    print('  4-I -- 7-O (Bottom Hub)')
    print('  5-C -- 7-O (Bottom Hub)')
    print('  6-A -- 3-M')
    print('-' * 40)

  def bfs(self, start=1):
    visited = []
    queue = deque([start])
    while queue:
      node = queue.popleft()
      if node not in visited:
        visited.append(node)
        for neighbor in self.graph[node]:
          if neighbor not in visited:
            queue.append(neighbor)
    return visited

  def dfs(self, start=1, visited=None):
    if visited is None:
      visited = []
    visited.append(start)
    for neighbor in self.graph[start]:
      if neighbor not in visited:
        self.dfs(neighbor, visited)
    return visited


if __name__ == '__main__':
  gs = GraphStructure()
  gs.print_diagram()

  bfs_res = gs.bfs()
  dfs_res = gs.dfs()

  print('BFS starting at 1-S:', ' -> '.join([f'{n}-{gs.nodes[n]}' for n in bfs_res]))
  print('DFS starting at 1-S:', ' -> '.join([f'{n}-{gs.nodes[n]}' for n in dfs_res]))