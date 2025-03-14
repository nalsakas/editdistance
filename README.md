# Edit distance problem
## Problem Statement
For a given two words (strings), only insert, delete and replace operations are allowed to convert word1 into word2.

word1: a b d --> i index
word2: a c d --> j index

allowed operations:
- Do nothing
- Replace character
- Delete character
- Insert character

Input: word1, word2
Output: minimum number of operations needed to convert word1 into word2?

## Solution
DFS algorithm will be used to to recurring nature of the problem. Word1 can be any string including an empty string.
 Two indexes i and j will be used to track word1 and word2. Termination condition is when index on word2 reaches to the end.
"""
