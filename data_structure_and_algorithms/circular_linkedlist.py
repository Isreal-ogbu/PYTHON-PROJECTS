class node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class circular_linkedlist:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, value):
        if self.size == 0:
            self.root = node(value)
            self.root.next_node = self.root
        else:
            new_node = node(value, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, value2):
        this_node = self.root
        while this_node is not None:
            if this_node.data == value2:
                return value2
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove(self, value3):
        this_node = self.root
        pre_node = None
        while True:
            if this_node.data == value3:
                if pre_node is not None:
                    pre_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True
            elif this_node.next_node == self.root:
                return False
            pre_node = this_node
            this_node = this_node.next_node

    def print(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node.data, end='->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node.data, end='->')
        print()


# Test
x = circular_linkedlist()
for i in [23, 45, 67, 89, 65, 43, 21, 46, 78, 100]:
    x.add(i)
x.print()
print(x.remove(23))
print(x.find(45))
x.print()
print('size = ', x.size)
