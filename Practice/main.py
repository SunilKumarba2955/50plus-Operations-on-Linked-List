class Solution:
    def insert_At_Front(self, head, data):
        node = Node(data)
        node.next = head
        return node
    
    def insert_At_End(self, head, data):
        node = Node(data)
        if head:
            temp = head
            while temp.next:
                temp = temp.next
            temp.next = node
        else:
            head = node
        return head

# Driver code starts here please Don't touch here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end='->')
            temp = temp.next
        print()

if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().strip().split()))
    Llist = LinkedList()
    for i in range(n):
        Llist.head = Solution().insert_At_Front(Llist.head, l[i])
        Llist.display()
    NLlist = LinkedList()
    for i in range(n):
        NLlist.head = Solution().insert_At_End(NLlist.head, l[i])
        NLlist.display()

