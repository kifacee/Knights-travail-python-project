

class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, childNode):
        if (childNode not in self._children):
            self._children.append(childNode)
            if childNode.parent is not self:
                childNode.parent = self

    def remove_child(self, childNode):
        if childNode in self._children:
            self._children.remove(childNode)
            childNode.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parentNode):
        if self._parent is not None and self in self._parent._children:     #remove from old parent's child list
            self._parent.remove_child(self)
        self._parent = parentNode       #set new parent
        if parentNode is not None:
            parentNode.add_child(self)  #add to parent's child list


    def depth_search(self, value):
        if self._value == value:       #check the value
            return self
        for child in self.children:         #for each child
            res = child.depth_search(value)    #check the val on first child, which will check its first child, so DFS
            if res:                 #returns None if no match
                return res
        return None             #base case of having no children will return None if no match

    def breadth_search(self, value):
        from collections import deque       #importing in a function waits for that function call before importing
                                            #but once run once, it is cached, so don't need to worry about importing multiple times
        #deque helps for faster queue operations, O(1) time
        queue = deque([self])           #start the queue off with the first node inside
        while queue:                    #end when empty
            current = queue.popleft()   #remove the first item in queue, this will do BFS
            if current.value == value:      #check it
                return current
            queue.extend(current.children)  #add all of its kids, this progresses the loop
        return None                             #return None if loops finishes and no match





#alternate where parent/child relationships are managed in the setter.
#makes the tests fail though

# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._parent = None
#         self._children = []

#     @property
#     def value(self):
#         return self._value

#     @property
#     def children(self):
#         return self._children

#     def add_child(self, childNode): #really a 'add parent', but in the parent setter it adds the child
#         # Set the child's parent — this will update self._children automatically
#         childNode.parent = self
#         #do not need to actually add the child to the children list, that happens in the setter
#         # if (childNode not in self._children):
#         #     self._children.append(childNode)

#     def remove_child(self, childNode):
#         if childNode in self._children:
#             self._children.remove(childNode)
#             childNode.parent = None

#     @property
#     def parent(self):
#         return self._parent

#     @parent.setter
#     def parent(self, newParent):
#         # Remove self from current parent if it exists
#         if self._parent is not None:
#             self._parent._children.remove(self)

#         # Set the new parent
#         self._parent = newParent

#         # Add self to new parent's children list (if not already added)
#         if  newParent is not None and self not in newParent._children:
#             newParent._children.append(self)
