'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
# Solution for deletion operation in Linked list
class Solution:
    def deleteAtBegining(self, head):
        return head.next if head else head

    def deleteAtEnd(self, head):
        if head and head.next:
            temp = head
            while temp.next.next:
                temp = temp.next
            temp.next = None
        else:
            head = None
        return head
        

    def deleteAtMiddle(self, head):
        if head and not head.next:
            return None
        elif head.next and not head.next.next:
            temp = head.next
            return temp
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head

# Driver code starts here please Don't touch here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


def printList(head):
    while head:
        print(head.data, end='->')
        head = head.next
    print()


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()

        nodes_info = list(map(int, input().split()))
        for i in nodes_info:
            a.push(i)
        printList(a.head)
        while True:
            print('1. Delete at Begining')
            print('2. Delete at End')
            print('3. Delete at Middle')
            ch = int(input('Enter your choice: '))
            match ch:
                case 1:
                    a.head = Solution().deleteAtBegining(a.head)
                    printList(a.head)
                case 2:
                    a.head = Solution().deleteAtEnd(a.head)
                    printList(a.head)
                case 3:
                    a.head = Solution().deleteAtMiddle(a.head)
                    printList(a.head)
                case _:
                    break
        printList(a.head)