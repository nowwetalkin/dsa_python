'''class Node(value):
  """docstring for Node"""
  def __init__(self, value):
    self.left=None
    self.right=None
    self.value=value
    

class BinarySearchTree():
  def __init__(self):
    self.root= None


  def insert(self,value):
    new_node= Node(value)
    if self.root=None:
      self.root = new_node
    else:
      curr_node= self.root
      while True:
        if value<curr_node.value:
          #Left
          if curr_node.left==None:
            curr_node.left= new_node
            return
          else:
            curr_node=curr_node.left
        else:
          #Right
          if curr_node.right == None:
            curr_node.right= new_node
            return
          else:
            curr_node =curr_node.right
  def lookup(self,value):
    if self.root==None:
      return False
    else:
      curr_node= self.root
      while curr_node==None:

        if value<curr_node.value:
          #Left
          curr_node= curr_node.left
        elif value> curr_node.value:
          curr_node= curr_node.right
        else:
          return curr_node
      return False

  def remove(self,data):'''
    
        


            














class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self,data):
    new_node = Node(data)
    if self.root == None:
      self.root = new_node
      return
    else:
      curr_node = self.root
      while True:
        if data < curr_node.data:
          #Left
          if curr_node.left == None:
            curr_node.left = new_node
            return 
          else:
            curr_node = curr_node.left
        elif data > curr_node.data:
            #Right
            if curr_node.right == None:
              curr_node.right = new_node
              return
            else:
              curr_node = curr_node.right

  def lookup(self,data):
    curr_node = self.root
    while True:
      if curr_node == None:
        return False
      if curr_node.data == data:
        return True
      elif data < curr_node.data:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right
    
  def print_tree(self):
    if self.root != None:
      self.printt(self.root)
#Inorder Traversal (We get sorted order of elements in tree)

  def printt(self,curr_node):
    if curr_node != None:
      self.printt(curr_node.left)
      print(str(curr_node.data))
      self.printt(curr_node.right)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)
bst.print_tree()
