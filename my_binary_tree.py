from typing import Any, Optional

class BinaryTree:
    """The base class for a Binary Tree."""

    def __init__(
            self,
            item: Any,
            left: "Optional[BinaryTree]" = None,
            right: "Optional[BinaryTree]" = None
    ) -> None:
        self._item = item

        self._left = left
        if self._left is not None:
            self._left._parent = left

        self._right = right
        if self._right is not None:
            self._right._parent = self

        self._parent: "Optional[BinaryTree]" = None

    def is_root(self) -> bool:
        return self._parent is None

    def get_parent(self) -> "Optional[BinaryTree]":
        return self._parent

    def get_left(self) -> "Optional[BinaryTree]":
        return self._left

    def get_right(self) -> "Optional[BinaryTree]":
        return self._right

    def get_item(self) -> Any:
        return self._item

    def get_root(self) -> "Optional[BinaryTree]":
        node: "Optional[BinaryTree]" = self
        while node and not node.is_root():
            node = node.get_parent()
        return node

    def set_left(self, left: "BinaryTree") -> None:
        self._left = left
        self._left._parent = self

    def set_right(self, right: "BinaryTree") -> None:
        self._right = right
        self._right._parent = self


class MyBinaryTree(BinaryTree):
    def height(self) -> int:
        """Returns the height of this tree."""
        c = []

        def helper(tree: MyBinaryTree, tiefe=0) -> int | None:
            if tree is not None:
                nonlocal c
                c.append(tiefe)
                helper(tree.get_left(), tiefe + 1)
                helper(tree.get_right(), tiefe + 1)
            return None
        helper(self)
        return max(c)+1

    def max_sum(self) -> int:
        def helper(tree: MyBinaryTree) -> None:
            nonlocal obj, x
            if tree is not None:
                if tree not in obj:
                    x = x + [tree.get_item()]
                    obj = obj + [tree]
                helper(tree.get_right())
                helper(tree.get_left())
            return None
        obj: list = []
        x: list = []
        if self.get_left() is not None:
            helper(self.get_left())
        a = sum(x)
        x.clear()
        obj.clear()
        if self.get_right() is not None:
            helper(self.get_right())
        return a if a > sum(x) else sum(x)

    def endings(self) -> list:
        def helper(tree: MyBinaryTree) -> None:
            if tree is not None:
                if tree.get_right() is None and tree.get_left() is None:
                    nonlocal obj
                    obj.append(tree)
                helper(tree.get_right())
                helper(tree.get_left())
            return None
        obj = []
        helper(self)
        return obj

    def max_path(self) -> int:
        obj = []
        obj[::] = (self.endings())[::]
        max_value = 0
        for tree in obj:
            temp_value = tree.get_item()
            while tree.get_parent() is not None:
                tree = tree.get_parent()
                temp_value += tree.get_item()
            if temp_value > max_value:
                max_value = temp_value

        return max_value

    def max_width(self) -> int:
        def helper(tree: MyBinaryTree, tiefe=0) -> int | None:

            if tree is not None:
                nonlocal c, obj
                if tree not in obj:
                    c.append(tiefe)
                    obj.append(tree)
                helper(tree.get_left(), tiefe + 1)
                helper(tree.get_right(), tiefe + 1)
            return None

        obj = []
        c = []
        helper(self)
        max2 = 0
        for x in c:
            if max2 < c.count(x):
                max2 = c.count(x)
        return max2


if __name__ == "__main__":
    tree = MyBinaryTree(1)

    tree.set_left(MyBinaryTree(2))
    tree.set_right(MyBinaryTree(3))

    tree.get_root().get_left().set_left(MyBinaryTree(20))
    tree.get_root().get_left().set_right(MyBinaryTree(50))
    tree.get_root().get_right().set_left(MyBinaryTree(8))
    tree.get_root().get_right().set_right(MyBinaryTree(7))

    print(tree.height())

    pass
