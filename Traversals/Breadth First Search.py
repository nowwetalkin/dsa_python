# class node:
#   """docstring for node"""
#   def __init__(self, value):
#     self.value= value
#     self.left= None
#     self.right = None

# class BinarySearchTree:
#   """docstring for BinarySearchTree"""
#   def __init__(self):
#     self.root= None
    
#   def insert(self, value):
#     new_node= node(value)
#     if self.root==None:
#       self.root= new_node
#     else:
#       currnode= self.root
#       while currnode != None:
#         if value< currnode.value:
#           if currnode.left==None:
#             currnode.left=new_node
#             break
#           else:
#             currnode=currnode.left
#         elif value>currnode.value:
#           if currnode.right==None:
#             currnode=new_node
#             break
#           else:
#             currnode=currnode.right

#   def lookup(self,value):

#   def breadthfirstsearch(self):
#     currnode=self.root
#     lis= []
#     queue= []
#     queue.append(currnode)


    




















class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self,val):
    new_node = Node(val)
    if self.root == None:
      self.root = new_node
      return 
    temp = self.root
    while True:
      if new_node.val < temp.val:
        if temp.left == None:
          temp.left = new_node
          break
        else:
          temp = temp.left
      elif new_node.val > temp.val:
        if temp.right == None:
          temp.right = new_node
          break
        else:
          temp = temp.right

  def lookup(self,val):
    temp = self.root
    while True:
      if temp.val == val:
        return True
      elif temp == None:
        return False
      elif val < temp.val:
        temp = temp.left
      elif val > temp.val:
        temp = temp.right

  def breadthfirstsearch(self):
    currnode = self.root
    mylist = []
    queue = []
    queue.append(currnode)

    while len(queue) > 0:
      currnode = queue[0]
      del queue[0]
      mylist.append(currnode.val)
      if currnode.left:
        queue.append(currnode.left)
      if currnode.right:
        queue.append(currnode.right)
    
    return mylist
  
  def recursivebfs(self,queue,mylist):
    if len(queue) == 0:
      return mylist
    currnode = queue[0]
    del queue[0]
    mylist.append(currnode.val)
    if currnode.left:
      queue.append(currnode.left)
    if currnode.right:
      queue.append(currnode.right)

    return self.recursivebfs(queue,mylist)
    
      

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

x = tree.lookup(170)
print(x)  
print(tree.breadthfirstsearch())
print(tree.recursivebfs([tree.root],[]))