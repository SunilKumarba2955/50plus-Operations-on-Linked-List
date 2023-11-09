<h2><a href="https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1">010. Finding middle element in a linked list</a></h2><h3>Easy</h3><hr><p>Given a singly linked list of N nodes.
The task is to find the middle of the linked list. For example, if the linked list is
1-> 2->3->4->5, then the middle node of the list is 3.
If there are two middle nodes(in case, when N is even), print the second middle element. </br>
For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
Input:
LinkedList: 1->2->3->4->5
Output: 3 
Explanation: 
Middle of linked list is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
Input:
LinkedList: 2->4->6->7->5->1
Output: 7 
Explanation: 
Middle of linked list is 7.
</pre>

<h3>Your Task:</h3>
<p>
The task is to complete the function getMiddle() which takes a head reference as the only argument and should return the data at the middle node of the linked list.
</p>

<p><b>Expected time complexity:</b> O(N) </br>
<b>Expected auxiliary space:</b> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<p>1 <= N <= 5000</p>
