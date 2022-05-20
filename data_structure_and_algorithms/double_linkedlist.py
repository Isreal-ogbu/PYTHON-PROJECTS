class node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return '(' + str(self.data) + ')'


class double_linkedlist:
    def __init__(self, root=None):
        self.root = root
        self.last = root
        self.size = 0

    def add(self, value3):
        if self.size == 0:
            self.root = node(value3)
            self.last = self.root
        else:
            new_node = node(value3, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1

    def find(self, value4):
        this_node = self.root
        while True:
            if this_node.data == value4:
                return value4
            elif this_node.next_node is None:
                return False
            this_node = this_node.next_node

    def remove(self, value5):
        this_node = self.root
        while this_node is not None:
            if this_node.data == value5:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node = this_node.next_node.prev_node
                        this_node.next_node.prev_node = this_node.prev_node.next_node
                    else:
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True
            else:
                this_node = this_node.next_node
        return False

    def print(self):
        if self.size == 0:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print()


# Test
x = double_linkedlist()
for i in [23, 45, 67, 89, 65, 43, 21, 46, 78, 100]:
    x.add(i)
x.print()
print('size = ', x.size)
print(x.remove(23))
print(x.find(45))
x.print()
print('size = ', x.size)
print(x.root.next_node)
