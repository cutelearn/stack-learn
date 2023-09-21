class StackOverflowError(Exception):
    pass

class StackUnderflowError(Exception):
    pass

class Stack:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def push(self, item):
        """將元素加入堆頂"""
        if self.size() >= self.capacity:
            raise StackOverflowError("堆疊溢位")
        self.items.append(item)

    def pop(self):
        """從堆頂移除並返回元素"""
        if self.is_empty():
            raise StackUnderflowError("堆疊下溢")
        return self.items.pop()

    def peek(self):
        """查看堆頂元素，但不移除它"""
        if self.is_empty():
            raise StackUnderflowError("堆疊下溢")
        return self.items[-1]

    def is_empty(self):
        """判斷堆疊是否為空"""
        return len(self.items) == 0

    def size(self):
        """返回堆疊的大小"""
        return len(self.items)
