class Node:
    def __init__(self, value, prevNode=None, nextNode=None):
        self.value = value
        self.prev = prevNode
        self.next = nextNode
        
class DoublyLinkedList:
    def __init__(self, _list=None):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def getList(self):
        result = []
        currentNode = self.head
        while currentNode.next.next:
            currentNode = currentNode.next
            result.append(currentNode.value)
        return result

    def insertAfter(self, prevNode, newNode):
        nextNode = prevNode.next
        newNode.prev, newNode.next = prevNode, nextNode
        prevNode.next = nextNode.prev = newNode
        self.nodeCount += 1
        return True
    
    def insertAt(self, position, newNode) -> bool:
        if position < -1 or position > self.nodeCount:
            return False

        prevNode = self.getAt(position - 1)
        return self.insertAfter(prevNode, newNode)
    
    def popAfter(self, prevNode):
        currentNode = prevNode.next
        nextNode = currentNode.next
        value = currentNode.value
        prevNode.next, nextNode.prev = nextNode, prevNode
        self.nodeCount -= 1
        return value
    
    def popAt(self, position):
        if position < 0 or position > self.nodeCount - 1:
            return False
        
        prevNode = self.getAt(position - 1)
        return self.popAfter(prevNode)
    
    def getAt(self, position) -> Node:
        if position < -1 or position > self.nodeCount:
            raise IndexError()
        
        isCloseToTail = position >= self.nodeCount // 2
        currentNode = self.tail if isCloseToTail else self.head
        iteration = self.nodeCount - position if isCloseToTail else position + 1
        for i in range(iteration):
            currentNode = currentNode.prev if isCloseToTail else currentNode.next
        return currentNode
    
    def __str__(self):
        return f"DoublyLinkedList({self.getList()})"