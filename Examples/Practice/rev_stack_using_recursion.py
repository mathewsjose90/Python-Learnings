class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        return " ".join(map(str, self.stack))


def insert_at_bottom(s, t):
    if s.isEmpty():
        s.push(t)
        return
    top = s.pop()
    insert_at_bottom(s, t)
    s.push(top)


def reverse_stack(s):
    if s.isEmpty():
        return
    top = s.pop()
    reverse_stack(s)
    insert_at_bottom(s, top)
    return s


s = Stack()
s.push(20)
s.push(450)
s.push(40)
s.push(55)
print(s.display())
print(reverse_stack(s).display())
