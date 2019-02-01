# -*- coding: utf-8 -*-
__author__ = 'gzp'

import collections


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(dict)
        self.key_st_map = collections.defaultdict(list)
        self.ts_set = collections.defaultdict(set)

        self.key_last_ts_map = dict()

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.map[key][timestamp] = value
        self.key_st_map[key].append(timestamp)
        self.ts_set[key].add(timestamp)

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        tmp = timestamp
        while tmp > 0:
            if tmp in self.ts_set[key]:
                break
            tmp -= 1
        else:
            return ''

        return self.map[key][tmp]
