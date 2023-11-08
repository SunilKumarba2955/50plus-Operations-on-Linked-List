<h2><a href="https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1">008. Remove loop in Linked List</a></h2><h3>Medium</h3><hr><p>Given a linked list of <code>N</code> nodes such that it may contain a loop.</p>

<p>A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.</p>

<p>Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
Input:
N = 3
value[] = {1,3,4}
X = 2
Output: 1
Explanation: The link list looks like
1 -> 3 -> 4
     ^    |
     |____|    
A loop is present. If you remove it 
successfully, the answer will be 1. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output: 1
Explanation: The Linked list does not 
contains any loop. 
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
Input:
N = 4
value[] = {1,2,3,4}
X = 1
Output: 1
Explanation: The link list looks like 
1 -> 2 -> 3 -> 4
^              |
|______________|
A loop is present. 
If you remove it successfully, 
the answer will be 1. 
</pre>

<h3>Your Task:</h3>
<p>
You don't need to read input or print anything. Your task is to complete the function removeLoop() which takes the head of the linked list as the input parameter. Simply remove the loop in the list (if present) without disconnecting any nodes from the list.
<p><b>Note: </b>The generated output will be 1 if your submitted code is correct.</p> 
</p>

<p><b>Expected time complexity:</b> O(N) </br>
<b>Expected auxiliary space:</b> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<p>1 ≤ N ≤ 10^4</p>
