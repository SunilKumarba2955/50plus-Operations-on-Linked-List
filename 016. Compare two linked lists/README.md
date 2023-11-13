<h2><a href="https://www.hackerrank.com/challenges/compare-two-linked-lists/problem">016. Compare two linked lists
</a></h2><h3>Easy</h3><hr><p>You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. If all data attributes are equal and the lists are the same length, return <code>1</code>. Otherwise, return <code>0</code>.

<b>Example</b> <br/>
<code>llist1 = 1 -> 2 -> 3 -> NULL</code> <br/>
<code>llist2 = 1 -> 2 -> 3 -> 4 -> NULL</code> <br/>

<p>
The two lists have equal data attributes for the first <code>3</code> nodes. <code>llist2</code>  is longer, though, so the lists are not equal. Return <code>0</code>.</p>

<b>Function Description</b> Complete the compare_lists function in the editor below.

compare_lists has the following parameters:

- SinglyLinkedListNode llist1: a reference to the head of a list
- SinglyLinkedListNode llist2: a reference to the head of a list

<b>Returns</b>

- int: return 1 if the lists are equal, or 0 otherwise

<b>Input Format</b>

The first line contains an integer <code>t</code>, the number of test cases.

Each of the test cases has the following format: </br>
The first line contains an integer <code>n</code>, the number of nodes in the first linked list. </br>
Each of the next <code>n</code> lines contains an integer, each a value for a data attribute. </br>
The next line contains an integer <code>m</code>, the number of nodes in the second linked list. </br>
Each of the next <code>m</code> lines contains an integer, each a value for a data attribute.

<b>Constraints:</b> <br/>
- <code>1 <= t <= 10</code> </br>
- <code>1 <= n,m <= 1000</code> </br>
- <code>1 <= llist1[i],llist2[i] <= 1000</code>

<b>Output Format</b>

Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to stdout/console.

The output is handled by the code in the editor and it is as follows:

For each test case, in a new line, print <code>1</code> if the two lists are equal, else print <code>0</code>.

<b>Sample Input</b>
<pre>2
2
1
2
1
1
2
1
2
2
1
2</pre>

<b>Sample Output</b>
<pre>0
1</pre>

<b>Explanation</b>

There are <code>t=2</code> test cases, each with a pair of linked lists.

In the first case, linked lists are: 1 -> 2 -> NULL and 1 -> NULL

In the second case, linked lists are: 1 -> 2 -> NULL and 1 -> 2 -> NULL.