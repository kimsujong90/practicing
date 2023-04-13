import collections

deque0 = collections.deque()

from collections import deque

queue = deque()
for i in range(5):
    queue.appendleft(i)

print(f"queue:{queue}")

stack = deque()
for i in range(5):
    stack.append(i)

print(f"stack:{stack}")

stack.rotate(2)
print(f"stack:{stack}")

queue.rotate(2)
print(f"queue:{queue}")