class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
      return
    
    current_node = self.root

    while True:
      if current_node.value > value:
        if current_node.left is not None:
          current_node = current_node.left
        else:
          current_node.left = Node(value)
          break
      else:
        if current_node.right is not None:
          current_node = current_node.right
        else:
          current_node.right = Node(value)
          break

  def search(self, value):
    return self._search_data(self.root, value)
  
  def _search_data(self, node, value):
    if node is None or node.value == value:
      return node is not None
    elif value < node.value:
      return self._search_data(node.left, value)
    else: 
      return self._search_data(node.right, value)

  def delete(self, value):
    self.root, is_delete = self._delete_data(self.root, value)
    return is_delete

  def _delete_data(self, node, value):
    # 삭제 로직의 경우
    # 삭제 시 2개의 자식 노드가 있는 경우
    # 우측 자식의 최하단 좌측 노드를 가져오도록 제작
    is_delete = True
    if node is None:
      return node, False
    if value == node.value:
      if node.left and node.right:
        parent = node
        child = node.right
        
        while child.left is not None:
          parent = child
          child = child.left
        child.left = node.left  
        if parent != node:
          parent.left = child.right
          child.right = node.right
        node = child
      elif node.left:
        node = node.left
      elif node.right:
        node = node.right
      else:
        node = None

    elif value < node.value:
      node.left, is_delete = self._delete_data(node.left, value)
    else:
      node.right, is_delete = self._delete_data(node.right, value)

    return node, is_delete

array = [14, 7, 4, 11, 9, 12, 8]
bst = BinarySearchTree()

for x in array:
  bst.insert(x)
# Find
print(bst.search(12)) # True
print(bst.search(7)) # True
# Delete
print(bst.delete(7)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # True
print(bst.delete(2)) # False
print(bst.search(7)) # False
print(bst.search(14)) # False
print(bst.search(11)) # False
print(bst.search(9)) # True