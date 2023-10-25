'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    # Code here
    if head:
        prev = None
        cur = head
        pos = 1
        while pos!=k and cur:
            prev = cur
            cur = cur.next
            pos+=1
        if prev==None:
            head = head.next
        elif cur:
            prev.next = cur.next
    return head


#{ 
 # Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
            self.last = self.head
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.last.next = new_node
            self.last = new_node

def printlist(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        k = int(input())
        newhead = delNode(list1.head, k)
        printlist(newhead)