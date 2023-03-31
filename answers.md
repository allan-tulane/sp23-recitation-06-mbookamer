# CMPS 2200 Recitation 6
## Answers

**Name:**Mackenzie Bookamer


Place all written answers from `recitation-06.md` here for easier grading.



- **d.**

![A0730861-54F9-477F-A752-7047DD9E9B3E_4_5005_c](https://user-images.githubusercontent.com/79340162/228989019-7094ed22-416a-437f-b273-9b9f636dc478.jpeg)

I do notice a pattern, namely that the Huffman cost is more work efficient than the fixed length cost in every file the code was run on. The average ratio of huffman cost: fixed length cost is abour 0.67/0.68, which shows a large improvement over the fixed length cost, especially with text files with lots of characters such as 'alice29.txt' and 'asyoulik.txt.'
File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    |                     |                |
alice29.txt    |                     |                |
asyoulik.txt    |                     |                |
grammar.lsp    |                     |                |
fields.c    |                     |                |




- **e.**

Over our alphabet $\Sigma$ we would expect the cost to be a sum from i =1 to i=n of $i^2$x, where x is our frquency of every node. This is because at every level, we have i nodes. Then, every level has a cost of $i^2$x, since the first level has 1 node encoded with 1 bit with frquency f, the second level has 2 nodes encoded with 2 bits with frequency f, and so on. In order to find the total cost, we just add all the levels together until we get to the $n^2$x level. This is consistent across all documents so long as the document uses either the whole $\Sigma$ or the same unique characters and each occurs with the same frequency x. 


