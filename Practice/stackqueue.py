class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def size(self):
    return len(self.items)
  
  def is_empty(self):
    return len(self.items) == 0 

class StackQueue:
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def enqueue(self, item):
    self.stack1.push(item)

  def dequeue(self):
    if self.stack2.is_empty():
      while self.stack1.is_empty() == False:
        self.stack2.push(self.stack1.pop())
    return self.stack2.pop()


def main():
  print("StackQueue TEST")
  queue = StackQueue()
  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  queue.enqueue(4)
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())

  print("Stack TEST")
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.push(4)
  print(stack.pop())
  print(stack.pop())
  print(stack.pop())
  print(stack.pop())

main()
