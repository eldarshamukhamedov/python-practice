"""
Stack implementation
Not using built-in list methods on purpose
"""

class Stack:

    def __init__(self, items = []):
        print items
        self.items = items

    def push(self, item):
        self.items += [item]
        return item

    def pop(self):
        item = self.items[-1]
        del self.items[-1]
        return item

    def clear(self):
        self.items = []
        return self.items

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return None

    def peekAll(self):
        return self.items

    def isEmpty(self):
        return False if len(self.items) > 0 else True




myStack = Stack(range(1, 5, 1))

print 'Stack:', myStack.peekAll()
print 'Empty?:', myStack.isEmpty()
print 'Peek:', myStack.peek(), '\n'

print 'Push:', myStack.push('HELLO')
print 'Stack:', myStack.peekAll()
print 'Empty?:', myStack.isEmpty()
print 'Peek:', myStack.peek(), '\n'

print 'Pop:', myStack.pop()
print 'Pop:', myStack.pop()
print 'Pop:', myStack.pop()
print 'Stack:', myStack.peekAll()
print 'Empty?:', myStack.isEmpty()
print 'Peek:', myStack.peek(), '\n'

print 'Clear:', myStack.clear()
print 'Stack:', myStack.peekAll()
print 'Empty?:', myStack.isEmpty()
print 'Peek:', myStack.peek(), '\n'
