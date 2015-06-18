'''
implimentation of linked lists
'''


class SinglyLinkedList(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def head(self):
        '''
        returns first element of linked list
        '''
        return self

    def tail(self):
        '''
        returns last element of linked list
        '''
        if self.next is None:
            return self
        else:
            return self.next.tail()

    def insert_start(self, value):
        '''
        inserts value with pointer into start of linked list
        '''
        self.next = SinglyLinkedList(self.value, self.next)
        self.value = value

    def insert_end(self, value):
        '''
        inserts value with pointer into end of linked list
        '''
        if self.next is None:
            self.next = SinglyLinkedList(value, None)
        else:
            self.next.insert_end(value)

    def delete_start(self):
        '''
        deletes first value from linked lists
        '''
        if self.next is None:
            return None
        else:
            self.value = self.next.value
            self.next = self.next.next

    def delete_end(self):
        '''
        deletes last value from linked list
        '''
        if self.next is None:
            self.value = None
        else:
            self.next.delete_end()

    def traverse(self):
        '''
        returns a list of all linked list elements in order
        '''
        if self.next is None:
            return [self.value]
        value_list = [self.value]
        return value_list + self.next.traverse()
