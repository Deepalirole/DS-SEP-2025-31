from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Iterable

@dataclass
class _Node:
    key: int
    left: Optional["_Node"] = None
    right: Optional["_Node"] = None

class BinarySearchTree:
    def __init__(self, keys: Iterable[int] = ()):
        self.root: Optional[_Node] = None
        for k in keys:
            self.insert(k)

    def insert(self, key: int) -> None:
        def _ins(node: Optional[_Node], key: int) -> _Node:
            if node is None:
                return _Node(key)
            if key < node.key:
                node.left = _ins(node.left, key)
            elif key > node.key:
                node.right = _ins(node.right, key)
            # duplicates ignored
            return node
        self.root = _ins(self.root, key)

    def search(self, key: int) -> bool:
        cur = self.root
        while cur:
            if key == cur.key:
                return True
            cur = cur.left if key < cur.key else cur.right
        return False

    def inorder(self) -> List[int]:
        res: List[int] = []
        def _dfs(n: Optional[_Node]):
            if not n: return
            _dfs(n.left); res.append(n.key); _dfs(n.right)
        _dfs(self.root)
        return res

    def preorder(self) -> List[int]:
        res: List[int] = []
        def _dfs(n: Optional[_Node]):
            if not n: return
            res.append(n.key); _dfs(n.left); _dfs(n.right)
        _dfs(self.root)
        return res

    def postorder(self) -> List[int]:
        res: List[int] = []
        def _dfs(n: Optional[_Node]):
            if not n: return
            _dfs(n.left); _dfs(n.right); res.append(n.key)
        _dfs(self.root)
        return res

    # Bonus: deletion
    def delete(self, key: int) -> None:
        def _min_node(n: _Node) -> _Node:
            while n.left:
                n = n.left
            return n

        def _del(node: Optional[_Node], key: int) -> Optional[_Node]:
            if node is None:
                return None
            if key < node.key:
                node.left = _del(node.left, key)
            elif key > node.key:
                node.right = _del(node.right, key)
            else:
                # found node to delete
                if node.left is None: return node.right
                if node.right is None: return node.left
                # two children: replace with inorder successor
                succ = _min_node(node.right)
                node.key = succ.key
                node.right = _del(node.right, succ.key)
            return node
        self.root = _del(self.root, key)
