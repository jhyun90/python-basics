

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0
        self.list = []

    def size(self):
        return self.size

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None

        else:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None

            return pop_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def display(self):
        result = []
        cur_node = self.head

        if self.is_empty():
            return None

        else:
            while(cur_node != None):
                print(cur_node.data, end=' ')
                if cur_node.next != None:
                    print('->', end=' ')

                result.append(cur_node.data)
                cur_node = cur_node.next

            print()

            return result


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print(stack.display())
print("Top Element:", stack.peek())

stack.pop()
stack.pop()

print(stack.display())
print("Top Element:", stack.peek())
