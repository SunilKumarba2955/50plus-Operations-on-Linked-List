<h2><a href="https://www.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1">012. Remove duplicates from an unsorted linked list</a></h2><h3>Easy</h3><hr><p>Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. When a value appears in multiple nodes, the node which appeared first should be kept, all others duplicates are to be removed.</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
Input:
N = 4
value[] = {5,2,2,4}
Output: 5 2 4
Explanation:Given linked list elements are
5->2->2->4, in which 2 is repeated only.
So, we will delete the extra repeated
elements 2 from the linked list and the
resultant linked list will contain 5->2->4
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
Input:
N = 5
value[] = {2,2,2,2,2}
Output: 2
Explanation:Given linked list elements are
2->2->2->2->2, in which 2 is repeated. So,
we will delete the extra repeated elements
2 from the linked list and the resultant
linked list will contain only 2.
</pre>

<h3>Your Task:</h3>
<p>
You have to complete the method removeDuplicates() which takes 1 argument: the head of the linked list.  Your function should return a pointer to a linked list with no duplicate element.
</p>

<p><b>Expected time complexity:</b> O(N) </br>
<b>Expected auxiliary space:</b> O(N)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<p>1 <= size of linked lists <= 10^6 </br>
0 <= numbers in list <= 10^4</p>
