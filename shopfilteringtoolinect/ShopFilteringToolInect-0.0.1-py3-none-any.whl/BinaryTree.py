class BinaryTreeNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self._right_child = None
        self._left_child = None

    def is_leaf(self):
        return self._right_child is None and self._left_child is None

    def set_right_child(self, node):
        if node is not None:
            node.key = 2 * self.key + 1
        self._right_child = node

    def set_left_child(self, node):
        if node is not None:
            node.key = 2 * self.key
        self._left_child = node

    def right(self):
        return self._right_child

    def left(self):
        return self._left_child

    def __repr__(self):
        return f'(im a node. key: {self.key}, value {self.value})'

    def copy(self):
        if self.is_leaf():
            return BinaryTreeNode(self.key, self.value)
        result = BinaryTreeNode(self.key, self.value)
        if self.left() is not None:
            result.set_left_child(self.left().copy())
        else:
            result.set_left_child(None)
        if self.right() is not None:
            result.set_right_child(self.right().copy())
        else:
            result.set_right_child(None)
        return result


# left = even, right = odd
class BinaryTree:
    # init
    def __init__(self, root=BinaryTreeNode(1, None)):
        self.root = root
        self.root.key = 1

    # infix order
    @staticmethod
    def traverse_order(root):
        if root is None:
            return []
        return BinaryTree.traverse_order(root.left()) + [root] + BinaryTree.traverse_order(root.right())

    def __iter__(self):
        return BinaryTree.traverse_order(self.root).__iter__()

    def add_node(self, node):
        for item in self:
            if 2 * item.key == node.key:
                item.set_left_child(node)
                return
            if 2 * item.key + 1 == node.key:
                item.set_right_child(node)
                return
        raise KeyError('Node has invalid key')

    # not optimal run time
    # TODO make it optimal
    def is_key_valid(self, key):
        for item in self:
            if key // 2 == item.key:
                return True
        return False

    def fix(self) -> None:
        def fix_node(root):
            if root.left() is not None:
                root.left().key = 2 * root.key
                fix_node(root.left())
            if root.right() is not None:
                root.right().key = 2 * root.key + 1
                fix_node(root.right())
        self.root.key = 1
        fix_node(self.root)

    # this invalidates binary tree passed to this function as argument
    def append(self, key, binary_tree):
        if not self.is_key_valid(key):
            raise KeyError('Invalid key')
        binary_tree.root.key = key
        self.add_node(binary_tree.root)
        self.fix()

    def __getitem__(self, key) -> BinaryTreeNode:
        path = []
        proxy_key = key
        while proxy_key > 0:
            path.append(proxy_key)
            proxy_key //= 2

        current_node = self.root
        current_direction = None
        while True:
            current_direction = path.pop(-1)
            if current_node is None:
                raise KeyError(f'No such key: {key}')

            if current_direction == key:
                return current_node

            if path[-1] % 2 == 0:
                current_node = current_node.left()
            else:
                current_node = current_node.right()

    def __setitem__(self, key, item):
        try:
            node = item
            if not isinstance(item, BinaryTreeNode):
                node = BinaryTreeNode(key, item)

            node.set_left_child(None)
            node.set_right_child(None)

            if key % 2 == 0:
                self[key // 2].set_left_child(node)
            else:
                self[key // 2].set_right_child(node)
        except KeyError:
            raise KeyError(f'No parent for {key}')

    def __str__(self):
        return str(BinaryTree.traverse_order(self.root))

    def copy(self):
        return BinaryTree(self.root.copy())

    @staticmethod
    def get_left_leaves(root):
        result = []
        if root.left() is None:
            result.append(root)
        else:
            result += BinaryTree.get_left_leaves(root.left())
        if root.right() is not None:
            result += BinaryTree.get_left_leaves(root.right())
        return result

    @staticmethod
    def get_right_leaves(root):
        result = []
        if root.right() is None:
            result.append(root)
        else:
            result += BinaryTree.get_right_leaves(root.right())
        if root.left() is not None:
            result += BinaryTree.get_right_leaves(root.left())
        return result

    def get_leafs(self, side):
        if 'left' in side or 'even' in side:
            return BinaryTree.get_left_leaves(self.root)

        if 'right' in side or 'odd' in side:
            return BinaryTree.get_right_leaves(self.root)

        raise ValueError('No such side')

    def append_side(self, binary_tree, side):
        todo = self.get_leafs(side)
        if 'left' in side or 'even' in side:
            for node in todo:
                copy_tree = binary_tree.copy()
                self.append(2 * node.key, copy_tree)
            return
        if 'right' in side or 'odd' in side:
            for node in todo:
                copy_tree = binary_tree.copy()
                self.append(2 * node.key + 1, copy_tree)
            return


def test():
    root = BinaryTreeNode(1, 1)
    tree = BinaryTree(root)
    tree[2] = 2
    tree[5] = 5
    copy_tree = tree.copy()
    tree[10] = 10

    simple_tree = BinaryTree(BinaryTreeNode(1, 1))
    simple_tree[2] = 2
    simple_tree[3] = 3
    simple_tree.append_side(simple_tree.copy(), 'left')
    print(simple_tree)
    # print(BinaryTree.get_left_leaves(tree.root), BinaryTree.get_right_leaves(tree.root))


if __name__ == '__main__':
    test()
