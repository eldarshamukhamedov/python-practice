"""
Queue implementation
Not using built-in list methods on purpose
"""

class Queue:

    def __init__(self, items = []):
        self.items = items

    def enqueue(self, item):
        self.items += [item]
        return item

    def dequeue(self):
        item = self.items[0]
        del self.items[0]
        return item

    def clear(self):
        self.items = []
        return self.items

    def head(self):
        try:
            return self.items[0]
        except IndexError:
            return None

    def tail(self):
        try:
            return self.items[-1]
        except IndexError:
            return None

    def peekAll(self):
        return self.items

    def isEmpty(self):
        return False if len(self.items) > 0 else True




myQueue = Queue(range(1, 5, 1))

print 'Queue:', myQueue.peekAll()
print 'Empty?:', myQueue.isEmpty()
print 'Head:', myQueue.head()
print 'Tail:', myQueue.tail(), '\n'

print 'Enqueue:', myQueue.enqueue('HELLO')
print 'Queue:', myQueue.peekAll()
print 'Empty?:', myQueue.isEmpty()
print 'Head:', myQueue.head()
print 'Tail:', myQueue.tail(), '\n'

print 'Dequeue:', myQueue.dequeue()
print 'Queue:', myQueue.peekAll()
print 'Empty?:', myQueue.isEmpty()
print 'Head:', myQueue.head()
print 'Tail:', myQueue.tail(), '\n'

print 'Clear:', myQueue.clear()
print 'Queue:', myQueue.peekAll()
print 'Empty?:', myQueue.isEmpty()
print 'Head:', myQueue.head()
print 'Tail:', myQueue.tail(), '\n'
