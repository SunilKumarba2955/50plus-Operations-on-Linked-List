<h2><a href="https://www.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1">015. Delete nodes having greater value on right</a></h2><h3>Medium</h3><hr><p>Given a singly linked list, remove all the nodes in the list which have any node on their right whose value is greater. (Not just immediate Right , but entire List on the Right)</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
Input:
LinkedList = 12->15->10->11->5->6->2->3
Output: 15 11 6 3
Explanation: Since, 12, 10, 5 and 2 are
the elements which have greater elements
on the following nodes. So, after deleting
them, the linked list would like be 15,
11, 6, 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
Input:
LinkedList = 10->20->30->40->50->60
Output: 60
Explanation: All the nodes except the last
node has a greater value node on its right,
so all the nodes except the last node must
be removed.
</pre>

<h3>Your Task:</h3>
<p>
The task is to complete the function compute() which should modify the list as required and return the head of the modified linked list. 
The printing is done by the driver code,
</p>

<p><b>Expected time complexity:</b> O(N) </br>
<b>Expected auxiliary space:</b> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<p>1 ≤ size of linked list ≤ 10^5 </br>
1 ≤ element of linked list ≤ 10^5</p>

<p><b>Note: Try to solve the problem without using any extra space.</b></p>
