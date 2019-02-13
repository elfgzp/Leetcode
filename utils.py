# -*- coding: utf-8 -*-
__author__ = 'gzp'

import json

from copy import copy


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def get_nodes(self):
        if not self:
            return []

        nodes = [self]
        node_vals = []

        while nodes:
            node = nodes.pop(0)

            node_vals.append(node.val)

            if node.left:
                nodes.append(node.left)

            if node.right:
                nodes.append(node.right)

        return node_vals


class Tree:
    def __new__(cls, nodes, *args, **kwargs):
        if isinstance(nodes, str):
            nodes = json.loads(nodes)

        if not nodes:
            return None

        root = TreeNode(nodes.pop(0))
        cls._tree(root, nodes)
        return root

    @classmethod
    def _tree(cls, root, nodes):
        tree_nodes = [root]

        while nodes and tree_nodes:
            tmp = []
            for node in tree_nodes:
                val = cls._get_first_node(nodes)
                if val is not None:
                    node.left = TreeNode(val)
                else:
                    node.left = None

                val = cls._get_first_node(nodes)

                if val is not None:
                    node.right = TreeNode(val)
                else:
                    node.right = None

                tmp.append(node.left)
                tmp.append(node.right)

            tree_nodes = copy(tmp)
        return root

    @classmethod
    def _get_first_node(cls, nodes):
        if nodes:
            return nodes.pop(0)
        else:
            return False


if __name__ == '__main__':
    t1 = Tree('[3,5,1,6,2,9,8,null,null,7,4]')
    print(t1.get_nodes())
    t2 = Tree('[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]')
    print(t2.get_nodes())
