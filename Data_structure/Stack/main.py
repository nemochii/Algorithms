"""
from stackarray import StackArray

s = StackArray(5)

s.Push(3)
s.Push(4)
s.Push(5)

s.Pop()

s.getSize()

s.Top()
"""

from stacklinked_list import StackLinked_list

s = StackLinked_list(5)

s.Push(4)
s.Push(3)

s.Pop()

s.Top()

s.IsEmpty()
s.getSize()