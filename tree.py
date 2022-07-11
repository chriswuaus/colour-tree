"""
Tree
----

This file contains the tree data structure that will be used for interacting
with our coloured nodes.
The tree contains a "root" node, which is the topmost node of the tree.
It is interconnected through children and finally ends at external nodes ending
at the leaves.

*** Assignment Notes ***

This is the main file that will be tested, you must implement the related
functions with a TODO annotated.

Your task is to implement these methods.
"""

from node import Node
from colours import Colour
from typing import Tuple, List


class Tree:
    """
    Tree Class
    ----------

    Contains the data structure of a tree, where each node of the tree has a
    parent and children.
    If a node has no parent, it is considered the "root" of the tree.
    If a node has zero (0) children, it is a leaf (or is "external").

    Each node in the tree has the type `Node`, which is defined in `node.py`.

    ====== Functions ======

    - __init__ : Sets up the tree with a specified root.
    - put(node, child) : Adds the `child` to the `node`.
    - swap(subtree_a, subtree_b) : Swaps the position of the subtrees.
    - is_coloured_to_depth_k(node, colour, k) : Checks that the subtree rooted
        at `node` has the same colour until `k` levels deep.
    - is_colour_until(start_node, colour_a, colour_b): Checks that the subtree
        rooted at `start_node` has `colour_a` for all nodes in all paths until
        `colour_b`. E.g. (if colour_a is red, and colour_b is green, then all
        paths must have nodes that are Green until reaching a red.)

    == Things to note ==

    1. Every node given as an argument WILL be in the tree, you do not have to
        check whether it exists in the tree.
    2. Every node will be initialised with a parent (unless it is the root node
        of the tree).
    3. The ordering of the children does not matter.
    """

    def __init__(self, root: Node) -> None:
        """
        Initialises the tree with a root of type `Node` from `node.py`

        :param root: The root node of our tree.
        """

        self.root = root

    def update_node_colour(self, n: Node, new_colour: Colour) -> None:
        """
        Update the colour of a node.

        :param n: The node to change the colour of.
        :param new_colour: The new colour to change to.
        """
        if (n == None or new_colour == None):
            return

        if (n.is_root()):
            n.update_colour(new_colour)
            return
        else:
            n.update_colour(new_colour)
            n.colour = new_colour
            self.update_node_colour(n.parent, n.parent.colour)

        # Call update_colour() on the node
        # TODO implement me please.

    def put(self, parent: Node, child: Node) -> None:
        """
        Inserts a node into the tree.
        Adds `child` to `parent`.

        :param parent: The parent node currently in the tree.
        :param child: The child to add to the tree.
        """
        # TODO implement me please.
        if (parent == None or child == None):
            return        
        parent.add_child(child)
        child.parent = parent
        self.update_node_colour(parent, parent.colour)

    def rm(self, child: Node) -> None:
        """
        Removes child from parent.

        :param child: The child node to remove.
        """
        if (child == None):
            return
        if (child == self.root):
            self.root = None
            return
        tmp = child.parent
        tmp.remove_child(child)
        self.update_node_colour(tmp, tmp.colour)

        # TODO implement me please.

    def swap(self, subtree_a: Node, subtree_b: Node) -> None:
        """
        Swaps subtree A with subtree B

        :param subtree_a : Root of the subtree A.
        :param subtree_b : Root of the subtree B.

        Example:

            A
           / \
           B  C
         /   / \
        D   J   K

        SWAP(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D
        """
        if (subtree_a == None or subtree_b == None):
            return
        if subtree_a.parent == None or subtree_b.parent == None:
            return
        atmp = subtree_a.parent
        tmpp = subtree_b.parent

        if (atmp == tmpp):
            return

        subtree_a.parent.remove_child(subtree_a)
        subtree_b.parent.remove_child(subtree_b)
        self.put(tmpp, subtree_a)
        self.put(atmp, subtree_b)

        # TODO implement me please.

    def is_coloured_to_depth_k(self, start_node: Node, colour: Colour, k: int) -> bool:
        """
        Checks whether all nodes in the subtree (up and including level `k`
            starting from the start node) have the same colour!

        (This checks node.colour)

        :param start_node : The node to start checking.
        :param colour: The colour to compare a node's colour to.
        :param k: The depth we should check until.

        === Examples ===

        (start)---> G
                   / \
                  G   G
                 /|   |
                G R   G
                  |
                  R

        is_coloured_to_depth_k(start, Colours.GREEN, 0) => True
        is_coloured_to_depth_k(start, Colours.RED, 0) => False
        is_coloured_to_depth_k(start, Colours.GREEN, 1) => True
        is_coloured_to_depth_k(start, Colours.GREEN, 2) => False
        """
        
        if (k < 0 or start_node == None):
            return False, None
        queue = [start_node]
        visited = [start_node]
        height = [0]
        i = 0
        hm = 0

        b = True

        while (len(queue) != 0):
                i += 1
                if (height[i - 1] == k + 1):
                    return True
                x = queue.pop(0)
                if (x.colour.cmp(colour) != 0):
                    b = False
                    break
                if (len(x.children) == 0 and (height[i-1] < k)):
                    b = False
                    break
                for child in x.children:
                    # if child not in visited:
                        height.append(height[i - 1] + 1)
                        queue.append(child)
                        visited.append(child)         
        return b

        # TODO implement me please.

    def is_colour_until_condition(
            self,
            start_node: Node,
            colour_a: Colour,
            colour_b: Colour
        ) -> Tuple[bool, List[Node]]:
        """
        Checks whether the subtree rooted at `start_node` has colour_a until
        colour_b in all paths.

        We are checking the property: "In subtree rooted at start_node, is every
        path colour_a until colour_b?"

        If this condition fails, you must provide a path
        (given in the form of a list starting from `start_node to the failing
        node) as a "witness" to ensure that your answer is correct.

        NOTE: your path MUST be a valid path!
        If there are more than one paths - only one witness path is required.

        If the condition holds, then you return (True, None), as there is no
        required path.

        :param start_node: The node to start checking.
        :param colour_a: The first condition "colour_a holds until"
        :param colour_b: The stopping condition "until colour_b"


        === Examples ===

        (start)---> G
                   / \
                  G   G
                 /|   |
                R R   R
                  |
                  R

        is_colour_until_condition(start, Colours.GREEN, Colours.RED)
            -> (True, None)

        (start)---> G
                   / \
                  G   G (nodeA)
                 /|   |
                R R   G  (nodeD)
                  |
                  R

        is_colour_until_condition(start, Colours.GREEN, colours.RED)
            -> (False, [start, nodeA, nodeD])

        """
        # TODO implement me please.

        if (start_node.colour.cmp(colour_b) == 0):
            return [True, None]
        n = None
        stack = [start_node]
        while (len(stack) != 0):
            node = stack.pop()
            if (node.colour.cmp(colour_b) == 0):
                continue
            if (node.colour.cmp(colour_a) != 0 or node.is_leaf()):
                n = node  
            for child in node.children:
                stack.append(child)
        
        if n != None:
            witness_path = [n]
            wit_node = n
            while (True):
                if (wit_node == start_node):
                    return [False, witness_path[::-1]]
                wit_node = wit_node.parent
                witness_path.append(wit_node)
        
        return [True, None]

