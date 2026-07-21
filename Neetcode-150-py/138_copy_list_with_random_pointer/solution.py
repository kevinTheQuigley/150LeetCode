from __future__ import annotations


class Node:
    def __init__(self, x: int, next: Node | None = None, random: Node | None = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # Time: O(?)
    # Space: O(?)
    def copy_random_list(self, head: Node | None) -> Node | None:
        # TODO: Implement copy_random_list
        return None
