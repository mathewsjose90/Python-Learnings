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

    def size(self):
        return len(self.stack)


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
print(s1.display())

s2 = Stack()
counter = 1
items_count = s1.size()
while counter <= items_count:
    top = s1.pop()
    for _ in range(items_count - counter):
        s2.push(s1.pop())
    s1.push(top)
    while not s2.isEmpty():
        s1.push(s2.pop())
    counter += 1

print(s1.display())
