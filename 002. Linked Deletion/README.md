<h2  ><a href="https://www.geeksforgeeks.org/deletion-in-linked-list/" > 002. Deletion Operations in Linked List 
</a> </h2>
<p>Solution for deletion operations in a linked list. This program provides three deletion operations:</p>

<ol>
  <li>Delete at the beginning of the linked list.</li>
  <li>Delete at the end of the linked list.</li>
  <li>Delete at the middle of the linked list.</li>
</ol>

<h3>Your Task:</h3>

You are required to implement the following functions:

1. `deleteAtBegining(head)`: Deletes the first element of the linked list.
2. `deleteAtEnd(head)`: Deletes the last element of the linked list.
3. `deleteAtMiddle(head)`: Deletes the middle element of the linked list (or the first middle element in case of an even number of elements).

<h3>Expected Time and Space Complexity:</h3>

- `deleteAtBegining`: O(1) time and O(1) space.
- `deleteAtEnd`: O(N) time and O(1) space.
- `deleteAtMiddle`: O(N) time and O(1) space.

<h3>Constraints:</h3>

- 1 <= N <= 10^4

<h3>Usage:</h3>

1. Provide the number of test cases (t).
2. For each test case:
   - Input the length of the linked list (n).
   - Input the elements of the linked list.
   - Choose a deletion operation from the menu:
     - Delete at Beginning
     - Delete at End
     - Delete at Middle
   - Observe the modified linked list after each deletion operation.

<h3>Sample Test Case:</h3>

<h4>Sample Test Case: 1</h4>

<pre>
<strong>Input:</strong> 
1
5
1 2 3 4 5
1
2
3
4

<strong>Output:</strong> 2 4
<strong>Explanation: </strong> 
In the first query, choice is 1 means `deleteAtBegining`, now list becomes 2,3,4,5.
In the second query, choice is 2 means `deleteAtEnd`, now list becomes 2,3,4
In the third query, choice is 3 means `deleteAtMiddle`, now list becomes 2,4
In the fourth query, choice is exit.
So, final output is 2,4
</pre>

<h4>Sample Test Case: 2</h4>

<pre>
<strong>Input:</strong> 
1
10
10 1 5 23 69 10 14 20 9 4
3
3
1
2
4

<strong>Output:</strong> 2 4
<strong>Explanation: </strong> 
In the first query, choice is 3 means `deleteAtMiddle`, now list becomes 10, 1, 5, 23, 69, 14, 20, 9, 4.
In the second query, choice is 3 means `deleteAtMiddle`, now list becomes 10, 1, 5, 23, 14, 20, 9, 4.
In the third query, choice is 1 means `deleteAtBegining`, now list becomes 1, 5, 23, 14, 20, 9, 4.
In the Fourth query, choice is 2 means `deleteAtEnd`, now list becomes 1, 5, 23, 14, 20, 9.
So, final output is 1, 5, 23, 14, 20, 9.
</pre>
