from collections import deque


class BinaryTree:

  def __init__(self):
    # Mapping para sa SUMICAO (7 letters)
    self.nodes = {1: 'S', 2: 'U', 3: 'M', 4: 'I', 5: 'C', 6: 'A', 7: 'O'}
    self.tree = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: [],
    }

  def print_diagram(self):
    print('BINARY TREE: SUMICAO')
    print('       1-S')
    print('      /   \\')
    print('    2-U   3-M')
    print('   /   \\  /  \\')
    print('  4-I  5-C 6-A 7-O')
    print('-' * 40)

  def bfs(self, start=1):
    visited = []
    queue = deque([start])
    while queue:
      node = queue.popleft()
      if node not in visited:
        visited.append(node)
        for neighbor in self.tree[node]:
          if neighbor not in visited:
            queue.append(neighbor)
    return visited

  def dfs(self, start=1, visited=None):
    if visited is None:
      visited = []
    visited.append(start)
    for neighbor in self.tree[start]:
      if neighbor not in visited:
        self.dfs(neighbor, visited)
    return visited


if __name__ == '__main__':
  bt = BinaryTree()
  bt.print_diagram()

  bfs_res = bt.bfs()
  dfs_res = bt.dfs()

  print('BFS:', ' -> '.join([f'{n}-{bt.nodes[n]}' for n in bfs_res]))
  print('DFS:', ' -> '.join([f'{n}-{bt.nodes[n]}' for n in dfs_res]))