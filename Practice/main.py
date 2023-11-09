# class Solution:
#     def insert_At_Front(self, head, data):
#         node = Node(data)
#         node.next = head
#         return node
    
#     def insert_At_End(self, head, data):
#         node = Node(data)
#         if head:
#             temp = head
#             while temp.next:
#                 temp = temp.next
#             temp.next = node
#         else:
#             head = node
#         return head

# # Driver code starts here please Don't touch here
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
    
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end='->')
#             temp = temp.next
#         print()

# if __name__ == '__main__':
#     n = int(input())
#     l = list(map(int, input().strip().split()))
#     Llist = LinkedList()
#     for i in range(n):
#         Llist.head = Solution().insert_At_Front(Llist.head, l[i])
#         Llist.display()
#     NLlist = LinkedList()
#     for i in range(n):
#         NLlist.head = Solution().insert_At_End(NLlist.head, l[i])
#         NLlist.display()



def distinct_strings(s):
    # Define the modulo value
    MOD = 10**9 + 7

    # Set to store distinct non-empty strings
    result_set = set()

    # Recursive function to generate strings
    def generate_strings(index, prev_char, temp_str):
        nonlocal result_set

        # Base case: reached end of the string
        if index == len(s):
            result_set.add(temp_str)
            return

        # Recursive case: take the current character if it is not adjacent to the previous character
        if prev_char != s[index]:
            generate_strings(index + 1, s[index], temp_str + s[index])

        # Recursive case: do not take the current character
        generate_strings(index + 1, prev_char, temp_str)

    # Start the recursion from index 0
    generate_strings(0, '', '')

    # Convert set to list and return the count modulo 10^9+7
    result_count = len(result_set) % MOD
    return result_count

s = "dd"

# Get distinct strings modulo 10^9+7
result = distinct_strings(s)
print(result)

