<h2><a href="https://practice.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1">003. Delete a Node in Singly Linked List</a></h2><h3>Easy</h3><hr><p>Given a singly linked list and an integer x.Delete xth node from the singly linked list.</p>

Example 1:
<pre>
Input: 1 -> 3 -> 4 
       x = 3
Output: 1 -> 3
Explanation:
After deleting the node at 3rd
position (1-base indexing), the
linked list is as 1 -> 3. 
</pre>
Example 2:

<pre>
Input: 1 -> 5 -> 2 -> 9 
x = 2
Output: 1 -> 2 -> 9
Explanation: 
After deleting the node at 2nd
position (1-based indexing), the
linked list is as 1 -> 2 -> 9.
</pre>

Your task: Your task is to complete the method deleteNode() which takes two arguments: the address of the head of the linked list and an integer x. The function returns the head of the modified linked list.


Constraints: <br/>
2 <= N <= 105 <br/>
1 <= x <= N