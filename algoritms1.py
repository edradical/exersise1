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
        x = []
        while node:
            if node.value == val:
                x.append(node)
            node = node.next
        if x:
            return x
        else:
            return None

    def delete(self, val, all = False):
        node = self.head
        
        if not node:
            return
        
        if not all:
            if not all:
                if node:
                    if node.value == val:
                        self.head = self.tail = node.next
                        node = None
                        return

                prev = node
                node = node.next
                while node:
                    if node.value == val:
                        if node.next == None:
                            node.value = None
                            self.tail = prev
                            self.tail.next = None
                            break
                        elif node.value == val:
                            prev.next = node.next
                            x = node.next
                            node.value = None
                            node = x
                            break
                    else:
                        prev = node
                        node = node.next
                if node == None:
                    return
                return

        else:
            if node.value == val:
                self.head = node.next

            prev = node
            node = node.next
            while node:
                if node.value == val:
                    if node.next == None:
                        node.value = None
                        self.tail = prev
                        self.tail.next = None
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

    def add_in_list(self):
        node = self.head
        x = []
        while node:
            x.append(node.value)
            node = node.next
        return (x)
