"""
from queuelinked_list import QueueLinked_list

q = QueueLinked_list(2)

q.Push(3)
q.Push(4)
q.Push(5)

q.Pop()

q.getFront()

q.getBack()

q.IsEmpty()

q.getSize()
"""
"""
from queuearray import QueueArray

q = QueueArray(5)

q.Push(3)
q.Push(4)
q.Push(5)

q.Pop()

q.getFront()

q.getBack()

q.IsEmpty()

q.getSize()
"""

from circularqueuearray import CircularQueueArray

q = CircularQueueArray(5)

q.Push(3)
q.Push(4)
q.Push(5)

q.Pop()

q.Push(6)

q.Pop()

q.Push(7)
q.Push(8)

q.getFront()

q.getBack()

q.getSize()