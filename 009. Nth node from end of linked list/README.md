<h2><a href="https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1">009. Nth node from end of linked list</a></h2><h3>Easy</h3><hr><p>Given a linked list consisting of <code>L</code> nodes and given a number <code>N</code>. The task is to find the <code>N<sup>th</sup></code> node from the end of the linked list.</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output: 8
Explanation: In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end is 8.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
Input:
N = 5
LinkedList: 10->5->100->5
Output: -1
Explanation: In the second example, there
are 4 nodes in the linked list and we
need to find 5th from the end. Since 'n'
is more than the number of nodes in the
linked list, the output is -1.
</pre>

<h3>Your Task:</h3>
<p>
The task is to complete the function getNthFromLast() which takes two arguments: reference to head and N and you need to return Nth from the end or -1 in case node doesn't exist.
<p><b>Note: </b>Try to solve in a single traversal.</p> 
</p>

<p><b>Expected time complexity:</b> O(N) </br>
<b>Expected auxiliary space:</b> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<p>1 <= L <= 10^6 </br>
1 <= N <= 10^6</p>
