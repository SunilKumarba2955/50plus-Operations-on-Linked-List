<h2><a href="https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1">013. Rotate a Linked List</a></h2><h3>Medium</h3><hr><p>Given a singly linked list of size N. The task is to left-shift the linked list by k nodes, where k is a given positive integer smaller than or equal to length of the linked list.</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
Input:
N = 5
value[] = {2, 4, 7, 8, 9}
k = 3
Output: 8 9 2 4 7
Explanation:
Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
Input:
N = 8
value[] = {1, 2, 3, 4, 5, 6, 7, 8}
k = 4
Output: 5 6 7 8 1 2 3 4
</pre>

<h3>Your Task:</h3>
<p>
You don't need to read input or print anything. Your task is to complete the function rotate() which takes a head reference as the first argument and k as the second argument, and returns the head of the rotated linked list.
</p>

<p><b>Expected time complexity:</b> O(N) </br>
<b>Expected auxiliary space:</b> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<p>1 <= N <= 10^3 </br>
1 <= k <= N</p>
