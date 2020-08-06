class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def find (self, val):
        node = self.head
        while node:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        index = 0
        x = []
        while node:
            if node.value == val:
                x.append(index)
            index += 1
            node = node.next
        if x:
            return x
        else:
            return None

    def delete(self, val, all = False):
        node = self.head

        if node:
            if node.value == val:
                self.head = node.next
                node = None
                return

        if not all:
            while node:
                if node.value == val:
                    break
                x = node
                node = node.next
            if node == None:
                return
            x.next = node.next
            node = None
            return

        else:
            prev = node
            node = node.next
            while node:
                if node.value == val:
                    if node.next == None:
                        self.tail = prev
                        break
                    else:
                        prev.next = node.next
                        x = node.next
                        node.value = None
                        node = x
                else:
                    prev = node
                    node = node.next

    def len(self):
        node = self.head
        i = 0
        while node:
            i += 1
            node = node.next
        return i

    def clear(self):
        self.__init__()

    def insert(self, afterNode, newNode):
        if not self.head:
            self.head = self.tail = Node(newNode)
            return
        elif afterNode == -1 or afterNode == None:
            k = self.head
            self.head = Node(newNode)
            self.head.next = k
            return
        node = self.head
        i = 0
        x = Node(newNode)
        while node:
            if i == afterNode:
                j = node.next
                node.next = x
                x.next = j
            if node.next == None:
                self.tail = x
            node = node.next
            i += 1

