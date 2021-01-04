class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class doubleLinkedList:
    def __init__(self):
        self.head = None #double linked-list의 Head Node를 가리킨다

    def addFirst(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newNode = Node(data)
            current = self.head
            newNode.next = current
            current.prev = newNode
            self.head = newNode

    def addLast(self, data): #double linked-list의 마지막에 Node(data)를 연결
        newNode = Node(data)

        if self.head == None:
            self.head = newNode

        else:
            current = self.head

            while current.next != None:
                current = current.next

            current.next = newNode
            newNode.prev = current.next


    def addNode(self, data, key): #linked-list의 data값을 key로 검색해 그 뒤에 Node를 추가

        newNode = Node(data)

        if self.head == None:
            self.head = newNode

        else:
            current = self.head
            while current.data != key:
                current = current.next

                if current == None:
                    print("Key value doesn't exist")

            Next = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = Next
            Next.prev = newNode

    def printNode(self):
        if self.head == None:
            return
        else:
            current = self.head

            while current != None:
                print(current.data)
                current = current.next

N = int(input())
dLL = doubleLinkedList()
for i in range(N):
    dLL.addLast(int(input()))

dLL.addNode(3, 2)

dLL.printNode()



