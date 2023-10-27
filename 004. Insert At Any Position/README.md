<h2><a href="https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem">004. Insert a node at a specific position in a linked list
</a></h2><h3>Easy</h3><hr><p>Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its <code>data</code> attribute, insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.</p>

<b>Example</b> <br/>
<code>head</code> refers to the first node in the list <code>1 -> 2 -> 3</code> <br/>
<code>data = 4</code> <br/>
<code>position = 2</code>

Insert a node at position <code>2</code> with <code>data = 4</code>. The new list is <code>1 -> 2 -> 4 -> 3</code>

<b>Function Description</b> Complete the function insertNodeAtPosition in the editor below. It must return a reference to the head node of your finished list.

insertNodeAtPosition has the following parameters:

- head: a SinglyLinkedListNode pointer to the head of the list
- data: an integer value to insert as data in your new node
- position: an integer position to insert the new node, zero based indexing

<b>Returns</b>

- SinglyLinkedListNode pointer: a reference to the head of the revised list

<b>Input Format</b>

The first line contains an integer , the number of elements in the linked list.

Each of the next <code>n</code> lines contains an integer SinglyLinkedListNode[i].data.

The next line contains an integer , the data of the node that is to be inserted.

The last line contains an integer <code>position</code>.

<b>Constraints:</b> <br/>
- <code>1 <= n <= 1000</code> </br>
- <code>1 <= SinglylinkedListNode[i].data <= 1000</code>, where  is the  element of the linked list.
- <code>0 <= position <= n</code>

<b>Sample Input</b>
<pre>3
16
13
7
1
2</pre>

<b>Sample Output</b>
<pre>16 13 1 7</pre>

<b>Explanation</b>

The initial linked list is <code>16 -> 13 -> 7</code>. Insert 1 at the position 2 which currently has 7 in it. The updated linked list is <code>16 -> 13 -> 1 -> 7</code>.