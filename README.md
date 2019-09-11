# Fibonacci_Sequence
This program gets number at certain point in the fibonacci sequence. There are two functions that solve this problem, both with two different techniques to solve problem:

* Recursion, this technique involves algorithm calling it self on small part of the problem to solve the whole problem.

* Dynamic Programming, this technique involves breaking down the problem to sub-problem so that it can be solved. Then the algorithm stores those solutions to sub-problems so that it can make final solution.

Below is a table of time it took to process each function with each input size. Unit is in seconds

| Input Size    | Dynamic Programming | Recursion   |
| ------------- | ----------------- | ------------- |
| 1             | 0.00000117        | 0.00000088    |
| 2             | 0.00000498        | 0.00000176    |
| 3             | 0.00000440        | 0.00000176    |
| 4             | 0.00000322        | 0.00000322    |
| 5             | 0.00000381        | 0.00000440    |
| 10            | 0.00000440        | 0.00004162    |
| 20            | 0.00000762        | 0.00543822    |
| 30            | 0.00000967        | 0.71134917    |
| 40            | 0.00001964        | 92.63238730   |
| 50            | 0.00001993        | 10495.60328890|

As you can see being able to avoid re-computing the same sub-problem can save a lot of time when you scale up the input.
