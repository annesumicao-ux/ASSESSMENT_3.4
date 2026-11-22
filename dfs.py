class BinaryTreeDFS:

  def __init__(self):
    # MAY SUMICAO (10 nodes, arranged top-to-bottom, left-to-right)
    self.nodes = {
        1: 'M',
        2: 'A',
        3: 'Y',
        4: 'S',
        5: 'U',
        6: 'M',
        7: 'I',
        8: 'C',
        9: 'A',
        10: 'O',
    }
    # Adjacency list: [left_child, right_child]
    self.tree = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [8, 9],
        5: [10],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
    }

  def print_diagram(self):
    print('BINARY TREE: MAY SUMICAO')
    print('             1-M')
    print('           /     \\')
    print('        2-A       3-Y')
    print('       /   \\     /   \\')
    print('     4-S   5-U  6-M   7-I')
    print('     / \\   /')
    print('   8-C 9-A 10-O')
    print('-' * 45)

  def preorder(self, node=1, result=None):
    """Root -> Left -> Right"""
    if result is None:
      result = []
    if node not in self.tree:
      return result

    result.append(self.nodes[node])
    children = self.tree[node]
    if len(children) >= 1:
      self.preorder(children[0], result)
    if len(children) >= 2:
      self.preorder(children[1], result)
    return result

  def inorder(self, node=1, result=None):
    """Left -> Root -> Right"""
    if result is None:
      result = []
    if node not in self.tree:
      return result

    children = self.tree[node]
    if len(children) >= 1:
      self.inorder(children[0], result)
    result.append(self.nodes[node])
    if len(children) >= 2:
      self.inorder(children[1], result)
    return result

  def postorder(self, node=1, result=None):
    """Left -> Right -> Root"""
    if result is None:
      result = []
    if node not in self.tree:
      return result

    children = self.tree[node]
    if len(children) >= 1:
      self.postorder(children[0], result)
    if len(children) >= 2:
      self.postorder(children[1], result)
    result.append(self.nodes[node])
    return result


if __name__ == '__main__':
  bt = BinaryTreeDFS()
  bt.print_diagram()

  print('A. Preorder  (Root -> Left -> Right):')
  print('  ', ' -> '.join(bt.preorder()))

  print('B. Inorder   (Left -> Root -> Right):')
  print('  ', ' -> '.join(bt.inorder()))

  print('C. Postorder (Left -> Right -> Root):')
  print('  ', ' -> '.join(bt.postorder()))