class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    ringList = self.storage
    if self.current == self.capacity:
      self.current = 0
    ringList[self.current] = item
    self.current += 1

  def get(self):
    cleanList = [i for i in self.storage if i != None]
    return cleanList

""" python
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

maybe some kind of counter, reset at 3, that keeps track of which
should be overwritten?

buffer.get()   # should return ['d', 'e', 'f']
"""
