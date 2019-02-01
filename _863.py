# -*- coding: utf-8 -*-
__author__ = 'gzp'

import collections

from utils import Tree, TreeNode

class Solution1(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # DFS
        conn = collections.defaultdict(list)

        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        connect(None, root)
        # BFS
        que = collections.deque()
        que.append(target.val)
        visited = {target.val}
        for k in range(K):
            size = len(que)
            for i in range(size):
                node = que.popleft()
                for j in conn[node]:
                    if j not in visited:
                        que.append(j)
                        visited.add(j)
        return list(que)


class Solution2(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # DFS
        conn = collections.defaultdict(list)

        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)

        connect(None, root)
        # BFS
        bfs = [target.val]
        visited = {target.val}
        for k in range(K):
            bfs = [y for x in bfs for y in conn[x] if y not in visited]
            visited |= set(bfs)
        return bfs


from collections import defaultdict


class Solution(object):
    def distanceK(self, root, target, K):
        dfs = defaultdict(list)

        def connect(parent, child):
            if parent and child:
                dfs[parent.val].append(child.val)
                dfs[child.val].append(parent.val)

            if child.left:
                connect(child, child.left)

            if child.right:
                connect(child, child.right)

        connect(None, root)

        seemed = {target.val}
        bfs = [target.val]
        for _ in range(K):
            bfs = [y for x in bfs for y in dfs[x] if y not in seemed]
            seemed |= set(bfs)
        return bfs


if __name__ == '__main__':
    s = Solution()
    root = Tree('[3,5,1,6,2,0,8,null,null,7,4]')
    print(s.distanceK(root, TreeNode(5), 2))
