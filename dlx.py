#Tools to construct a dancing links matrix

class Node():
    """
    Node used to construct vertical doubly linked lists
    
    Attributes:
        - option, int, option that Node is contained in
        - top, int, number of Header at top of vertical list
        - number, int, reference
        - above, Node/Header object, linked above
        - below, Node/Header object, linked below 

    Methods:
        - unlink_vert(), unlinks self from its above and below links
        - link_vert(), relinks self to its above and below links
    """
    def __init__(self, option, top, number):
        self.option = option
        self.top = top 
        self.number = number
        self.above = None
        self.below = None

    def unlink_vert(self):
        """Sets aboves below link to below and belows above link to above"""
        self.above.below = self.below
        self.below.above = self.above

    def link_vert(self):
        """Sets aboves below link and belows above link to self"""
        self.above.below = self.below.above = self
        self.unlinked = False

class Header():
    """
    Header for top of vertical doubly linked lists, 
    also form horizontal doubly linked list of Headers

    Attributes:
        - len, int, number of nodes in vertical doubly linked list
        - number, int, reference
        - left, Node/Header object, linked left
        - right, Node/Header object, linked right
        - above, Node/Header object, linked above
        - below, Node/Header object, linked below

    Methods:
        - unlink_hor(), unlinks self from its left and right links
        - link_hor(), relinks self to its left and right links
    """
    def __init__(self, number):
        self.len = 0
        self.number = number
        self.left = None
        self.right = None
        self.above = None
        self.below = None

    def unlink_hor(self):
        """Sets lefts right link to right link and rights left link to left link"""
        self.left.right = self.right
        self.right.left = self.left

    def link_hor(self):
        """Sets lefts right link and rights left link to self"""
        self.right.left = self.left.right = self