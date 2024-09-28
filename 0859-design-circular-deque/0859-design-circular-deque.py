class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class MyCircularDeque:

    def __init__(self, k: int):
        self.head=None
        self.tail=None
        self.capacity=k
        self.k=k
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.head and not self.tail:
            node=Node(value)
            self.head=node
            self.tail=node
            self.capacity-=1
            return True
        node=Node(value)
        node.next=self.head
        self.head.prev=node
        self.head=node
        self.capacity-=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.head or not self.tail:
            node=Node(value)
            self.head=node
            self.tail=node
            self.capacity-=1
            return True
        node=Node(value)
        self.tail.next=node
        node.prev=self.tail
        self.tail=node
        self.capacity-=1
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.head==self.tail:
            self.head=None
            self.tail=None
            self.capacity+=1
            return True
        self.head.next.prev=None
        self.head=self.head.next
        self.capacity+=1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.head==self.tail:
            self.head=None
            self.tail=None
            self.capacity+=1
            return True
        self.tail.prev.next=None
        self.tail = self.tail.prev
        self.capacity+=1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.capacity==self.k

    def isFull(self) -> bool:
        return self.capacity<=0
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()