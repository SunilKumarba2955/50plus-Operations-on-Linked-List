<h2><a href="https://practice.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0">001. Insert an element at Front and End of the Linked List</a></h2><h3>Basic</h3><hr><p>Create a link list of size N according to the given input literals. Each integer input is accompanied by an indicator which can either be 0 or 1. If it is 0, insert the integer in the beginning of the link list. If it is 1, insert the integer at the end of the link list. <br/> <br/>
Hint: When inserting at the end, make sure that you handle NULL explicitly.</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input: </strong>
LinkedList: 9->0->5->1->6->1->2->0->5->0
<strong>Output: </strong> 5 2 9 5 6
<strong>Explanation: </strong>
Length of Link List = N = 5
9 0 indicated that 9 should be
inserted in the beginning. Modified
Link List = 9.
5 1 indicated that 5 should be
inserted in the end. Modified Link
List = 9,5.
6 1 indicated that 6 should be
inserted in the end. Modified Link
List = 9,5,6.
2 0 indicated that 2 should be
inserted in the beginning. Modified
Link List = 2,9,5,6.
5 0 indicated that 5 should be
inserted in the beginning. Modified
Link List = 5,2,9,5,6. 
Final linked list = 5, 2, 9, 5, 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input: </strong>
LinkedList: 5->1->6->1->9->1
<strong>Output: </strong> 5 6 9
</pre>

<p>
<strong>Your Task: </strong> <br/>
You only need to complete the functions insertAtBeginning() and insertAtEnd() that takes the head of link list and integer value of the data to be inserted as inputs and returns the head of the modified link list.

<strong>Expected Time Complexity: </strong> O(1) for insertAtBeginning() and O(N) for insertAtEnd().  <br/>
<strong>Expected Auxiliary Space:</strong> O(1) for both.
</p>

<p><strong>Constraints:</strong></p>
<ul>
	<li>1 &lt;= N &lt;= 104</li>
</ul>