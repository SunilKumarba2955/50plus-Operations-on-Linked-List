<h2><a href="https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1">014. Reverse a Linked List in groups of given size</a></h2><h3>Medium</h3><hr><p>Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5 
Explanation: 
The first 4 elements 1,2,2,4 are reversed first 
and then the next 4 elements 5,6,7,8. Hence, the 
resultant linked list is 4->2->2->1->8->7->6->5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4 
Explanation: 
The first 3 elements are 1,2,3 are reversed 
first and then elements 4,5 are reversed.Hence, 
the resultant linked list is 3->2->1->5->4.
</pre>

<h3>Your Task:</h3>
<p>
You don't need to read input or print anything. Your task is to complete the function reverse() which should reverse the linked list in group of size k and return the head of the modified linked list.
</p>

<p><b>Expected time complexity:</b> O(N) </br>
<b>Expected auxiliary space:</b> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<p>1 <= N <= 10^5 </br>
1 <= k <= N</p>
