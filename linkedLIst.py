class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#Linked List의 원소를 클래스로 지정. 클래스의 data에는 입력 변수를, next에는 다음 Node를 지정


class linkedList:
    def __init__(self):
        self.head = None

    #Linked List의 head Node를 가리킨다

    def addLast(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = Node(data)

    def addFirst(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode

        else:
            newNode.next = self.head
            self.head = newNode

    def addNode(self, data, key):
        current = self.head
        if current == None:
            self.head = Node(data)

        else:
            while current.data != key:
                current = current.next

                if current == None:
                    print("Key value doesn't exist")
                    return

            newNode = Node(data)
            newNode.next = current.next
            current.next = newNode

    def delFirst(self):
        current = self.head
        if current == None:
            return
        else:
            self.head = current.next
            del current

    def delLast(self):
        current = self.head

        if self.head == None:
            return

        else:
            while current.next != None:
                prev = current
                current = current.next

            prev.next = None
            del current

    def delNode(self, key):

        current = self.head
        if current == None:
            return

        else:
            while current.data != key:
                prev = current
                current = current.next

                if current == None:
                    print("Key value doesn't exist")
                    return
            prev.next = current.next
            del current

    def printNode(self):
        current = self.head
        while (current != None):
            print(current.data)
            current = current.next


n = int(input())
num = []
Nodes = linkedList()

for i in range(n):
    num.append(int(input()))
    Nodes.addLast(num[i])

Nodes.addNode(4, 3)
Nodes.addFirst(0)
Nodes.delNode(3)
Nodes.delLast()

Nodes.printNode()