"""
Tree Node
---------

This file contains the information for the tree nodes.
Each node contains a property (colour), the parent and list of children (unordered list).
This node comes with the operations required for basic functionality.
You need to finish off some of those functions though :)
"""

from colours import Colour


class Node:
    """
    Node Class
    ----------

    Contains the relevant functions to provide a node in the tree.
    The node has a property, "colour", which represents the colour of the node.

    IMPORANT: **Every node MUST have a colour, there are no blank nodes**

    Functions:

    * add_child(child_node: Node) : adds the child node to the list of children.
    * update_colour(colour: Colour) : changes the colour of this node.
    * is_external() -> bool : Checks if the node is a leaf, returns true if is leaf.
    * children() -> list(Node) : Returns the list of children in this node.
    """

    def __init__(self, colour: Colour) -> None:
        """
        Initialises the node with the required elements.

        :param colour: The colour of the node.
        """
        self.colour = colour
        self.parent = None
        self.children = []
        self.propagated_colour = colour

    def set_parent(self, parent: 'Node') -> None:
        """
        Sets a node's parent to the given node.

        :param parent: The pointer to the parent of this node.
        """
        self.parent = parent

    def update_colour(self, colour: Colour) -> None:
        """
        Updates the colour of the node.
        (HINT) if we don't give a colour, you shouldn't update it.
        :param colour: The new colour to set the node.
        """
        self.colour = colour 
        self.propagated_colour = colour

        if (self.is_leaf() == False):
            for child in self.children:
                if (child.propagated_colour.cmp(self.propagated_colour) >= 0):
                    self.propagated_colour = child.propagated_colour

        if (self.is_root()):
            return
        parent = self.parent
        while (parent != None):
            parent.propagated_colour = parent.colour
            parent = parent.parent
            if (parent == None):
                break
        parent = self.parent
        while (self.propagated_colour.cmp(parent.colour) >= 0 ):
            parent.propagated_colour = self.propagated_colour
            parent = parent.parent
            if (parent == None):
                break
        # TODO implement me please 

    def add_child(self, child_node: 'Node') -> None:
        """
        Adds a child node to the list of children of this node.
        (HINT) this should also perform some _things_.
        :param child_node: The pointer to the child node to add to children.
        """

        self.children.append(child_node)
        child_node.set_parent(self)
        child_node.update_colour(child_node.colour)
        # TODO implement me please

    def remove_child(self, child_node: 'Node') -> None:
        """
        Removes the child from the list of children.
        NOTE: You don't have to worry about adding the subtree of this node to
        the children, we are removing this child_node and all its subtree from
        existence.
        :param child_node: The pointer to the child node to remove.
        """
        i = 0
        node = self
        if (len(self.children) == 0):
            return
        for child in self.children:
            if child == child_node:
                child.parent = None
                self.children.pop(i)
            i += 1
        # if (b == True):
        # self.update_colour(self.colour)
        # # TODO implement me

    def get_children(self) -> list:
        """
        Returns the list of children for this current node.
        :return: The list of children
        """

        # Note: this is also accessible with `node.children`, but we want to
        # keep this here for usage in other languages people may be used to.
        return self.children

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False
    def is_root(self) -> bool:
        if self.parent == None:
            return True
        return False