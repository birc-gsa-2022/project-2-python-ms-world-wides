[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8635020&assignment_repo_type=AssignmentRepo)
# Project 2: Suffix tree construction

You should implement a suffix tree construction algorithm. You can choose to implement the naive O(n²)-time construction algorithm as discussed in class or McCreight’s O(n) construction algorithm. After that, implement a search algorithm (similar to slow-scan) for finding all occurrences of a pattern. This algorithm should run in O(m+z) where m is the length of the pattern and z the number of occurrences.

Write a program, `st` using the suffix tree exact pattern search algorithm (similar to slow-scan) to report all indices in a string where a given pattern occurs. 

The program should take the same options as in project 1: `st genome.fa reads.fq`. The program should output (almost) the same SAM file. Because a search in a suffix tree is not done from the start to the end of the string the output might be in a different order, but if you sort the output from the previous project and for this program, they should be identical.

## Evaluation

Implement the tool `st` that does exact pattern matching using a suffix tree. Test it to the best of your abilities, and then fill out the report below.

# Report

## Specify if you have used a linear time or quadratic time algorithm.
In the implementation we used the quadratic time algorithm. 
## Insights you may have had while implementing and comparing the algorithms.

## Problems encountered if any.
Not explicit return statement caused very weird problems with None being returned in certain cases.Apart from that using many different variables for indexing into the suffix, edge and the whole string caused some confusion and incorrect results. 

## Correctness

To check the correctness of the algorithm we compared the output of our match-algorithm with the output of the linear exact matching algorithm from project one.

## Running time

### Constructing algorithm
The algorithm we implemented for constructing the tree takes no longer than O(n²), because for all n suffixes of x we walk trough the tree once (upper bound n steps per suffix), until it mismatches and then update/insert the (new) node(s) in linear time.

A worst case input in this implementation would be x = a^n, because in every iteration we have to walk down the whole suffix until we reach the $ and then add a new node.

A best case input would be a String x of unique characters, because for every suffix we would mismatch in the fist step and then insert a new node to the root in linear time. -> O(n)

In the following plot the running time is quadratic, as expected, for the worst case (x = a^n). For a random sequence (average case) the running time seems to be linear.
![](fig/Figure_compare_runtime_construct.png)


### Search algorithm
The implemented algorithm for the search is O(m+Z), because for a pattern of length m we only need to walk down the tree (max. m steps) until a mismatch occurs (slow-scan) and then report all the leafs "Z" of the "subtree" by jumping from parents to children via links (fast-scan). The figure below shows this: 
![](fig/rand_search.png)

In the figure we decided to plot a Tree with length(x) = 1000 and patterns from length 5 to 100 and, because for smaller patterns (length < 5) then the m becomes negligible in comparison to Z (as explained more in detail below).

A best case input could look like T(x) with x = a^n and p = b^m, because the pattern would mismatch in the first step and no leaves would be reported.

A worst case input could be the T(x) of x = a^n and p = a, because we would have to report all n leaves. The shorter the p, the more leaves we need to report which has a high impact on the runtime -> O(m+Z) 
![](fig/Increasing_matches.png)


