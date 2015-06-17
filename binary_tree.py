'''
defines a class for binary trees
'''


class BinaryTree(object):
    def __init__(self, value, left_branch, right_branch):
        self.value = value
        self.left = left_branch
        self.right = right_branch

    def search_tree(self, value):
        '''
        returns the sub tree with the argument value as the root. if value is not present, returns None
        '''
        if value == self.value:
            return self
        elif value < self.value:
            if self.left is None:
                return None
            return self.left.search_tree(value)
        elif value > self.value:
            if self.right is None:
                return None
            return self.right.search_tree(value)
        else:
            return None

    def search_tree_for_parent(self, value):
        '''
        returns subtree that is the parent of argument value.
        if argument value is not present, returns None.
        '''
        if self.search_tree(value) is None or value == self.value:
            return None
        if value == self.left.value or value == self.right.value:
            return self
        elif value > self.value:
            return self.left.search_tree_for_parent(value)
        elif value < self.value:
            return self.right.search_tree_for_parent(value)
        else:
            return None

    def size(self):
        '''
        returns size of given tree
        '''
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.size() + 1
        elif self.right is None:
            return self.left.size() + 1
        else:
            return self.left.size() + self.right.size() + 1

    def min_tree(self):
        '''
        returns lowest value node in given tree
        '''
        if self.left is None:
            return self
        else:
            return self.left.min_tree()

    def max_tree(self):
        '''
        returns highest value node in given tree
        '''
        if self.right is None:
            return self
        else:
            return self.right.max_tree()

    def pred_tree(self, value):
        '''
        returns subtree of next lowest valued node than given value
        '''
        value_tree = self.search_tree(value)
        if value_tree.left is None:
            return None
        else:
            return value_tree.left.max_tree()

    def succ_tree(self, value):
        '''
        returns subtree of next highest valued node than given value
        '''
        value_tree = self.search_tree(value)
        if value_tree.right is None:
            return None
        else:
            return value_tree.right.min_tree()

    def delete(self, value):
        '''
        deletes argument value from tree
        '''
        value_tree = self.search_tree(value)
        parent_tree = self.search_tree_for_parent(value)
        if value_tree.left is None and value_tree.right is None:
            if parent_tree.value < value:
                parent_tree.right = None
                return self
            if parent_tree.value > value:
                parent_tree.left = None
                return self
        if parent_tree.right is value_tree:
            if value_tree.left is None:
                parent_tree.right = value_tree.right
                return self
            if value_tree.right:
                parent_tree.right = value_tree.left
                return self
        if parent_tree.left is value_tree:
            if value_tree.left is None:
                parent_tree.right = value_tree.right
                return self
            if value_tree.right:
                parent_tree.right = value_tree.left
                return self
        else:
            predecessor = self.pred_tree(value)
            pred_value = predecessor.value
            value_tree.value = pred_value
            predecessor.value = value
            self.delete(predecessor.value)
            return self

    def insert(self, value):
        '''
        inserts argument value into tree
        '''
        if self.value == value:
            return self
        if self.value > value:
            if self.left is None:
                self.left = value
                return self
            else:
                self.insert(value)
        if self.value < value:
            if self.right is None:
                self.right = value
                return self
            else:
                self.insert(value)

    def elements_in_order(self):
        '''
        returns all elements in tree in order as a list
        '''
        if self is None:
            return []
        if self.left is None:
            left = []
        else:
            left = self.left.elements_in_order()
        node = [self.value]
        if self.right is None:
            right = []
        else:
            right = self.right.elements_in_order()
        return left + node + right
