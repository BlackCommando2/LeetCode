class MyQueue(object):
    def __init__(self):
        self.queue=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.queue:
            pop = self.queue[0]
            self.queue = self.queue[1:]
            return pop
        else:
            return []

    def peek(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        else:
            return []

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()