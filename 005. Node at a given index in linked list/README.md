<h2><a href="https://practice.geeksforgeeks.org/problems/node-at-a-given-index-in-linked-list/1">005. Node at a given index in linked list</a></h2><h3>Easy</h3><hr><p>Given a singly linked list with N nodes and a number X. The task is to find the node at the given index (X)(1 based index) of linked list.</p>

<b>Input:</b> </br>
First line of input contains number of testcases T. For each testcase, first line of input contains space seperated two integers, length of linked list and X.

<b>Output:</b> </br>
For each testcase, there will be single line of output containing data at Xth node.

<b>User Task:</b> </br>
The task is to complete the function <b>GetNth()</b> which takes head reference and index as arguments and should return the data at Xth position in the linked list.

<b>Constraints:</b> <br/>
1 <= T <= 30 <br/>
1 <= N <= 100 <br/>
X <= N <br/>
1 <= value <= 103

<b>Example:</b>
<pre>
<b>Input:</b>
6 5
1 2 3 4 657 76
10 2
8 7 10 8 6 1 20 91 21 2
</pre>

<pre>
Output:
657
7
</pre>

<b>Explanation:</b> </br>
Testcase 1: Element at 5th index in the linked list is 657 (1-based indexing).