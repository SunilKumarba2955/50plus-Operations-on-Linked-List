<h2><a href="https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1">011. Remove duplicate element from sorted Linked List</a></h2><h3>Easy</h3><hr><p>Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists). </br>
Note: Try not to use extra space. The nodes are arranged in a sorted way.</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
Input:
LinkedList: 2->2->4->5
Output: 2 4 5
Explanation: In the given linked list 
2 ->2 -> 4-> 5, only 2 occurs more 
than 1 time. So we need to remove it once.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
Input:
LinkedList: 2->2->2->2->2
Output: 2
Explanation: In the given linked list 
2 ->2 ->2 ->2 ->2, 2 is the only element
and is repeated 5 times. So we need to remove
any four 2.
</pre>

<h3>Your Task:</h3>
<p>
The task is to complete the function removeDuplicates() which takes the head of input linked list as input. The function should remove the duplicates from linked list and return the head of the linkedlist.
</p>

<p><b>Expected time complexity:</b> O(N) </br>
<b>Expected auxiliary space:</b> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<p>1 <= Number of nodes <= 10^5</p>
