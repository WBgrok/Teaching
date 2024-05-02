class Queue:
  # Implement the class here
  pass




"""
Do not change the code below - use it to find out what methods are expected
"""
q = Queue()
q.show()
q.enqueue("job2")
q.enqueue("job3")
q.show()
q.enqueue("job4")
q.enqueue("job5")
q.show()
q.showFront()
q.dequeue()
q.dequeue()
q.dequeue()
q.show()
q.dequeue()
q.show()
q.dequeue()
print(q.dequeue())